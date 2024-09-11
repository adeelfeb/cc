


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
