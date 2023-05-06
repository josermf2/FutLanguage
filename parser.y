%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %sn", s); }
%}

%token DIGIT NUMBER LETTER STRING VARIABLE IF THEN ELSE ENDIF WHILE DO ENDWHILE FUNCTION ENDFUNCTION DECLARE AS PRINT TYPE_STRING TYPE_INTEGER AND OR EQUAL NOT_EQUAL LESS_THAN GREATER_THAN LESS_THAN_OR_EQUAL GREATER_THAN_OR_EQUAL LEFT_PARENTHESIS RIGHT_PARENTHESIS PLUS MINUS COMMA RETURN
%token TEAM1_SCORE TEAM2_SCORE POSSESSION GAME_TIME TEAM1_PLAYER1 TEAM1_PLAYER2 TEAM1_PLAYER3 TEAM1_PLAYER4 TEAM1_PLAYER5 TEAM1_PLAYER6 TEAM1_PLAYER7 TEAM1_PLAYER8 TEAM1_PLAYER9 TEAM1_PLAYER10 TEAM1_PLAYER11 TEAM2_PLAYER1 TEAM2_PLAYER2 TEAM2_PLAYER3 TEAM2_PLAYER4 TEAM2_PLAYER5 TEAM2_PLAYER6 TEAM2_PLAYER7 TEAM2_PLAYER8 TEAM2_PLAYER9 TEAM2_PLAYER10 TEAM2_PLAYER11

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
    | FUNCTION VARIABLE LEFT_PARENTHESIS RIGHT_PARENTHESIS statements RETURN expression ENDFUNCTION
    | DECLARE VARIABLE AS type
    | VARIABLE EQUAL expression
    | PRINT expression
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
    | VARIABLE
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
