from dataclasses import dataclass
from typing import NewType

# Type Alias
tokentype = NewType("tokentype", str)

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT"  # add, foobar, x, y
INT = "INT"

# Operators
ASSIGN = "="
PLUS = "+"

# Delimiters
COMMA = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"

keywords = {"fn": FUNCTION, "let": LET}


def lookup_ident(ident: str) -> tokentype:
    if ident in keywords:
        return keywords[ident]
    else:
        return IDENT


@dataclass
class Token:
    type: tokentype
    literal: str


def new_token(tt: tokentype, ch: str) -> Token:
    return Token(type=tt, literal=ch)