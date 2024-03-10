"""Test case for lexical analyzer."""
#Standard libary

# 3rd Party library
import pytest

# project library
from calculator.token import Token, TokenType
from calculator.lexer import Lexer


# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.NUMBER, "456"), 3),
        ("705", 1, Token(TokenType.NUMBER, "05"), 3),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_number(text, pos, expected_token, expected_pos):
    """Extract number from text starting at pos,."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_number(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("456", 0, Token(TokenType.ERROR, ""), 0),
        ("705", 1, Token(TokenType.ERROR, ""), 1),
        ("+", 0, Token(TokenType.ADD_OP, "+"), 1),
        ("+-", 1, Token(TokenType.ADD_OP, "-"), 2),
    ]
)
def test_get_add_op(text, pos, expected_token, expected_pos):
    """Extract an addition operator from text starting at pos,."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_add_op(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos

# -----------------------------------------------------------------------------
@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("*", 0, Token(TokenType.MUL_OP, "*"), 1),
        ("/", 0, Token(TokenType.MUL_OP, "/"), 1),
        ("%", 0, Token(TokenType.MUL_OP, "%"), 1),
        ("+", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_mul_op(text, pos, expected_token, expected_pos):
    """Extract a multiplication operator."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_mul_op(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("^", 0, Token(TokenType.POWER_OP, "^"), 1),
        ("*", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_power_op(text, pos, expected_token, expected_pos):
    """Extract a power operator."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_power_op(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("!", 0, Token(TokenType.FAC_OP, "!"), 1),
        ("*", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_fac_op(text, pos, expected_token, expected_pos):
    """Extract a factorial operator."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_fac_op(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        ("(", 0, Token(TokenType.LEFT_PAREN, "("), 1),
        ("*", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_left_paren(text, pos, expected_token, expected_pos):
    """Extract a left parenthesis."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_left_paren(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos


@pytest.mark.parametrize(
    "text, pos, expected_token, expected_pos",
    [
        (")", 0, Token(TokenType.RIGHT_PAREN, ")"), 1),
        ("*", 0, Token(TokenType.ERROR, ""), 0),
    ]
)
def test_get_right_paren(text, pos, expected_token, expected_pos):
    """Extract a right parenthesis."""
    # Arrange
    lexer = Lexer()

    # Act
    token, new_pos = lexer.get_right_paren(text, pos)

    # Assert
    assert token == expected_token
    assert new_pos == expected_pos

# -----------------------------------------------------------------------------
def test_skip_white_space():
    """Test skip_white_space() function."""
    assert Lexer().skip_white_space(" abc ", 0) == 1
    assert Lexer().skip_white_space(" xyz ", 0) == 1
    assert Lexer().skip_white_space(" xyz ", 1) == 1
    assert Lexer().skip_white_space(" xyz ", 2) == 2
    assert Lexer().skip_white_space(" xyz ", 3) == 3
    assert Lexer().skip_white_space(" xyz ", 4) == 5
    assert Lexer().skip_white_space(" xyz ", 5) == 5
    assert Lexer().skip_white_space("   pqr", 0) == 3


def test_get_token_list():
    """Test get_token_list() function."""
    lexer = Lexer()
    tokens = lexer.get_token_list("123 + (32 / 4)", 0)
    expected_tokens = [
        Token(TokenType.NUMBER, "123"),
        Token(TokenType.ADD_OP, "+"),
        Token(TokenType.LEFT_PAREN, "("),
        Token(TokenType.NUMBER, "32"),
        Token(TokenType.MUL_OP, "/"),
        Token(TokenType.NUMBER, "4"),
        Token(TokenType.RIGHT_PAREN, ")"),
    ]
    assert tokens == expected_tokens