
import re

keywords = ['int', 'float', 'double', 'for', 'if', 'else']

def getState(currentState, currentChar):
    if currentState == 0:
        if currentChar.isalpha() or currentChar == '_':  # Letter or underscore
            return 1
        elif currentChar == ',':
            return 2
        elif currentChar == ';':
            return 3
        elif currentChar == '=':
            return 4
        elif currentChar.isdigit():
            return 6
        elif currentChar in [' ', '\t', '\n']:  # Whitespace
            return 0
        else:
            return -1

    elif currentState == 1:
        if currentChar.isalpha() or currentChar.isdigit() or currentChar == '_':  # Letter, digit or underscore
            return 1
        else:
            return -1

    elif currentState == 2 or currentState == 3:
        return -1  # No path from state 2 or 3

    elif currentState == 4:
        if currentChar == '=':
            return 5  # Equals operator ==
        else:
            return -1

    elif currentState == 5:
        return -1  # No path from state 5

    elif currentState == 6:
        if currentChar.isdigit():
            return 6  # Building integer constant
        elif currentChar == '.':
            return 7  # Starting real number
        else:
            return -1

    elif currentState == 7:
        if currentChar.isdigit():
            return 8  # Building real number
        else:
            return -1

    elif currentState == 8:
        if currentChar.isdigit():
            return 8  # Building real number
        else:
            return -1

    return -1  # No valid state transition

# Function to classify the token based on the final state
def classify_token(state, lexeme):
    if state == 1:
        if lexeme in keywords:
            return f'Keyword: {lexeme}'
        else:
            return f'Identifier: {lexeme}'
    elif state == 2:
        return 'Punctuation: ,'
    elif state == 3:
        return 'Punctuation: ;'
    elif state == 4:
        return 'Operator: = (Assignment)'
    elif state == 5:
        return 'Operator: == (Equality)'
    elif state == 6:
        return f'Constant int: {lexeme}'
    elif state == 8:
        return f'Constant real: {lexeme}'
    else:
        return 'Unknown token'

# Main lexical analyzer function
def lexical_analyzer(input_file):
    with open(input_file, 'r') as file:
        content = file.read()

    F = 0  # Forward pointer
    LS = 0  # Lexeme start
    LineNo = 1  # Line number
    CS = 0  # Current state
    LFSV = -1  # Last final state visited
    IWLFSV = -1  # Index where the last final state was visited
    
    tokens = []  # List to hold the tokens

    while F < len(content):
        char = content[F]

        # Track line number
        if char == '\n':
            LineNo += 1

        next_state = getState(CS, char)

        if next_state == -1:  # Invalid state transition
            if CS in [1, 2, 3, 4, 5, 6, 8]:  # Final states
                lexeme = content[LS:F]
                tokens.append((LineNo, classify_token(CS, lexeme)))
                LS = F  # Move Lexeme Start
                CS = 0  # Reset current state
            else:
                print(f"Error at line {LineNo}: Invalid token '{content[LS:F]}'")
                LS = F  # Move Lexeme Start
                CS = 0  # Reset current state
        else:
            CS = next_state  # Move to the next state
            if CS in [1, 2, 3, 4, 5, 6, 8]:  # Final states
                LFSV = CS
                IWLFSV = F

        F += 1

    # Handle the last lexeme
    if LS < len(content):
        lexeme = content[LS:F]
        if CS in [1, 2, 3, 4, 5, 6, 8]:
            tokens.append((LineNo, classify_token(CS, lexeme)))
        else:
            print(f"Error at line {LineNo}: Invalid token '{lexeme}'")

    # Return the list of tokens
    return tokens

# Example usage
input_file = 'expresssion.txt'  # Replace with the path to your input file
tokens = lexical_analyzer(input_file)

# Print the tokens
for line_no, token in tokens:
    print(f"Line {line_no}: {token}")