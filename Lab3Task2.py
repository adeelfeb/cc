# Task 2
# this error :

# ~/adeelfeb/cc main
# ❯ python Lab3Task2.py
# String is not complete
# Traceback (most recent call last):
#   File "Lab3Task2.py", line 73, in <module>
#     StartState() 
#   File "Lab3Task2.py", line 61, in StartState
#     B_NonTerminal() 
#   File "Lab3Task2.py", line 50, in B_NonTerminal
#     B_NonTerminal()    
#   File "Lab3Task2.py", line 49, in B_NonTerminal
#     getNextToken()
#   File "Lab3Task2.py", line 27, in getNextToken
#     next_Token = expression[counterOfString]
# IndexError: index out of range






def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression


file_path = 'expression.txt'
expression = read_expression_from_file(file_path)
next_Token = expression[0]

counterOfString = 0


def displayError():
    print("This String is Invalid")


def getNextToken():
    global counterOfString
    global next_Token
    counterOfString= counterOfString + 1
    if( counterOfString < len(expression) ):
        next_Token = expression[counterOfString]
    else:
        print('String is not complete')
        return False
    return True


def A_NonTerminal():
    if(next_Token == '_'):
        getNextToken()
        return
    elif(next_Token.isalpha()):
        getNextToken()
        return
    else:
        displayError()
    
def B_NonTerminal():
    if(counterOfString >= len(expression)):
        return

    elif(next_Token == '_'):
        getNextToken()
        B_NonTerminal()
    elif(next_Token.isalpha()):
        getNextToken()
        B_NonTerminal()    
    elif(next_Token.isDigit()):
        next_Token()
        B_NonTerminal()
    else:
        displayError()



def StartState():
        A_NonTerminal() 
        B_NonTerminal() 

    
    






if __name__ == "__main__":

    StartState() 


    