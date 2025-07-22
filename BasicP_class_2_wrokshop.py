distance = float(input("Enter your distance (KM.): "))

if  5 <= distance and distance <= 50:
    print("Price is 10 ฿")
elif 51 <= distance and distance <= 100:
    print("price is 15 ฿")
elif 101 <= distance and distance <= 300:
     print("Price is 25 ฿")
elif 301 <= distance and distance <= 500:
    print("Price is 35 ฿")
elif distance >= 500:
    print("Price is 45 ฿")
else:
    print("Are you serious?")


