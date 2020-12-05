tokens = (
    'POSTINCREMENT','PREINCREMENT','VAR',
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_POSTINCREMENT(t):
    r'post\sincrement|increment'
    return t
def t_PREINCREMENT(t):
    r'pre\sincrement'
    return t
def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


def t_skip(t):
    r'.'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules



# dictionary of names
#names = {}

def p_statement_rule1(p):
    'statement : POSTINCREMENT VAR'
    print(str(p[2])+"++")
def p_statement_rule2(p):
    'statement : PREINCREMENT VAR'
    print("++"+str(p[2]))

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def infun(s1):
    yacc.parse(s1)
def getVar():
    f = open("E:\\codecompleter1\\SymbolTable.txt", "r")
    a = f.read()
    f.close()
    fl = 0
    v = ""
    for j in range(ord('a'), ord('z') + 1):
        for i in range(0, 10):
            if chr(j) + str(i) not in a:

                v = chr(j) + str(i)

                fl = 1
                break
        if fl == 1:
            break
    return v
s = input()
#print(s)
s.encode('UTF-8')
#print(s)
infun(s)
