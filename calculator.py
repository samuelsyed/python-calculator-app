from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return  "You can't divide by zero!"

#Storing functions in dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculate(first_num,second_num,operation):
    result = operations[operation](first_num,second_num)
    return  result

def main():
    start = float(input("Enter your first number?: "))
    carry_on = True


    while carry_on:
        operand = input('Choose an operation: "+","-", "*","/": ')
        next_num = float(input("Enter your next num: "))
        final_result =  calculate(first_num=start,second_num=next_num,operation=operand)
        print(f"{start} {operand} {next_num} = {final_result}")
        proceed = input(f"Type 'y' to continue calculating with {final_result} : or type 'n' to start a new calculation: ").lower()
        if proceed == "y":
            start = final_result
        if proceed == "n":
            start = float(input("Enter your first number?: "))



if __name__ == "__main__":
    main()