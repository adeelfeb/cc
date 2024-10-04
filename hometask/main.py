keywords = ['float', 'int', 'double']
final_State = [1, 2, 3, 4, 5, 6, 8]

file_name = "code.txt"
with open(file_name, 'r') as file:
    content = file.read()

CS = 0  # Current State
LS = 0  # Lexeme Start
LFSV = -1  # Last Final State Visited
IWLFS = -1  # Index When Last Final State was Visited
tokens = []  # List to store tokens


def getNextState(currentState, char):
    if currentState == 0:
        if char == '_' or char.isalpha():
            return 1  # Identifier or keyword
        elif char == ',':
            return 2  # Comma
        elif char == ';':
            return 3  # Semicolon
        elif char == '=':
            return 4  # Single equal sign
        elif char.isdigit():
            return 6  # Integer constant
        elif char == " " or char == "\t" or char == "\n":
            return 0  # Ignore whitespace
    elif currentState == 1:
        if char == '_' or char.isalpha() or char.isdigit():
            return 1  # Continue identifier/keyword
        else:
            return -1  # Invalid state for identifier
    elif currentState == 2 or currentState == 3 or currentState == 5:
        return -1  # Comma, semicolon, or == cannot be followed by anything
    elif currentState == 4:
        if char == '=':
            return 5  # Double equal (==)
        else:
            return -1  # Invalid state for operator
    elif currentState == 6:
        if char.isdigit():
            return 6  # Continue integer constant
        elif char == ".":
            return 7  # Decimal point for floating-point number
        else:
            return -1  # Invalid state for integer
    elif currentState == 7:
        if char.isdigit():
            return 8  # Floating-point constant
        elif char == '.':
            return -1  # Error: consecutive dots
        else:
            return -1  # Invalid state for decimal number
    elif currentState == 8:
        if char.isdigit():
            return 8  # Continue floating-point constant
        else:
            return -1  # Invalid state for floating-point number

    return -1  # Invalid character or state


def makeString():
    return ''.join(content[LS:IWLFS + 1])


def assignLabel(st):
    if LFSV == 1 and st in keywords:
        return "KEYWORD"
    elif LFSV == 1:
        return "IDENTIFIER"
    elif LFSV in [2, 3]:
        return "PUNCTUATION"
    elif LFSV in [4, 5]:
        return "OPERATOR"
    elif LFSV in [6, 8]:
        return "CONSTANT"
    else:
        return "ERROR"


for index, char in enumerate(content):
    if char == ' ' or char == '\n' or char == '\t':  # Skip whitespace
        continue

    prevCS = CS  # Store the previous state for error handling
    CS = getNextState(CS, char)

    if CS < 0:  # If current state is invalid
        if prevCS != 0:  # Check if we have a valid token before the error
            st = makeString()
            label = assignLabel(st)
            tokens.append(f'<{st}, {label}>')

        if char != ' ' and char != '\n':  # Ignore spaces and newlines in errors
            tokens.append(f'<{char}, ERROR>')  # Mark the error token

        # Reset state after error
        CS = 0
        LFSV = -1
        IWLFS = -1
        LS = index + 1  # Move to the next character for lexeme start
    else:
        if CS in final_State:
            LFSV = CS  # Update last final state visited
            IWLFS = index  # Update index when last final state was visited

# Add final token if there's a valid one at the end of the content
if LFSV != -1:
    st = makeString()
    label = assignLabel(st)
    tokens.append(f'<{st}, {label}>')

# Output the list of tokens
print(tokens)
