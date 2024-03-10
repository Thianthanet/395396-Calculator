"""Token"""

#Standard libary
from collections import namedtuple
from enum import Enum

# 3rd Party library

# project library


# -----------------------------------------------------------------------------
TokenType = Enum(
    "TokenType",
    [
        "ERROR",
        "UNKNOWN",
        "EMPTY",
        "NUMBER",
        "FAC_OP",
        "POWER_OP",
        "MUL_OP",
        "ADD_OP",
        "LEFT_PAREN",
        "RIGHT_PAREN",
    ]
)


# -----------------------------------------------------------------------------
Token = namedtuple(
    "Token",
    [
        "token_type",
        "lexeme",
    ]
)