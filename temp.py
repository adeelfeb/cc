def StartState(s):
    r=a(s)
    if(r==1):
        token=getNext_Token()
        if(token==-1):
            return 0
        r=b(token)
        return r
    else:
        return 0
     
def a(s):
    if(s=='_'):
        return 1
    elif(s.isalpha()):
        return 1
    else:
        return 0
         
def b(s):
    if(s=='_'):
        token=getNext_Token()
        if(token==-1):
            return 1
        r=b(token)
        return r
        
    elif(s.isalpha()):
        token=getNext_Token()
        if(token==-1):
            return 1
        r=b(token)
        return r
    elif(s.isdigit()):
        token=getNext_Token()
        if(token==-1):
            return 1
        r=b(token)
        return r
   # elif(" "):

    else:
        return 0
     
    
def getNext_Token():
    global i
    if(i<length):
        token=expression[i]
        i=i+1
        return token
    else:
        print("Complete")
        return -1





def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
        length = len(expression)  # Get the length of the expression
#        print(f"length{length}")
    return expression


i=0
file_path = 'expression.txt'
expression = read_expression_from_file(file_path)

length = len(expression)

token=getNext_Token()
re = StartState(token)


if(re==1):
    print("Valid String")
else:
    print("Invalid String!") 