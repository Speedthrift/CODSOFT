print("Calculator\n")

# stripNum = lambda n: n if n%1 else int(n)       #function for stripping insignificant 0s after decimal in float numbers 

def stripNum(n):
    if n%1: 
        return n
    else:
        return int(n)

try:
    num1 = stripNum(float(input("Enter the first number: ")))       #taking input of numbers from user
    num2 = stripNum(float(input("Enter the second number: ")))
    opr = input("Enter the operation to be performed (+ - * /):  ")     #taking input of operation 

    match opr:      #matching the entered operator by the user and display the result
        #addition
        case "+":       
            print(f"{num1} + {num2} =", stripNum(num1 + num2))
        #subtraction
        case "-":       
            print(f"{num1} - {num2} =", stripNum(num1 - num2))
        #multiplication
        case "*":       
            print(f"{num1} * {num2} =", stripNum(num1 * num2))
        #division
        case "/":       
            print(f"{num1} / {num2} =", stripNum(num1 / num2))
        #case when user entered something else (wrong operator)
        case _:         
            print("Wrong operator entered!")

except ValueError:      #handling if user entered non-numeric input when asked for numbers
    print("Please enter numeric values!")