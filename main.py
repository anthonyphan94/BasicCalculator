from art import logo
print(logo)

def add(n1, n2):
    return n1+ n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

my_operator = {
    '+' : add,
    '-' : substract,
    '*' : multiply,
    '/' : divide
}

#What's the next number?: 
def calculator():

    first_number = float(input("What's the first number?: "))
    isContinue = True

    while isContinue:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What is the next number?: "))
        calculation = my_operator[operation_symbol]
        answer= calculation(first_number, second_number)
        answer_float = '{:.2f}'.format(answer)
        print("{first} {symbol} {second} = {result}"
            .format(first=first_number, second=second_number, symbol = operation_symbol, result=answer_float))
        get_continue = input("Type 'y' to continue, or type 'n' to exit: ")
        # Replace first number with the last answer
        if get_continue == 'y':
            first_number = answer
        else:
            isContinue = False

calculator()