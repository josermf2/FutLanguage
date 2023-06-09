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
    NUMBER = 258,                  /* NUMBER  */
    STRING = 259,                  /* STRING  */
    IDENTIFIER = 260,              /* IDENTIFIER  */
    IF = 261,                      /* IF  */
    THEN = 262,                    /* THEN  */
    ELSE = 263,                    /* ELSE  */
    ENDIF = 264,                   /* ENDIF  */
    WHILE = 265,                   /* WHILE  */
    DO = 266,                      /* DO  */
    ENDWHILE = 267,                /* ENDWHILE  */
    FUNCTION = 268,                /* FUNCTION  */
    ENDFUNCTION = 269,             /* ENDFUNCTION  */
    DECLARE = 270,                 /* DECLARE  */
    AS = 271,                      /* AS  */
    PRINT = 272,                   /* PRINT  */
    TYPE_STRING = 273,             /* TYPE_STRING  */
    TYPE_INTEGER = 274,            /* TYPE_INTEGER  */
    AND = 275,                     /* AND  */
    OR = 276,                      /* OR  */
    EQUAL = 277,                   /* EQUAL  */
    COMP_EQUAL = 278,              /* COMP_EQUAL  */
    NOT_EQUAL = 279,               /* NOT_EQUAL  */
    LESS_THAN = 280,               /* LESS_THAN  */
    GREATER_THAN = 281,            /* GREATER_THAN  */
    LESS_THAN_OR_EQUAL = 282,      /* LESS_THAN_OR_EQUAL  */
    GREATER_THAN_OR_EQUAL = 283,   /* GREATER_THAN_OR_EQUAL  */
    LEFT_PARENTHESIS = 284,        /* LEFT_PARENTHESIS  */
    RIGHT_PARENTHESIS = 285,       /* RIGHT_PARENTHESIS  */
    PLUS = 286,                    /* PLUS  */
    MINUS = 287,                   /* MINUS  */
    COMMA = 288,                   /* COMMA  */
    RETURN = 289                   /* RETURN  */
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
