try:
    print("Addition with 50")
    number = int(input("Enter a number: "))
    result = 50 + number

except ValueError:
    print("Not a valid number")

else:
    print(f"The amswer is {result}")

finally:
    print("The program has ended")