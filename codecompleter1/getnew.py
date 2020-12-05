tokens = (
    'COMPARE','CONST','SUM','SUB','QUO','MUL','MOD','MINUS','PRINT','SCAN','OTHERS'
)
def t_COMPARE(t):
    r'comparing|compare|compared|compared\sto|compared\swith|check|where'
    return t
def t_CONST(t):
    r'constant'
    return t
def t_SUM(t):
    r'add|plus|sum'
    return t
def t_SUB(t):
    r'subtract|difference'
    return t
def t_QUO(t):
    r'quotient|divide'
    return t
def t_MUL(t):
    r'multiply|product'
    return t
def t_MOD(t):
    r'mod|remainder'
    return t
def t_MINUS(t):
    r'minus|negation|negative'
    return t
def t_PRINT(t):
    r'print|printf|display|output'
    return t
def t_SCAN(t):
    r'scan|input|read|get'
    return  t
def t_OTHERS(t):
    r'.'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
import ply.lex as lex
lex.lex()

def inputfunction(s1):
    lex.input(s1)
    for tok in iter(lex.token, None):
        if(tok.type==tokens[0]):
            print("compare.py")
            break
        if (tok.type == tokens[1]):
            print("const.py")
            break
        if (tok.type == tokens[2]):
            print("sum.py")
            break
        if (tok.type == tokens[3]):
            print("difference.py")
            break
        if (tok.type == tokens[4]):
            print("quotient.py")
            break
        if (tok.type == tokens[5]):
            print("multiply.py")
            break
        if (tok.type == tokens[6]):
            print("mod.py")
            break
        if (tok.type == tokens[7]):
            print("minus.py")
            break
        if (tok.type == tokens[8]):
            print("print.py")
            break
        if (tok.type == tokens[9]):
            print("scan.py")
            break
s = input()
s.encode('UTF-8')
inputfunction(s)