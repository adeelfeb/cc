# cc
```py
# class LR1Parser:
#     def __init__(self, parse_table, grammar):
#         self.parse_table = parse_table
#         self.grammar = grammar
#         self.stack = []
#         self.current_token = None
#         self.pos = 0

#     def next_token(self, tokens):
#         if self.pos < len(tokens):
#             self.current_token = tokens[self.pos]
#             self.pos += 1
#         else:
#             self.current_token = ('EOF', '$')

#     def parse(self, tokens):
#         self.stack = [0]
#         self.pos = 0
#         self.next_token(tokens)
        
#         while True:
#             state = self.stack[-1]
#             action = self.parse_table.get((state, self.current_token[0]))
            
#             if not action:
#                 raise Exception("Syntax error")
            
#             if action[0] == 's':  # shift
#                 self.stack.append(int(action[1:]))
#                 self.next_token(tokens)
#             elif action[0] == 'r':  # reduce
#                 rule = self.grammar[int(action[1:])]
#                 for _ in range(len(rule[1])):
#                     self.stack.pop()
#                 self.stack.append(self.parse_table[(self.stack[-1], rule[0])])
#             elif action == 'acc':  # accept
#                 return True

#     def run(self, tokens):
#         try:
#             if self.parse(tokens):
#                 return "Accepted"
#             else:
#                 return "Rejected"
#         except Exception as e:
#             return "Rejected"

# # Example usage:
# parse_table = {  # Sample parse table
#     (0, 'a'): 's1', (0, 'b'): 's2',
#     (1, 'a'): 'r1', (1, 'b'): 's3',
#     (2, 'b'): 'r2', (3, 'a'): 'acc',
# }
# grammar = [  # Sample grammar rules
#     ('S', ['a']),
#     ('S', ['b']),
# ]
# tokens = [('a', 'b'), ('b', 'b')]  # Sample tokens
# parser = LR1Parser(parse_table, grammar)
# result = parser.run(tokens)
# print(result)



# class LR1Parser:
#     def __init__(self, parse_table, grammar):
#         self.parse_table = parse_table
#         self.grammar = grammar
#         self.stack = []
#         self.current_token = None
#         self.pos = 0

#     def next_token(self, tokens):
#         if self.pos < len(tokens):
#             self.current_token = tokens[self.pos]
#             self.pos += 1
#         else:
#             self.current_token = '$'  # End of input, use '$' as EOF

#     def parse(self, tokens):
#         self.stack = [0]
#         self.pos = 0
#         self.next_token(tokens)
        
#         while True:
#             state = self.stack[-1]
#             print(f"State: {state}, Current Token: {self.current_token}")  # Debugging line
#             action = self.parse_table.get((state, self.current_token))
            
#             if not action:
#                 print(f"No action found for state {state} and token {self.current_token}")  # Debugging line
#                 raise Exception("Syntax error")
            
#             print(f"Action: {action}")  # Debugging line

#             if action[0] == 's':  # shift
#                 self.stack.append(int(action[1:]))
#                 self.next_token(tokens)
#             elif action[0] == 'r':  # reduce
#                 rule = self.grammar[int(action[1:]) - 1]  # Fixing index: action[1:] gives r1, r2, so subtract 1
#                 print(f"Reducing with rule: {rule}")  # Debugging line
#                 for _ in range(len(rule[1])):
#                     self.stack.pop()
#                 self.stack.append(self.parse_table[(self.stack[-1], rule[0])])
#             elif action == 'acc':  # accept
#                 return True

#     def run(self, tokens):
#         try:
#             if self.parse(tokens):
#                 return "Accepted"
#             else:
#                 return "Rejected"
#         except Exception:
#             return "Some Exception :)"

# def tokenize(input_string):
#     # Only return a list of characters, no tuples
#     return [char for char in input_string]

# parse_table = {  # Updated parse table
#     (0, 'b'): 's5', (0, 'd'): 's10',
#     (0, 'S'): '1', (0, 'A'): '3',
#     (1, '$'): 'acc',
#     (2, '$'): 'acc',
#     (3, 'a'): 's4',
#     (4, '$'): 'r1',
#     (5, 'd'): 's8', (5, 'A'): '6',
#     (6, 'c'): 's7',
#     (7, '$'): 'r2',
#     (8, 'a'): 's9',
#     (8, 'c'): 'r5',
#     (9, '$'): 'r4',
#     (10, 'a'): 'r5',
#     (10, 'c'): 's11',
#     (11, '$'): 'r3',
# }
# grammar = [  # Updated grammar rules
#     ('S', ['Aa']),
#     ('S', ['bAc']),
#     ('S', ['dc']),
#     ('S', ['bda']),
#     ('A', ['a']),
# ]

# parser = LR1Parser(parse_table, grammar)

# while True:
#     input_string = input("Enter a string (or type 'exit' to quit): ")
#     if input_string.lower() == 'exit':
#         print("Goodbye!")
#         break
#     tokens = tokenize(input_string)
#     result = parser.run(tokens)
#     print(result)












class LR1Parser:
    def __init__(self, parse_table, grammar):
        self.parse_table = parse_table
        self.grammar = grammar
        self.stack = []
        self.current_token = None
        self.pos = 0

    def next_token(self, tokens):
        if self.pos < len(tokens):
            self.current_token = tokens[self.pos]
            self.pos += 1
        else:
            self.current_token = '$'  # End of input, use '$' as EOF

    def parse(self, tokens):
        self.stack = [0]
        self.pos = 0
        self.next_token(tokens)
        
        while True:
            state = self.stack[-1]
            print(f"State: {state}, Current Token: {self.current_token}")  # Debugging line
            action = self.parse_table.get((state, self.current_token))
            
            if not action:
                print(f"No action found for state {state} and token {self.current_token}")  # Debugging line
                raise Exception("Syntax error")
            
            print(f"Action: {action}")  # Debugging line

            if action[0] == 's':  # shift
                self.stack.append(int(action[1:]))
                self.next_token(tokens)
            elif action[0] == 'r':  # reduce
                rule = self.grammar[int(action[1:]) - 1]  # Fixing index: action[1:] gives r1, r2, so subtract 1
                print(f"Reducing with rule: {rule}")  # Debugging line
                for _ in range(len(rule[1])):
                    self.stack.pop()
                # Now, the top of the stack should have the state to transition to after reduction.
                # Push the new state determined by the left-hand side of the rule.
                self.stack.append(self.parse_table[(self.stack[-1], rule[0])])
            elif action == 'acc':  # accept
                return True

    def run(self, tokens):
        try:
            if self.parse(tokens):
                return "Accepted"
            else:
                return "Rejected"
        except Exception:
            return "End of parser :)"

def tokenize(input_string):
    # Only return a list of characters, no tuples
    return [char for char in input_string]

# Updated parse table to fix issues:
parse_table = {  
    (0, 'b'): 's5', (0, 'a'): 's4', (0, 'd'): 's10',  # Handle 'a' shift from state 0
    (0, 'S'): '1', (0, 'A'): '3', 
    
    (1, '$'): 'acc',
    (2, '$'): 'acc',
    (3, 'a'): 's4',
    (4, '$'): 'r1',
    
    (5, 'd'): 's8', (5, 'A'): '6',
    (6, 'c'): 's7',
    (7, '$'): 'r2',
    
    (8, 'a'): 's9',
    (8, 'c'): 'r5',
    
    (9, '$'): 'r4',
    
    (10, 'a'): 'r5',
    (10, 'c'): 's11',
    
    (11, '$'): 'r3',
}

# Updated grammar rules
grammar = [
    ('S', ['Aa']),
    ('S', ['bAc']),
    ('S', ['dc']),
    ('S', ['bda']),
    ('A', ['a']),
]

parser = LR1Parser(parse_table, grammar)

while True:
    input_string = input("Enter a string (or type 'exit' to quit): ")
    if input_string.lower() == 'exit':
        print("Goodbye!")
        break
    tokens = tokenize(input_string)
    result = parser.run(tokens)
    print(result)

```


