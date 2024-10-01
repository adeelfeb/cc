import re

# Define keywords and operators
keywords = {"if", "else", "while", "return", "int", "float"}
operators = {'+', '='}
punctuation = {',', ';'}

# Define regex patterns for lexical analysis
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
float_pattern = r'\d+\.\d+'
keyword_pattern = r'\b(?:' + '|'.join(keywords) + r')\b'
operator_pattern = r'[+=]'
punctuation_pattern = r'[;,]'

# Combined regex pattern for token matching
token_pattern = f'({float_pattern}|{keyword_pattern}|{identifier_pattern}|{operator_pattern}|{punctuation_pattern})'

def lexical_analyzer(input_string):
    tokens = []
    
    # Find all tokens using regex
    for match in re.finditer(token_pattern, input_string):
        token = match.group()
        if re.fullmatch(float_pattern, token):
            tokens.append(("FLOAT", token))
        elif token in keywords:
            tokens.append(("KEYWORD", token))
        elif re.fullmatch(identifier_pattern, token):
            tokens.append(("IDENTIFIER", token))
        elif token in operators:
            tokens.append(("OPERATOR", token))
        elif token in punctuation:
            tokens.append(("PUNCTUATION", token))
    
    return tokens

def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression

file_path = 'expression.txt'
input_string = read_expression_from_file(file_path)

# Check if the input_string is not empty before accessing its first character
if input_string:
    next_Token = input_string[0]
    print(f"Next Token: {next_Token}")
else:
    print("Input string is empty.")

tokens = lexical_analyzer(input_string)
for token in tokens:
    print(token)
