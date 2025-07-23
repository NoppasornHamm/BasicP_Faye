has_rice = True
has_spoon = False

if has_rice:
    print("มีข้าวแล้ว")
    if has_spoon:
        print("มีช้อน กินข้าวได้")
    else:
        print("ไม่มีช้อน กินไม่ได้ จะใช้มือหรอจ๊ะ")
else:
    print("ไม่มีข้าว")


wake_up = False
on_the_way = False 

if wake_up:
    print("มอนิ่ง")
    if on_the_way:
        print("see yaaaaa")
    else:
        print("รีบมาจ้า")
else:
    print("ไม่ต้องมาแล้วก็ได้นะ")



#i is from index

for index in range(1, 6):
    print("Round:", index, "Hello World")

if index == 2:
    print("55555")


for index in range(1, 7):
    print("Hello World")
    if index == 3:
        print("Starter pack")



# num = int(input("Enter number: "))
# round = int(input("Enter times: "))

# for i in range(round):
#     minus_num = int(input())

#     print(num-minus_num)
#     num = (num-minus_num)
#     print("เหลือ: " ,num)
# print("Final: " ,num)

i = 0 
while i < 5:
    print("Hello")
    i = i + 1
    print(i)


i = 0 
while i < 5:
    print("Hello")
    print(i)
    break

#ถ้าเลือก 1 จะให้เลือกใหม่
#ถ้าเลือก 2 จะจบการทำงาน
while True:
    option = input("Enter number: ")
    if option == "1":
        print("try again")
    elif option == "2":
        break




