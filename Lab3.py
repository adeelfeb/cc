# Task 1



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
    counterOfString= counterOfString + 1
    if(len(expression) != (counterOfString )):
        global next_Token
        next_Token = expression[counterOfString]
    else:
        print('String is not complete')
        return
    


def A_NonTerminal():
    if(next_Token == 'a'):
        getNextToken()
        A_NonTerminal()
    elif(next_Token == 'b' and counterOfString == (len(expression) - 1)):
        print('Correct String!')
    else:
        displayError()
    



def StartState():
    if(next_Token == "_"):
        
        getNextToken()
        A_NonTerminal()  
    else:
        displayError()
    
    






if __name__ == "__main__":

    StartState() 


    