```
%{
#include <stdio.h>
int operators_count = 0, integers_count = 0; // Counters for operators and integers
%}

%%

"+"|"-"|"*"|"/" {
    operators_count++;
    printf("Operator: %s\n", yytext); // Print the operator
}

[0-9]+ {
    integers_count++;
    printf("Integer: %s\n", yytext); // Print the integer
}

[ \t\n] ; // Ignore whitespace and newlines

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter an arithmetic expression: ");
    yylex(); // Call the lexer

    printf("\nTotal Operators: %d\n", operators_count);
    printf("Total Integers: %d\n", integers_count);

    return 0;
} ```

### The Global Variable declaration in Python

` Write Global before the variabkle inside the function in which it is being called`

getting started

# write apython code for a simpele task that will read a .txt file from it an expression and convert it into postfix 


```



```
%{
    #include <stdio.h>
%}

%%

"+"|"-"|"*"|"/" { printf("Operator: %s\n", yytext); }

[0-9]+ { printf("Integer: %s\n", yytext); }

[ \t]+   ; 

"//".*    ; 

[ \n]     ; 

%%

int yywrap() {
    return 1;
}

int main() {
    printf("Enter an arithmetic expression: ");
    yylex(); 
    return 0;
}
```

```
Website Urls: https://gnuwin32.sourceforge.net/packages.html, https://sourceforge.net/projects/mingw/
Bison:  https://gnuwin32.sourceforge.net/downlinks/bison.php
Flex: https://gnuwin32.sourceforge.net/downlinks/flex.php
```

```
[10/9, 6:59 AM] Adeel: https://youtu.be/NzPB2eiiYDA?feature=shared
[10/9, 6:59 AM] Adeel: Agr nahi install 
https://youtu.be/Mmy7y8a-WdA?feature=shared
```

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = stack.pop()
        else:
            while (stack) and (precedence[stack[-1]] >= precedence[char]):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ' '.join(postfix)



def evaluate_postfix(expression):
    stack = []

    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    return stack.pop()



def read_expression_from_file(file_path):
    with open(file_path, 'r') as file:
        expression = file.read().strip()
    return expression





file_path = 'expression.txt'
infix_expression = read_expression_from_file(file_path)
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {postfix_expression}")
result = evaluate_postfix(postfix_expression)
print(f"The result of the postfix expression '{postfix_expression}' is: {result}")


```


