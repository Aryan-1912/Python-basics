age = int(input("Enter your age"))
is_student = str(input("enter yes/ no")).lower()

if age< 10:
    price = "free"
elif age<=20:
    if is_student=="yes":
        price = "2"
    else:
        price = "3"
elif age <= 30:
    if is_student == "yes":
        price = "4"
    else:
        price = "5"
else:
    price = "70"


print(age, is_student, price)



