def StartState(s):
    returnValue =a(s)
    if(returnValue ==1):
        token=getNextToken()
        if(token==-1):
            return 0
        if(token=='.'):
            token=getNextToken()
            if(token==-1):
                return 0
            returnValue =a(token)
            return returnValue 
        else:
            return 0
    else:
        return 0
     
def a(s):
    global rep
    global counterString 
    if(s.isdigit()):
        token=getNextToken()
        if(token==-1):
            return 1
        returnValue =a(token)
        return returnValue 
    elif(s=='.'):
        if(rep==0):
            rep=1
            counterString =counterString -1
            return 1
        else:
            return 0
    else:
        return 0

            
def getNextToken():
    global counterString 
    if(counterString <length):
        token = expression[counterString]
        counterString =counterString +1
        return token
    else:
        return -1


def display_error():
    print("Error")


def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
        length = len(expression)  # Get the length of the expression
#        print(f"length{length}")
    return expression



counterString = 0
rep = 0


file_path = 'expression.txt'
expression = read_expression_from_file(file_path)
length = len(expression)


next_Token=getNextToken()

re = StartState(next_Token)



if(re==1):
    print("Valid String")
else:
    print("Invalid String") 