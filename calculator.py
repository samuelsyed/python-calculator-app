from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

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

recent_result = []
start = float(input("Enter your first number?: "))
carry_on = True


while carry_on:
    operand = input('Choose an operation: "+","-", "*","/": ')
    next_num = float(input("Enter your next num: "))
    final_result =  calculate(first_num=start,second_num=next_num,operation=operand)
    recent_result.append(final_result)
    print(f"{start} {operand} {next_num} = {final_result}")
    proceed = input(f"Type 'y' to continue calculating with {final_result} : or type 'n' to start a new calculation: ").lower()
    if proceed == "y":
        if len(recent_result) == 1:
            index = 0
        else:
            index = -1
        start = recent_result[-1]
    if proceed == "n":
        recent_result = []
        start = float(input("Enter your first number?: "))
