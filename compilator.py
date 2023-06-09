import sys

reserved_words = ['PRINT', 'WHILE', 'IF', 'ENDIF', 'ENDWHILE', 'ENDFUNCTION', 'ELSE', 'THEN', 'FUNCTION', 'RETURN', 'AS', 'INTEGER', 'STRING', 'DO', 'DECLARE']

class Token:
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

class PrePro:
    @staticmethod
    def filter(source):
        if '#' not in source:
            return source
        lines = source.split('\n')
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    lines[i] = lines[i][:j]
                    break
        return '\n'.join(lines)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def Evaluate(symboltable):
        pass 

class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        if self.value == '-':
            return ["INTEGER", - self.children[0].Evaluate(symboltable)[1]]
        if self.value == '!':
            return ["INTEGER", not self.children[0].Evaluate(symboltable)[1]]
        return ["INTEGER", self.children[0].Evaluate(symboltable)[1]]

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        esq_op = self.children[0].Evaluate(symboltable)
        dir_op = self.children[1].Evaluate(symboltable)
        if esq_op[0] == "String" or dir_op[0] == "String":
            if self.value == '<>':
                if esq_op[1] != dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]       
            elif self.value == '==':
                if esq_op[1] == dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]     
            elif self.value == '<':
                if esq_op[1] < dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '>':
                if esq_op[1] > dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '<=':
                if esq_op[1] <= dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '>=':
                if esq_op[1] >= dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == 'AND':
                if esq_op[1] and dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == 'OR':
                if esq_op[1] or dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
        else:
            if self.value == '+':
                return ["INTEGER", esq_op[1] + dir_op[1]]
            elif self.value == '-':
                return ["INTEGER", esq_op[1] - dir_op[1]]
            elif self.value == '<>':
                if esq_op[1] != dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]       
            elif self.value == '==':
                if esq_op[1] == dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]     
            elif self.value == '<':
                if esq_op[1] < dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '>':
                if esq_op[1] > dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '<=':
                if esq_op[1] <= dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == '>=':
                if esq_op[1] >= dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == 'AND':
                if esq_op[1] and dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
            elif self.value == 'OR':
                if esq_op[1] or dir_op[1]:
                    return ["INTEGER", 1]
                else:
                    return ["INTEGER", 0]
        
class IntVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symboltable):
        return ["INTEGER", self.value]

class StrVal(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symboltable):
        return ["String", self.value]

class VarDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        key = self.children[0].value
        if self.children[1] == 0 or self.children[1] == '' :
            y = self.children[1]
        else:
            y = self.children[1].Evaluate(symboltable)
        symboltable.create(key, self.value, y)


class NoOp(Node):
    def __init__(self):
        self.value = 'NOOP'

    def Evaluate(self, symboltable):
        return 
    
