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
