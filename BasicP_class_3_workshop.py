monster = 100

knife = 10
gun = 20
bomb = 30

while True:
    print("1.โจมตีมอนเตอร์")
    print("2.หนีดีกว่า")
    choice = int(input("พิมพ์ 1 / 2 เพื่อเลือก: "))
    if choice == 1:
        round = int(input("จะตีกี่ที เอาให้ชนะ : "))
        for i in range(round):
                weapon = str(input("chooes one, knife gun bomb : "))
                if weapon == "knife":
                    num = (monster-knife)
                if weapon == "gun":   
                    num = (monster-gun)
                if weapon == "bomb":
                    num = (monster-bomb)
                else:
                     print("ไปเล่นที่อื่นเนาะ")
                if monster < 0 :
                     monster = 20
        print(num)
    if monster == 0:
         print("You win, monster dieddddddddddddd")
    else:
         print("You died")
        