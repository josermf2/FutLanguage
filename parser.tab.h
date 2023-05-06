/* A Bison parser, made by GNU Bison 3.7.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_PARSER_TAB_H_INCLUDED
# define YY_YY_PARSER_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    DIGIT = 258,                   /* DIGIT  */
    NUMBER = 259,                  /* NUMBER  */
    LETTER = 260,                  /* LETTER  */
    STRING = 261,                  /* STRING  */
    VARIABLE = 262,                /* VARIABLE  */
    IF = 263,                      /* IF  */
    THEN = 264,                    /* THEN  */
    ELSE = 265,                    /* ELSE  */
    ENDIF = 266,                   /* ENDIF  */
    WHILE = 267,                   /* WHILE  */
    DO = 268,                      /* DO  */
    ENDWHILE = 269,                /* ENDWHILE  */
    FUNCTION = 270,                /* FUNCTION  */
    ENDFUNCTION = 271,             /* ENDFUNCTION  */
    DECLARE = 272,                 /* DECLARE  */
    AS = 273,                      /* AS  */
    PRINT = 274,                   /* PRINT  */
    TYPE_STRING = 275,             /* TYPE_STRING  */
    TYPE_INTEGER = 276,            /* TYPE_INTEGER  */
    AND = 277,                     /* AND  */
    OR = 278,                      /* OR  */
    EQUAL = 279,                   /* EQUAL  */
    NOT_EQUAL = 280,               /* NOT_EQUAL  */
    LESS_THAN = 281,               /* LESS_THAN  */
    GREATER_THAN = 282,            /* GREATER_THAN  */
    LESS_THAN_OR_EQUAL = 283,      /* LESS_THAN_OR_EQUAL  */
    GREATER_THAN_OR_EQUAL = 284,   /* GREATER_THAN_OR_EQUAL  */
    LEFT_PARENTHESIS = 285,        /* LEFT_PARENTHESIS  */
    RIGHT_PARENTHESIS = 286,       /* RIGHT_PARENTHESIS  */
    PLUS = 287,                    /* PLUS  */
    MINUS = 288,                   /* MINUS  */
    COMMA = 289,                   /* COMMA  */
    RETURN = 290,                  /* RETURN  */
    TEAM1_SCORE = 291,             /* TEAM1_SCORE  */
    TEAM2_SCORE = 292,             /* TEAM2_SCORE  */
    POSSESSION = 293,              /* POSSESSION  */
    GAME_TIME = 294,               /* GAME_TIME  */
    TEAM1_PLAYER1 = 295,           /* TEAM1_PLAYER1  */
    TEAM1_PLAYER2 = 296,           /* TEAM1_PLAYER2  */
    TEAM1_PLAYER3 = 297,           /* TEAM1_PLAYER3  */
    TEAM1_PLAYER4 = 298,           /* TEAM1_PLAYER4  */
    TEAM1_PLAYER5 = 299,           /* TEAM1_PLAYER5  */
    TEAM1_PLAYER6 = 300,           /* TEAM1_PLAYER6  */
    TEAM1_PLAYER7 = 301,           /* TEAM1_PLAYER7  */
    TEAM1_PLAYER8 = 302,           /* TEAM1_PLAYER8  */
    TEAM1_PLAYER9 = 303,           /* TEAM1_PLAYER9  */
    TEAM1_PLAYER10 = 304,          /* TEAM1_PLAYER10  */
    TEAM1_PLAYER11 = 305,          /* TEAM1_PLAYER11  */
    TEAM2_PLAYER1 = 306,           /* TEAM2_PLAYER1  */
    TEAM2_PLAYER2 = 307,           /* TEAM2_PLAYER2  */
    TEAM2_PLAYER3 = 308,           /* TEAM2_PLAYER3  */
    TEAM2_PLAYER4 = 309,           /* TEAM2_PLAYER4  */
    TEAM2_PLAYER5 = 310,           /* TEAM2_PLAYER5  */
    TEAM2_PLAYER6 = 311,           /* TEAM2_PLAYER6  */
    TEAM2_PLAYER7 = 312,           /* TEAM2_PLAYER7  */
    TEAM2_PLAYER8 = 313,           /* TEAM2_PLAYER8  */
    TEAM2_PLAYER9 = 314,           /* TEAM2_PLAYER9  */
    TEAM2_PLAYER10 = 315,          /* TEAM2_PLAYER10  */
    TEAM2_PLAYER11 = 316           /* TEAM2_PLAYER11  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_PARSER_TAB_H_INCLUDED  */
