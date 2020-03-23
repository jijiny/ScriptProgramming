import tkinter as tk
import tkinter.messagebox as msg

base = tk.Tk()
insert_money = tk.IntVar()
base.geometry("400x200")

def input_money() :                 #투입 버튼 클릭 시 실행 되는 함수
    global money                    #다른 함수에서도 사용해서 전역변수
    money = insert_money.get()      # entry에 입력받은 값
    rest_label = tk.Label(base, text = "투입된 금액은 "+ str(money) +"원 입니다        ").place(x=100, y=150)

def vending_coffee() :              #커피 선택 시 실행되는 함수
    global money
    if (money >= 500) :
            money = money - 500
            rest_label = tk.Label(base, text = "남은 금액 : " + str(money) + "원 입니다        ").place(x=100, y=150)
            msg.showinfo("Vending Machine", "커피     500원\n남은 금액 : " + str(money) +"원        \n")      #메세지 박스(인포메이션 아이콘, 정보, OK)
    else :
        rest_label = tk.Label(base, text = "돈이 부족합니다\n자판기를 종료합니다        ").place(x=100, y=150)

def vending_soda() :              #사이다 선택 시 실행되는 함수
    global money
    if (money >= 700) :
            money = money - 700
            rest_label = tk.Label(base, text = "남은 금액 : " + str(money) + "원 입니다        ").place(x=100, y=150)
            msg.showinfo("Vending Machine", "사이다     700원\n" + "남은 금액 : " + str(money) + "원        \n")
    else :
        rest_label = tk.Label(base, text = "돈이 부족합니다\n자판기를 종료합니다        ").place(x=100, y=150)

def vending_coke() :              #콜라 선택 시 실행되는 함수
    global money
    if (money >= 800) :
            money = money - 800
            rest_label = tk.Label(base, text = "남은 금액 : " + str(money) + "원 입니다        ").place(x=100, y=150)
            msg.showinfo("Vending Machine", "콜라     800원\n" + "남은 금액 : " + str(money) + "원        \n")      #메세지 박스(인포메이션 아이콘, 정보, OK)
    else :
        rest_label = tk.Label(base, text = "돈이 부족합니다\n자판기를 종료합니다        ").place(x=100, y=150)

def vending_grape() :              #포도주스 선택 시 실행되는 함수
    global money
    if (money >= 1000) :
            money = money - 1000
            rest_label = tk.Label(base, text = "남은 금액 : " + str(money) + "원 입니다        ").place(x=100, y=150)
            msg.showinfo("Vending Machine", "포도주스     1000원\n" + "남은 금액 : " + str(money) + "원        \n")      #메세지 박스(인포메이션 아이콘, 정보, OK)
    else :
        rest_label = tk.Label(base, text = "   돈이 부족합니다   \n자판기를 종료합니다     ").place(x=150, y=150)

def change() :              #반환 버튼 클릭 시 실행되는 함수
    global money
    yes_no = msg.askyesno("Vending Machine", "잔돈을 반환할까요?")      #메세지 박스 (예 / 아니오)
    if (yes_no == True) :       #메세지 박스('예'를 선택했을 때)
        rest_label = tk.Label(base, text = "남은 금액 : 0원 입니다         ").place(x=100, y=150)
        msg.showinfo("Vending Machine", "반환된 금액: " + str(money) + "원\n")      #메세지 박스(인포메이션 아이콘, 정보, OK)

coffee = tk.Button(base, text = "커피 \n500원", width = 8, command = vending_coffee).place(x=50, y=30)
soda = tk.Button(base, text = "사이다 \n700원", width = 8, command = vending_soda).place(x=130, y=30)
coke = tk.Button(base, text = "콜라 \n800원", width = 8, command = vending_coke).place(x=210, y=30)
grape = tk.Button(base, text = "포도주스 \n1000원", width = 8, command = vending_grape).place(x=290, y=30)

money_label = tk.Label(base, text = "돈을 투입하세요 : ").place(x=50, y=100)
money_entry = tk.Entry(base, textvariable = insert_money).place(x=150, y=100)
input = tk.Button(base, text = "투입", width = 5, command = input_money).place(x=300, y=95)
rest = tk.Button(base, text = "반환", width = 5, command = change).place(x=350, y=95)

base.mainloop()             # 하면이 계속 표시되게 유지
