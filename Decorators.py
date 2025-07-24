def main(func):
    def sub_main():
        print("before")
        print(func())
        print("after")
    return sub_main

@main
def course():
    return "lododododo"
course()
