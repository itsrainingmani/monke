from dataclasses import dataclass

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

# Type Alias
tokentype = str


@dataclass
class Token:
    type: tokentype
    literal: str