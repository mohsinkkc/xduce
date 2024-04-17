#exception Handle
try:
    x = int(input("Enter a number: "))
    y = 10 / x
    print("Result:", y)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print("An error occurred:", e)
else:
    print("No exception occurred.")
finally:
    print("Program execution completed.")

    