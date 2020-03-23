import sys
import os
import tkinter as tk
import serial
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

base = tk.Tk()
base.geometry("500x500")

status_out = Image.open("status_out.jpg")
status_in = Image.open("status_in.jpg")
triangle = Image.open("arrow.png")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

now = time.gmtime(time.time())
now_date = now.tm_year, '년', now.tm_mon, '월', now.tm_mday, '일', now.tm_hour+9, '시', now.tm_min, '분'
frame1=tk.Frame(base, relief="solid", bd=1, bg = "white")
frame1.pack(side="top", fill="both", expand=True)

frame2=tk.Frame(base, relief="solid", bd=1, bg = "white")
frame2.pack(side="bottom", fill="both", expand=True)

targetUrl = "http://aqicn.org/city/korea/gyeongbuk/gyeongju-si/kr"
html = urlopen(targetUrl).read()
soupData = BeautifulSoup(html, "html.parser")
titleData = soupData.find("a", id="aqiwgttitle1")
timeData = soupData.find("span", id="aqiwgtutime")
aqiData = soupData.find("div", id="aqiwgtvalue")
status_outdoor = ImageTk.PhotoImage(status_out)
status_indoor = ImageTk.PhotoImage(status_in)
arrow = ImageTk.PhotoImage(triangle)

ard = serial.Serial('COM5')
obj = ard.readline()
dust = obj[:-2].decode()

Label1 =tk.Label(frame1, text = "외부 대기질지수 (Air Quality Index)", font = ("돋움체","15","bold"), bg = "white").place(x=70, y=5)

location = tk.Label(frame1, text = titleData.string, font = "10", bg = "white").place(x=10,y=40)
date = tk.Label(frame1, text = timeData.string, font = "10", bg = "white").place(x=10, y=60)
condtion = tk.Label(frame1, text = aqiData.get("title"), font = "10", bg = "white").place(x=10,y=80)
num = tk.Label(frame1, text = aqiData.string + " ㎍/㎥", font = "10", bg = "white").place(x=10,y=100)
status_web = tk.Label(frame1, image = status_outdoor).place(x=15,y=140)
arrow1 = tk.Label(frame1, image = arrow).place(x=float(aqiData.string)*2.5 + 15,y=170)


Label2 =tk.Label(frame2, text = "내부 대기질지수 (Air Quality Index)", font = ("돋움체","15","bold"), bg = "white").place(x=70, y=5)

date_now = tk.Label(frame2, text = now_date , font = "10", bg = "white").place(x=10,y=40)
sensor_value = tk.Label(frame2, text = dust + " ㎍/㎥", font = "10", bg = "white").place(x=10,y=60)
restart_btn =tk.Button(frame2, text="UPDATE",bg="white", command=restart_program).place(x=110, y=60)
status_now = tk.Label(frame2, image = status_indoor).place(x=15,y=130)
arrow2 = tk.Label(frame2, image = arrow).place(x= float(dust)*6 + 15,y=160)

if (float(dust) <= 15.0) :
    tk.Label(frame2, text = "좋음", font = "10", bg = "white").place(x=10,y=80)
elif (15.0 < float(dust) <= 50.0) :
    tk.Label(frame2, text = "보통", font = "10", bg = "white").place(x=10,y=80)
else :
    tk.Label(frame2, text = "나쁨", font = "10", bg = "white").place(x=10,y=80)

base.mainloop()