class Print(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        print(self.children[0].Evaluate(symboltable)[1])
    
class Assign(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        x, y = self.children[0].value, self.children[1].Evaluate(symboltable)
        symboltable.set(x, y)

class Identifier(Node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self, symboltable):
        return symboltable.get(self.value)
    
class Block(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def Evaluate(self, symboltable):
        for child in self.children:
            if hasattr(child, 'value'):
                child.Evaluate(symboltable)
                if child.value == 'RETURN':
                    return child.Evaluate(symboltable)

class Return(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, symboltable):
        return self.children[0].Evaluate(symboltable)

class While(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, symboltable):
        while self.children[0].Evaluate(symboltable)[1]:
            self.children[1].Evaluate(symboltable)

class If(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, symboltable):
        if self.children[0].Evaluate(symboltable)[1]:
            self.children[1].Evaluate(symboltable)
        elif len(self.children) == 3:
            self.children[2].Evaluate(symboltable)

class FuncDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, symboltable):
        functiontable.create(self.children[0], self)

class FuncCall(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, symboltable):
        funcDec = functiontable.get(self.value)
        if (len(funcDec.children[1]) != len(self.children)):
            raise Exception('Numero de argumentos invalido')
        
        newSt = SymbolTable()

        if len(self.children) != 0:
            for i in range(len(funcDec.children[1])):
                newSt.create(funcDec.children[1][i].children[0].value, funcDec.children[1][i].value, funcDec.children[1][i].children[1])
            for i in range(len(funcDec.children[1])):
                arg = self.children[i]
                vardec = funcDec.children[1][i]
                argType = arg.Evaluate(symboltable)[0]
                vardecType = newSt.get_type(vardec.children[0].value)
                if argType != vardecType:
                    raise Exception('Tipo de argumento invalido')
                else:
                    newSt.set(vardec.children[0].value, arg.Evaluate(symboltable))
        ret_block = funcDec.children[2].Evaluate(newSt)
        return ret_block

class SymbolTable:
    def __init__(self):
        self.table = {}

    def set(self, key, value):
        if key not in self.table:
            raise Exception('Variable does not exist')
        else:
            if self.table[key][0] == value[0]:
                self.table[key][1] = value
            else:
                raise Exception('Type mismatch')

    def get(self, key):
        return self.table[key][1]
    
    def get_type(self, key):
        return self.table[key][0]
    
    def create(self, key, _type, value):
        if key in self.table:
            raise Exception('Variable already exists')
        else:
            self.table[key] = [_type, value]

class FuncTable:
    def __init__(self):
        self.table = {}
    
    def create(self, key, value):
        if key  in self.table:
            raise Exception('Function already exists')
        else:
            self.table[key] = value
        
    def get(self, key):
        return self.table[key]

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = self.selectNext()

    def selectNext(self):
        original_size = len(self.source)
        while self.position < original_size and self.source[self.position]==' ':
            self.position += 1
        if self.position == original_size:
            self.next = Token('EOE', '')
        elif self.source[self.position].isdigit():
            n = ''
            while self.position < original_size and self.source[self.position].isdigit():
                n = n + self.source[self.position]
                self.position += 1
            self.next = Token('INTEGER', n)
        elif self.position < original_size and self.source[self.position] == '-':
            self.next = Token('SUB', '-')
            self.position += 1
        elif self.position < original_size and self.source[self.position] == '"':
            string = ''
            self.position += 1
            while self.position < original_size and self.source[self.position] != '"':
                string += self.source[self.position]
                self.position += 1
            self.position += 1
            self.next = Token('STRING', string)
        elif self.position < original_size and self.source[self.position] == '+':
            self.next = Token('ADD', '+')
            self.position += 1
        elif self.position < original_size and self.source[self.position] == '(':
            self.next = Token('O_PAR', '(')
            self.position += 1
        elif self.position < original_size and self.source[self.position] == ')':
            self.next = Token('C_PAR', ')')
            self.position += 1
        elif self.position < original_size and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
            n = ''
            while self.position < original_size and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                n = n + self.source[self.position]
                self.position += 1
            if n in reserved_words:
                if n == 'INTEGER' or n == 'STRING':
                    self.next = Token('TYPE', n)
                elif n == 'AND':
                    self.next = Token('AND', n)
                elif n == 'OR':
                    self.next = Token('OR', n)
                else:
                    self.next = Token('RESERVED', n)
            else:
                self.next = Token('IDENTIFIER', n)
        elif self.position < original_size and self.source[self.position] == '\n':
            self.next = Token('NEW_LINE', '\n')
            self.position += 1
        elif self.position < original_size and self.source[self.position] == '=':
            if self.position + 1 < original_size and self.source[self.position+1] == '=':
                self.next = Token('EQUAL', '==')
                self.position += 2
            else:
                self.next = Token('ASSIGN', '=')
                self.position += 1
        elif self.position < original_size and self.source[self.position] == '>':
            if self.position + 1 < original_size and self.source[self.position+1] == '=':
                self.next = Token('GREATER_EQUAL', '>=')
                self.position += 2
            else:
                self.next = Token('GREATER', '>')
                self.position += 1
        elif self.position < original_size and self.source[self.position] == '<':
            if self.position + 1 < original_size and self.source[self.position+1] == '>':
                self.next = Token('DIFFERENT', '<>')
                self.position += 2
            elif self.position + 1 < original_size and self.source[self.position+1] == '=':
                self.next = Token('LESS_EQUAL', '<=')
                self.position += 2
            else:
                self.next = Token('LESS', '<')
                self.position += 1
        elif self.position < original_size and self.source[self.position] == ',':
            self.next = Token('COMMA', ',')
            self.position += 1
        else:
            raise Exception('Algo de estranho aconteceu, confira a entrada')
        return self.next   
 
class Parser:
    def __init__(self, source):
        self.tokenizer = Tokenizer(source)
        

    def parseBlock(self):
        result = []
        while self.tokenizer.next.type != 'EOE':
            result.append(self.parseStatement())
        return Block('BLOCK', result)  
    
    def parseStatement(self):
        if self.tokenizer.next.type == 'NEW_LINE':
            self.tokenizer.selectNext()
            return NoOp()
        
        if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'DECLARE':
            self.tokenizer.selectNext()
            identifier = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'AS':
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'TYPE':
                    _type = self.tokenizer.next.value
                    self.tokenizer.selectNext()
                    if _type == 'INTEGER':    
                        return VarDec(_type, [Identifier(identifier), 0])
                    elif _type == 'STRING':
                        return VarDec(_type, [Identifier(identifier), ''])
                     
                
        elif self.tokenizer.next.type == 'IDENTIFIER':
            identifier = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'O_PAR':
                self.tokenizer.selectNext()
                args = []
                if self.tokenizer.next.value == 'C_PAR':
                    self.tokenizer.selectNext()
                    return FuncCall(identifier, args)
                else:
                    args.append(self.parseRelExpr())
                    while self.tokenizer.next.type == 'COMMA':
                        self.tokenizer.selectNext()
                        args.append(self.parseRelExpr())
                    if self.tokenizer.next.type == 'C_PAR':
                        self.tokenizer.selectNext()
                        return FuncCall(identifier, args)
                    else:
                        raise Exception('Algo de estranho aconteceu, confira a entrada')

            elif self.tokenizer.next.type == 'ASSIGN':
                self.tokenizer.selectNext()
                return Assign('ASSIGN', [Identifier(identifier), self.parseRelExpr()])
            
            elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'AS':
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'TYPE':
                    _type = self.tokenizer.next.value
                    self.tokenizer.selectNext()
                    if _type == 'INTEGER':    
                        return VarDec(_type, [Identifier(identifier), 0])
                    elif _type == 'STRING':
                        return VarDec(_type, [Identifier(identifier), ''])
            else:
                raise Exception('Algo de estranho aconteceu, confira a entrada')
            
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'RETURN':
            self.tokenizer.selectNext()
            return Return('RETURN', [self.parseRelExpr()])

        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'PRINT':
            self.tokenizer.selectNext()
            to_print = self.parseRelExpr()
            return Print('PRINT', [to_print]) 
                
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'WHILE':
            self.tokenizer.selectNext()
            condition = self.parseRelExpr()   
            if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'DO':
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'NEW_LINE': 
                    self.tokenizer.selectNext()
                    body = Block('BLOCK', [])
                    while self.tokenizer.next.value != 'ENDWHILE':
                        body.children.append(self.parseStatement())
                    if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'ENDWHILE':
                        self.tokenizer.selectNext()
                        return While('WHILE', [condition, body])
        
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'IF':
            self.tokenizer.selectNext()
            condition = self.parseRelExpr()
            if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'THEN':
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'NEW_LINE':
                    self.tokenizer.selectNext()
                    body = Block('BLOCK', [])
                    newline = False
                    control = True
                    while control:
                        if self.tokenizer.next.type == 'NEW_LINE':
                            newline = True
                            self.tokenizer.selectNext()
                        if newline and (self.tokenizer.next.value == 'ENDIF' or self.tokenizer.next.value == 'ELSE'):
                                control = False
                        if control:
                            body.children.append(self.parseStatement())

                    if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'ELSE':
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.type == 'NEW_LINE':
                            self.tokenizer.selectNext()
                            else_body = Block('BLOCK', [])
                            while self.tokenizer.next.value != 'ENDIF':
                                else_body.children.append(self.parseStatement())
                            if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'ENDIF':
                                self.tokenizer.selectNext()
                                return If('IF', [condition, body, else_body])
                            else:
                                raise Exception('Algo de estranho aconteceu, confira a entrada')
                    elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'ENDIF':
                        self.tokenizer.selectNext()
                        return If('IF', [condition, body])
                    else:
                        raise Exception('Algo de estranho aconteceu, confira a entrada')

        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'FUNCTION':
            self.tokenizer.selectNext()
            identifier = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'O_PAR':
                self.tokenizer.selectNext()
                args = []
                if self.tokenizer.next.type == 'IDENTIFIER':
                    args.append(self.parseStatement())
                    while self.tokenizer.next.type == 'COMMA':
                        self.tokenizer.selectNext()           
                        args.append(self.parseStatement())
                if self.tokenizer.next.type == 'C_PAR':
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == 'NEW_LINE':
                        self.tokenizer.selectNext()
                        body = Block('BLOCK', [])
                        while self.tokenizer.next.value != 'ENDFUNCTION':
                            body.children.append(self.parseStatement())
                        if self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'ENDFUNCTION':
                            self.tokenizer.selectNext()
                            return FuncDec("FUNC", [identifier, args, body])
                        else:
                            raise Exception('Algo de estranho aconteceu, confira a entrada')
        else:
            raise Exception('Algo de estranho aconteceu, confira a entrada')

    def parseFactor(self):
        if self.tokenizer.next.type == 'INTEGER':
            result = int(self.tokenizer.next.value)
            self.tokenizer.selectNext()
            return IntVal(result)
        elif self.tokenizer.next.type == 'STRING':
            result = self.tokenizer.next.value
            self.tokenizer.selectNext()
            return StrVal(result)
        elif self.tokenizer.next.type == 'ADD':
            self.tokenizer.selectNext()
            result = self.parseFactor()
            return UnOp('+', [result])
        elif self.tokenizer.next.type == 'SUB':
            self.tokenizer.selectNext()
            result = self.parseFactor()
            return UnOp('-', [result])
        
        elif self.tokenizer.next.type == 'O_PAR':
            self.tokenizer.selectNext()
            result = self.parseRelExpr()
            if self.tokenizer.next.type == 'C_PAR':
                self.tokenizer.selectNext()
                return result
            else:
                raise Exception('Algo de estranho aconteceu, confira a entrada')
        elif self.tokenizer.next.type == 'IDENTIFIER':
            result = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'O_PAR':
                self.tokenizer.selectNext()
                args = []
                if self.tokenizer.next.type == 'C_PAR':
                    self.tokenizer.selectNext()
                    return FuncCall(result, args)
                else:
                    args.append(self.parseRelExpr())
                    while self.tokenizer.next.type == 'COMMA':
                        self.tokenizer.selectNext()
                        args.append(self.parseRelExpr())
                    if self.tokenizer.next.type == 'C_PAR':
                        self.tokenizer.selectNext()
                        return FuncCall(result, args)
                    else:
                        raise Exception('Algo de estranho aconteceu, confira a entrada')
            else:
                return Identifier(result)
        else:
            raise Exception('Algo de estranho aconteceu, confira a entrada')

    def parseTerm(self):
        result = self.parseFactor()
        while self.tokenizer.next.type == 'AND':
            if self.tokenizer.next.type == 'AND':
                self.tokenizer.selectNext()
                result = BinOp('AND', [result, self.parseFactor()])
        return result
    
    def parseExpression(self):
        result = self.parseTerm()
        while self.tokenizer.next.type == 'ADD' or self.tokenizer.next.type == 'SUB' or self.tokenizer.next.type == 'OR':
            if self.tokenizer.next.type == 'ADD':
                self.tokenizer.selectNext()
                result = BinOp('+', [result, self.parseTerm()])
            elif self.tokenizer.next.type == 'SUB':
                self.tokenizer.selectNext()
                result = BinOp('-', [result, self.parseTerm()])
            elif self.tokenizer.next.type == 'OR':
                self.tokenizer.selectNext()
                result = BinOp('OR', [result, self.parseTerm()])
        return result
    
    def parseRelExpr(self):
        result = self.parseExpression()
        while self.tokenizer.next.type == 'EQUAL' or self.tokenizer.next.type == 'GREATER' or self.tokenizer.next.type == 'LESS' or self.tokenizer.next.type == 'LESS_EQUAL' or self.tokenizer.next.type == 'GREATER_EQUAL' or self.tokenizer.next.type == 'DIFFERENT':
            if self.tokenizer.next.type == 'EQUAL':
                self.tokenizer.selectNext()
                result = BinOp('==', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'DIFFERENT':
                self.tokenizer.selectNext()
                result = BinOp('<>', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'GREATER':
                self.tokenizer.selectNext()
                result = BinOp('>', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'LESS':
                self.tokenizer.selectNext()
                result = BinOp('<', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'LESS_EQUAL':
                self.tokenizer.selectNext()
                result = BinOp('<=', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'GREATER_EQUAL':
                self.tokenizer.selectNext()
                result = BinOp('>=', [result, self.parseExpression()])
        return result

    @staticmethod
    def run(self, symboltable):
        result = self.parseBlock()
        if self.tokenizer.next.type != 'EOE':
            raise Exception('Algo de estranho aconteceu, confira a entrada')
        return result.Evaluate(symboltable)
        
global functiontable
functiontable = FuncTable()

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        code = f.read()

    symboltable = SymbolTable()
    code = PrePro.filter(code)
    Parser.run(Parser(code), symboltable) 