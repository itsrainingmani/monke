from monke import lexer, token
import monke


def test_next_token():
    input = "=+(){},;"

    expected = [
        token.Token(token.ASSIGN, "="),
        token.Token(token.PLUS, "+"),
        token.Token(token.LPAREN, "("),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.COMMA, ","),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    l = lexer.new(input)

    for t in expected:
        tok = l.next_token()

        assert tok == t
