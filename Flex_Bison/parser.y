%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token NUMBER STRING IDENTIFIER IF THEN ELSE ENDIF WHILE DO ENDWHILE FUNCTION ENDFUNCTION DECLARE AS PRINT TYPE_STRING TYPE_INTEGER AND OR EQUAL NOT_EQUAL LESS_THAN GREATER_THAN LESS_THAN_OR_EQUAL GREATER_THAN_OR_EQUAL LEFT_PARENTHESIS RIGHT_PARENTHESIS PLUS MINUS COMMA RETURN

%start program

%%
program:
    statements
    ;

statements:
    statement
    | statements statement
    ;

statement:
    IF expression THEN statements ELSE statements ENDIF
    | WHILE expression DO statements ENDWHILE
    | FUNCTION IDENTIFIER LEFT_PARENTHESIS parameter_list RIGHT_PARENTHESIS statements RETURN expression ENDFUNCTION
    | DECLARE IDENTIFIER AS type
    | IDENTIFIER EQUAL expression
    | PRINT expression
    ;

parameter_list:
    /* empty */
    | IDENTIFIER
    | parameter_list COMMA IDENTIFIER
    ;


expression:
    expression OR term
    | expression AND term
    | expression EQUAL term
    | expression NOT_EQUAL term
    | expression LESS_THAN term
    | expression GREATER_THAN term
    | expression LESS_THAN_OR_EQUAL term
    | expression GREATER_THAN_OR_EQUAL term
    | term
    ;

term:
    term PLUS factor
    | term MINUS factor
    | factor
    ;

factor:
    factor LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
    | value
    ;

value:
    NUMBER
    | STRING
    | IDENTIFIER
    ;

type:
    TYPE_STRING
    | TYPE_INTEGER
    ;

%%


int main() {
    yyparse();
    return 0;
}
