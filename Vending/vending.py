print("-------------Vending Machine--------------")
print("    1커피   2사이다  3콜라   4포도주스")
print("     500     700     800      1000 ")
print("------------------------------------------")
buy = input("음료를 구입하시겠습니까? (y/n) : ")

if (buy == 'y') :
    money = int(input("돈을 투입하세요 : "))
    if (money >= 500 ) :
        while 1 :
            drink = input("음료를 선택하세요 (1,2,3,4) : ")
            if(drink == '1' and money >= 500):
                print("커피     500원")
                money = money - 500
                print("남은 금액 : ", money,"원\n")

            elif (drink == '2' and money >= 700):
                print("사이다     700원")
                money = money - 700
                print("남은 금액 : ", money,"원\n")

            elif (drink == '3' and money >= 800):
                print("콜라     800원")
                money = money - 800
                print("남은 금액 : ", money,"원\n")

            elif (drink == '4' and money >= 1000):
                print("포도주스     1000원")
                money = money - 1000
                print("남은 금액 : ", money,"원\n")

            elif (money <= 1000) :
                print("돈이 부족합니다\n")

            else :
                print("잘못입력하셨습니다\n")

            if (money < 500 ) :
                print("자판기 종료")
                break

            buy = input("음료를 더 구입하시겠습니까? (y/n) : ")
            if (buy == 'n') :
                print("잔돈은 ", money, "원 입니다")
                print("자판기 종료")
                break
    else :
        print("돈이 부족합니다")
        print("자판기 종료")
else :
    print("자판기 종료")
