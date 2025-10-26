"""Write a short interactive Python program of your choice that uses try and except to catch and respond to at least two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, a basic calculator, or even a simple quiz with input validation.
"""
def square_number():
    number = input("Enter a number to square: ")
    squared_number = int(number) ** 2
    print(f"The square of {number} is {squared_number}.")
    try:
        result = 10 / 5
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("That's not a number! Please enter a valid number.")
    else:
        print("Division successful!")
    finally:
        print("Execution completed.")
square_number()