# For second Lab the task begin like this somehow 

```python



class SimpleCompiler:
    def __init__(self):
        # Initialize state variables
        self.current_state = 'START'
        self.last_state = None

        # Define token types and their expected syntax patterns
        self.token_table = {
            'keyword': ['int', 'float', 'return', 'if', 'else', 'for', 'while'],
            'identifier': r'[a-zA-Z_]\w*',
            'number': r'\d+(\.\d+)?',
            'operator': ['+', '-', '*', '/', '=', '==', '!=', '<', '>'],
            'delimiter': [';', '{', '}', '(', ')']
        }

    def check_token(self, token):
        """Check if the token is valid based on the token table."""
        if token in self.token_table['keyword']:
            return 'keyword'
        elif token in self.token_table['operator']:
            return 'operator'
        elif token in self.token_table['delimiter']:
            return 'delimiter'
        elif re.fullmatch(self.token_table['identifier'], token):
            return 'identifier'
        elif re.fullmatch(self.token_table['number'], token):
            return 'number'
        else:
            return 'unknown'

    def process_line(self, line):
        """Process a line of C++ code to check token validity and state transitions."""
        tokens = line.split()
        for token in tokens:
            token_type = self.check_token(token)
            print(f"Token: {token}, Type: {token_type}")

            # State management
            self.last_state = self.current_state
            self.current_state = self.determine_next_state(token_type)
            print(f"Transitioned from {self.last_state} to {self.current_state}")

    def determine_next_state(self, token_type):
        """Determine the next state based on the current token type."""
        state_transition = {
            'START': {
                'keyword': 'IN_KEYWORD',
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_KEYWORD': {
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_IDENTIFIER': {
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_NUMBER': {
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_OPERATOR': {
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_DELIMITER': {
                'keyword': 'IN_KEYWORD',
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'ERROR': {}
        }

        return state_transition.get(self.current_state, {}).get(token_type, 'ERROR')

import re




if __name__ == "__main__":
    compiler = SimpleCompiler()

    # Example usage with a file
    file_path = 'expression.txt'  # Replace with your actual file path

    try:
        with open(file_path, 'r') as file:
            for line in file:
                compiler.process_line(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

```


