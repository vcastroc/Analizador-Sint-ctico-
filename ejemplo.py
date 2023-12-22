import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'ID', 'NUM', 'SEMI', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'NEQ', 'LT', 'LE', 'GT', 'GE', 'NOT', 'AND', 'OR', 'REAL',
    'LPAREN', 'RPAREN', 'TRUE', 'FALSE', 'IF', 'ELSE', 'WHILE', 'DO', 'BREAK', 'BASICO',
)

# Expresiones regulares para los tokens simples

def t_LBRACE(t):
    r'\{'
    print(f"Izq.LLAVE")
    return t

def t_RBRACE(t):
    r'\}'
    print(f"Der.LLAVE")
    return t

def t_LBRACKET(t):
    r'\['
    print(f"Izq.CORCHETE")
    return t

def t_RBRACKET(t):
    r'\]'
    print(f"Der.CORCHETE")
    return t

def t_SEMI(t):
    r';'
    print(f"PUNTO_y_COMA")
    return t

def t_PLUS(t):
    r'\+'
    print(f"Oper.SUMA")
    return t

def t_MINUS(t):
    r'-'
    print(f"Oper.RESTA")
    return t

def t_TIMES(t):
    r'\*'
    print(f"Oper.MULTIPLICAR")
    return t

def t_DIVIDE(t):
    r'/'
    print(f"Oper.DIVISION")
    return t

def t_EQUALS(t):
    r'='
    print(f"ASIGNACIONIGUAL: =")
    return t

def t_NEQ(t):
    r'!='
    print(f"OPREL: !=")
    return t

def t_LT(t):
    r'<'
    print(f"OPREL: <")
    return t

def t_LE(t):
    r'<='
    print(f"OPREL: <=")
    return t

def t_GT(t):
    r'>'
    print(f"OPREL: >")
    return t

def t_GE (t):
    r'>='
    print(f"OPREL: >=")
    return t

def t_NOT(t):
    r'!'
    print(f"OPBOOL: NOT")
    return t

def t_AND(t):
    r'&&'
    print(f"OPBOOL: AND")
    return t

def t_OR(t):
    r'\|\|'
    print(f"OPBOOL: OR")
    return t

def t_LPAREN(t):
    r'\('
    print(f"Izq.PARENTESIS")
    return t

def t_RPAREN(t):
    r'\)'
    print(f"Der.PARENTESIS")
    return t

def t_TRUE(t):
    r'true'
    print(f"TRUE")
    return t

def t_FALSE(t):
    r'false'
    print(f"FALSE")
    return t

def t_IF(t):
    r'if'
    print(f"IF")
    return t

def t_ELSE(t):
    r'else'
    print(f"ELSE")
    return t

def t_WHILE(t):
    r'while'
    print(f"WHILE")
    return t

def t_DO(t):
    r'do'
    print(f"DO")
    return t

def t_BREAK(t):
    r'break'
    print(f"BREAK")
    return t

def t_REAL(t):
    r'\d*\.\d+|\d+\.\d*'
    print(f"REAL: {t.value}")
    return t

def t_BASICO(t):
    r'do|while|int|float|for'
    print(f"TIPO: {t.value}")
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    print(f"ID: {t.value}")
    return t

def t_NUM(t):
    r'\d+'
    print(f"NUMERO: {t.value}")
    return t


# Ignorar espacios y tabuladores
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Reglas de la gramática
def p_programa(p):
    'programa : bloque'
    print("Programa válido")

def p_bloque(p):
    'bloque : LBRACE decls instrs RBRACE'

def p_decls(p):
    'decls : decls decl'
    

def p_decls_empty(p):
    'decls :'
    pass

def p_decl(p):
    'decl : tipo ID SEMI'
    

def p_tipo(p):
    '''tipo : BASICO
        | tipo LBRACKET NUM RBRACKET'''
    

def p_instrs(p):
    'instrs : instrs instr'
    

def p_instrs_empty(p):
    'instrs :'
    pass

def p_instr(p):
    '''instr : loc EQUALS bool SEMI
            | IF LPAREN bool RPAREN instr
            | IF LPAREN bool RPAREN instr ELSE instr
            | WHILE LPAREN bool RPAREN instr
            | DO instr WHILE LPAREN bool RPAREN SEMI
            | BREAK SEMI
            | bloque'''
    

def p_loc(p):
    '''loc : loc LBRACKET bool RBRACKET
        | ID'''
    

def p_bool(p):
    '''bool : bool OR comb
            | comb'''
            

def p_comb(p):
    '''comb : comb AND igualdad
            | igualdad'''

def p_igualdad(p):
    '''igualdad : igualdad EQUALS rel
                | igualdad NEQ rel
                | rel'''

def p_rel(p):
    '''rel : expr LT expr
        | expr LE expr
        | expr GE expr
        | expr GT expr
        | expr'''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term'''

def p_term(p):
    '''term : term TIMES unario
            | term DIVIDE unario
            | unario'''

def p_unario(p):
    '''unario : NOT unario
            | MINUS unario
            | factor'''

def p_factor(p):
    '''factor : LPAREN bool RPAREN
            | loc
            | NUM
            | REAL
            | TRUE
            | FALSE'''

def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.type}', valor '{p.value}'")
    else:
        print("Error de sintaxis en EOF")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Código de entrada
codigo = '''
{
int x;
float y;
x = 5;
y = 3.14;
if (x > 0){
      y = y * x;
}
}
'''

# Parseo del código
parser.parse(codigo, lexer=lexer)

