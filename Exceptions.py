try:
    file = open("linda.txt")
    content = file.read()
except FileNotFoundError:
    print("file not found bhadva")
except Exception as ex:
    print(ex)
else:
    if "file" in locals or not file.closed():
        file.close()
        print("closed")
finally:
    print("ef lodiii")





class Error(Exception):
    pass

class dob(Error):
    pass

year = int(input("dob "))
age = 2024  - year


try:

    if age <= 30 and age>= 20:
        print("valid")
    else:
        raise dob
except dob:
    print("not in limit")