# Code that is for temporary work staging
```python
import re

class SimpleCompiler:
    def __init__(self):
        # Initialize state variables
        self.current_state = 'START'
        self.last_state = None

        # Define token types and their expected syntax patterns
        self.token_table = {
            'keyword': ['int', 'float', 'return', 'if', 'else', 'for', 'while'],
            'identifier': r'[a-zA-Z_]\w*',
            'number': r'\d+(\.\d+)?',
            'operator': ['+', '-', '*', '/', '=', '==', '!=', '<', '>'],
            'delimiter': [';', '{', '}', '(', ')']
        }
        self.token_pattern = re.compile(
            r'\b(?:' + '|'.join(re.escape(op) for op in self.token_table['operator']) + r')\b|'  # operators
            r'\b(?:' + '|'.join(re.escape(delim) for delim in self.token_table['delimiter']) + r')\b|'  # delimiters
            r'\b(?:' + '|'.join(re.escape(kw) for kw in self.token_table['keyword']) + r')\b|'  # keywords
            r'\b[a-zA-Z_]\w*\b|'  # identifiers
            r'\b\d+(\.\d+)?\b'  # numbers
        )
    
    def get_state_for_char(self, line):
        """Get state transitions for each character in a line of code."""
        states = []
        i = 0
        while i < len(line):
            char = line[i]

            if char.isspace():
                i += 1
                continue

            # Determine the token for the substring starting from current position
            match = self.token_pattern.match(line, i)
            if match:
                token = match.group(0)
                token_type = self.check_token(token)
                states.append((token, token_type, self.current_state))

                # State management
                self.last_state = self.current_state
                self.current_state = self.determine_next_state(token_type)
                states.append((f"Transitioned from {self.last_state} to {self.current_state}"))

                i += len(token)
            else:
                states.append((char, 'unknown', self.current_state))
                i += 1

        return states

    def check_token(self, token):
        """Check if the token is valid based on the token table."""
        if token in self.token_table['keyword']:
            return 'keyword'
        elif token in self.token_table['operator']:
            return 'operator'
        elif token in self.token_table['delimiter']:
            return 'delimiter'
        elif re.fullmatch(self.token_table['identifier'], token):
            return 'identifier'
        elif re.fullmatch(self.token_table['number'], token):
            return 'number'
        else:
            return 'unknown'

    def determine_next_state(self, token_type):
        """Determine the next state based on the current token type."""
        state_transition = {
            'START': {
                'keyword': 'IN_KEYWORD',
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_KEYWORD': {
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_IDENTIFIER': {
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_NUMBER': {
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_OPERATOR': {
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'IN_DELIMITER': {
                'keyword': 'IN_KEYWORD',
                'identifier': 'IN_IDENTIFIER',
                'number': 'IN_NUMBER',
                'operator': 'IN_OPERATOR',
                'delimiter': 'IN_DELIMITER',
                'unknown': 'ERROR'
            },
            'ERROR': {}
        }

        return state_transition.get(self.current_state, {}).get(token_type, 'ERROR')

if __name__ == "__main__":
    compiler = SimpleCompiler()

    # Example usage
    line = 'int main() { return 0; }'
    states = compiler.get_state_for_char(line)

    for state in states:
        print(state)


```
