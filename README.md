# FUT Language

## Descrição:
 Linguagem de programação desenvolvida para a disciplina de Lógica da Computação do curso de Engenharia de Computação do Insper. A linguagem foi desenvolvida para simular ações de um jogo de futebol.

## Desenvolvido por:
* José Fernandes

## EBNF:
``` lua
PROGRAM = STATEMENT_LIST ;

STATEMENT_LIST = STATEMENT | STATEMENT STATEMENT_LIST ;

STATEMENT = ASSIGNMENT | CONDITIONAL | LOOP | FUNCTION | VARIABLE_DECLARATION | PRINT_STATEMENT ;

ASSIGNMENT = IDENTIFIER "=" EXPRESSION ;

CONDITIONAL = "IF" EXPRESSION "THEN" STATEMENT_LIST "ELSE" STATEMENT_LIST "ENDIF" ;

LOOP = "WHILE" EXPRESSION "DO" STATEMENT_LIST "ENDWHILE" ;

FUNCTION = "FUNCTION" IDENTIFIER "(" [PARAMETER_LIST] ")" STATEMENT_LIST "RETURN" EXPRESSION "ENDFUNCTION" ;

PARAMETER_LIST = IDENTIFIER "AS" TYPE | IDENTIFIER  "AS" TYPE "," PARAMETER_LIST ;

VARIABLE_DECLARATION = "DECLARE" IDENTIFIER "AS" TYPE ;

PRINT_STATEMENT = "PRINT" EXPRESSION ;

IDENTIFIER = LETTER (LETTER | DIGIT)* ;

TYPE = "INTEGER" | "STRING" ;

EXPRESSION = COMPARISON | COMPARISON LOGICAL_OPERATOR COMPARISON | NUMBER ADDITIVE_OPERATOR NUMBER; 

COMPARISON = TERM | TERM COMPARISON_OPERATOR TERM ;

TERM = IDENTIFIER | NUMBER | STRING | "(" EXPRESSION ")" ;

LOGICAL_OPERATOR = "AND" | "OR" ;

COMPARISON_OPERATOR = "=" | "<>" | "<" | ">" | "<=" | ">=" ;

ADDITIVE_OPERATOR = "+" | "-" ;

NUMBER = DIGIT | NUMBER DIGIT ;

STRING = '"' (LETTER | DIGIT)* '"' ;

LETTER = "A" | "B" | ... | "Z" | "a" | "b" | ... | "z" ;

DIGIT = "0" | "1" | ... | "9" ;

```

## Exemplo de programa

```
DECLARE TEAM1_SCORE AS INTEGER
DECLARE TEAM2_SCORE AS INTEGER
DECLARE POSSESSION AS INTEGER
DECLARE GAME_TIME AS INTEGER

FUNCTION increment_score(score AS INTEGER)
    score = score + 1
    RETURN score
ENDFUNCTION

TEAM1_SCORE = 0
TEAM2_SCORE = 0
POSSESSION = 1
GAME_TIME = 0

WHILE GAME_TIME < 90 DO
    GAME_TIME = GAME_TIME + 1
    
    IF POSSESSION == 1 THEN
        IF TEAM1_SCORE < 5 THEN
            TEAM1_SCORE = increment_score(TEAM1_SCORE)
            PRINT "Team 1 scores!"            
        ENDIF
        POSSESSION = 2
    ELSE
        IF TEAM2_SCORE < 4 THEN
            TEAM2_SCORE = increment_score(TEAM2_SCORE)
            PRINT "Team 2 scores!"
        ENDIF
        POSSESSION = 1
    ENDIF
ENDWHILE

IF TEAM1_SCORE > TEAM2_SCORE THEN
    PRINT "Team 1 wins!"
    PRINT TEAM1_SCORE
ELSE
    PRINT "Team 2 wins!"
    PRINT TEAM2_SCORE
ENDIF

IF TEAM1_SCORE == TEAM2_SCORE THEN
    PRINT "It's a draw!"
ENDIF
```

## Flex e Bison
Para fazer a análise sintática e léxica da linguagem, foram utilizados o Flex e o Bison.

Para compilar o programa, é necessário ter o Flex e o Bison instalados. Assim, para fazer as análises, basta rodar os seguintes comandos no terminal:

``` bash
cd Flex_Bison
flex -l fut.l
bison -dv parser.y
gcc -o analyzer parser.tab.c lex.yy.c -lfl
./analyzer < ../example.fut
```

## Compilador
O compilador da FUT Language utiliza como base o compilador desenvolvido na disciplina para julia. Ele faz todas as etapas de análise (léxica, sintática e semântica) e imprime o resultado do programa do terminal. 

Para compilar o programa de testes é necessário ter o python instalado. Para rodar, utilize o senguinte comando no terminal:
```bash
python3 compilator.py example.fut
```
