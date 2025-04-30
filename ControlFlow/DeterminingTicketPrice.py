age = int(input())
price = 50
is_Student = input("are u a student?(y/n):").lower()
if age <5:
    price = "Free"
elif age <= 12:
    if is_Student =="y":
        price = 15
elif age <= 25:
    if is_Student =="y":
        price = price/2
else:
    price = price
print(price)
