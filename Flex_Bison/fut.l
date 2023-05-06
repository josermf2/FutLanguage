%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

DIGIT [0-9]
LETTER [a-zA-Z]
VARIABLES TEAM1_SCORE|TEAM2_SCORE|POSSESSION|GAME_TIME|TEAM1_PLAYER1|TEAM1_PLAYER2|TEAM1_PLAYER3|TEAM1_PLAYER4|TEAM1_PLAYER5|TEAM1_PLAYER6|TEAM1_PLAYER7|TEAM1_PLAYER8|TEAM1_PLAYER9|TEAM1_PLAYER10|TEAM1_PLAYER11|TEAM2_PLAYER1|TEAM2_PLAYER2|TEAM2_PLAYER3|TEAM2_PLAYER4|TEAM2_PLAYER5|TEAM2_PLAYER6|TEAM2_PLAYER7|TEAM2_PLAYER8|TEAM2_PLAYER9|TEAM2_PLAYER10|TEAM2_PLAYER11

%%
[ \t\n]

"IF" { printf("IF\n"); return IF; }
"THEN" { printf("THEN\n"); return THEN; }
"ELSE" { printf("ELSE\n"); return ELSE; }
"ENDIF" { printf("ENDIF\n"); return ENDIF; }
"WHILE" { printf("WHILE\n"); return WHILE; }
"DO" { printf("DO\n"); return DO; }
"ENDWHILE" { printf("ENDWHILE\n"); return ENDWHILE; }
"FUNCTION" { printf("FUNCTION\n"); return FUNCTION; }
"ENDFUNCTION" { printf("ENDFUNCTION\n"); return ENDFUNCTION; }
"DECLARE" { printf("DECLARE\n"); return DECLARE; }
"AS" { printf("AS\n"); return AS; }
"PRINT" { printf("PRINT\n"); return PRINT; }
"STRING" { printf("TYPE STRING\n"); return TYPE_STRING; }
"INTEGER" { printf("TYPE INTEGER\n"); return TYPE_INTEGER; }
"AND" { printf("AND\n"); return AND; }
"OR" { printf("OR\n"); return OR; }
"=" { printf("EQUAL\n"); return EQUAL; }
"<>" { printf("NOT EQUAL\n"); return NOT_EQUAL; }
"<" { printf("LESS THAN\n"); return LESS_THAN; }
">" { printf("GREATER THAN\n"); return GREATER_THAN; }
"<=" { printf("LESS THAN OR EQUAL\n"); return LESS_THAN_OR_EQUAL; }
">=" { printf("GREATER THAN OR EQUAL\n"); return GREATER_THAN_OR_EQUAL; }
"(" { printf("LEFT PARENTHESIS\n"); return LEFT_PARENTHESIS; }
")" { printf("RIGHT PARENTHESIS\n"); return RIGHT_PARENTHESIS; }
"+" { printf("PLUS\n"); return PLUS; }
"-" { printf("MINUS\n"); return MINUS; }
"," { printf("COMMA\n"); return COMMA; }
"RETURN" { printf("RETURN\n"); return RETURN; }

{DIGIT}+ { printf("NUMBER\n"); return NUMBER; }
\"(\\.|[^\"\n])*\" { printf("STRING\n"); return STRING; }
{VARIABLES}|[a-zA-Z_][_a-zA-Z0-9]* { printf("IDENTIFIER\n"); return IDENTIFIER; } 


.  {printf("Unknown token!n"); yyterminate();};


%%
