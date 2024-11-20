user_input = float(input("Enter a number less than 25:\n"))
if user_input > 25:
    print("Error")
else:
    for i in range(int(user_input), 26):
        print(f"Inside the loop, my variable is {i}")