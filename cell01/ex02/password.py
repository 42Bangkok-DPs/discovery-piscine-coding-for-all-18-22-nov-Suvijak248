password = "Python is awesome"

def main():
    user_input = input("Enter password: ")

    if user_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    main()