def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression

def displayError():
    print("This String is Invalid")

# Declare the global variable
counterOfString = 0

def getNextToken(expression):
    global counterOfString
    counterOfString += 1
    next_Token = expression[counterOfString]
    return next_Token

def A_NonTerm():
    # Your implementation here
    pass

def StartState(expression):
    try:
        while True:
            next_Token = getNextToken(expression)
            if next_Token == 'a':
                # Your logic here
                pass
            elif next_Token == '_':
                # Your logic here
                pass
            else:
                displayError()
                break
    except IndexError:
        displayError()

# Example usage
expression = read_expression_from_file('expression.txt')
StartState(expression)
