from monke import lexer, token


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
        # print(tok, t)
        assert tok == t


def test_next_token1():
    input = """let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);"""

    expected = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    l = lexer.new(input)

    for t in expected:
        tok = l.next_token()
        # print(tok, t)
        assert tok == t


def test_next_token_extended():
    input = """let five = 5;
let ten = 10;

let add = fn(x, y) {
  x + y;
};

let result = add(five, ten);
!-/*5;
5 < 10 > 5;
"""

    expected = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.BANG, "!"),
        token.Token(token.MINUS, "-"),
        token.Token(token.SLASH, "/"),
        token.Token(token.ASTERISK, "*"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.GT, ">"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    l = lexer.new(input)

    for t in expected:
        tok = l.next_token()
        # print(tok, t)
        assert tok == t


def test_new_keywords():
    input = """
if (5 < 10) {
    return true;
} else {
    return false;
}
"""

    expected = [
        token.Token(token.IF, "if"),
        token.Token(token.LPAREN, "("),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.TRUE, "true"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.ELSE, "else"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.FALSE, "false"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.EOF, ""),
    ]

    l = lexer.new(input)

    for t in expected:
        tok = l.next_token()
        # print(tok, t)
        assert tok == t


def test_doublechar_ops():
    input = """
10 == 10;
10 != 9;
"""

    expected = [
        token.Token(token.INT, "10"),
        token.Token(token.EQ, "=="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.INT, "10"),
        token.Token(token.NOT_EQ, "!="),
        token.Token(token.INT, "9"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    l = lexer.new(input)

    for t in expected:
        tok = l.next_token()
        # print(tok, t)
        assert tok == t