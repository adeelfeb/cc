# Task 1

# this error : 

# ❯ python Lab3.py
# _
# Traceback (most recent call last):
#   File "Lab3.py", line 125, in <module>
#     StartState() 
#   File "Lab3.py", line 110, in StartState
#     getNextToken()
#   File "Lab3.py", line 90, in getNextToken
#     counterOfString= counterOfString + 1
# UnboundLocalError: local variable 'counterOfString' referenced before assignment

# for this code ;


def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression


file_path = 'expression.txt'
expression = read_expression_from_file(file_path)
next_Token = expression[0]
print(next_Token)
counterOfString = 0


def displayError():
    print("This String is Invalid")


def getNextToken():
    counterOfString= counterOfString + 1
    next_Token = expression[counterOfString]


def A_NonTerminal():
    if(next_Token == 'a'):
        getNextToken()
        A_NonTerminal()
    
    elif(next_Token == 'b' & counterOfString == (expression.length - 1)):
        print('The String is Valid!')
    
    else:
        displayError()
    



def StartState():
    if(next_Token == '_'):
        getNextToken()
        A_NonTerminal()
    
    else:
        displayError()
    
    






if __name__ == "__main__":

    StartState() 