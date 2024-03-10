"""A simple lexical analyzer."""

# Standard libary

# 3rd Party library

# project library
from calculator.token import Token, TokenType


# -----------------------------------------------------------------------------
class Lexer:
    """A simple lexical analyzer."""

    def get_number(self, text, pos):
        """Extract number from text starting at pos.

        Args:
            text(str): Text to be scanned.
            pos(int): The starting position to scan.

        Returns:
            token: The extracted token
            pos: The position after the scanning.

        Grammar:
            Number = Digit { Digit }
            Digit = "0" | ... | "9"
        """
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if not text[pos].isdigit():
            return Token(TokenType.ERROR, lexeme), pos

        while pos < length and text[pos].isdigit():
            lexeme = lexeme + text[pos]
            pos = pos + 1

        return Token(TokenType.NUMBER, lexeme), pos

    def get_add_op(self, text, pos):
        """Extract an addition operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == "+":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        elif text[pos] == "-":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.ADD_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

# -----------------------------------------------------------------------------
    def get_mul_op(self, text, pos):
        """Extract a multiplication operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == "*":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "/":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        elif text[pos] == "%":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.MUL_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_power_op(self, text, pos):
        """Extract a power operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == "^":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.POWER_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_fac_op(self, text, pos):
        """Extract a factorial operator."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == "!":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.FAC_OP, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_left_paren(self, text, pos):
        """Extract a left parenthesis."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == "(":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.LEFT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

    def get_right_paren(self, text, pos):
        """Extract a right parenthesis."""
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        if text[pos] == ")":
            lexeme = text[pos]
            pos = pos + 1
            return Token(TokenType.RIGHT_PAREN, lexeme), pos
        else:
            return Token(TokenType.ERROR, lexeme), pos

# -----------------------------------------------------------------------------
    def get_token(self, text, pos):
        """Extract a token from text starting at pos."""
        self.skip_white_space(text, pos)
        lexeme = ""
        length = len(text)
        if pos >= length:
            return Token(TokenType.EMPTY, lexeme), pos

        current_char = text[pos]
        if current_char.isdigit():
            return self.get_number(text, pos)
        elif current_char in "+-":
            return self.get_add_op(text, pos)
        elif current_char in "*/%":
            return self.get_mul_op(text, pos)
        elif current_char == "^":
            return self.get_power_op(text, pos)
        elif current_char == "!":
            return self.get_fac_op(text, pos)
        elif current_char == "(":
            return self.get_left_paren(text, pos)
        elif current_char == ")":
            return self.get_right_paren(text, pos)
        else:
            return Token(TokenType.ERROR, ""), pos + 1

    def skip_white_space(self, text, pos):
        """Skip all white spaces."""
        length = len(text)
        while pos < length and text[pos].isspace():
            pos += 1
        return pos
    
    def get_token_list(self, text, pos):
        """Extract all tokens from the text."""
        tokens = []
        while pos < len(text):
            token, pos = self.get_token(text, pos)
            tokens.append(token)
        return tokens

