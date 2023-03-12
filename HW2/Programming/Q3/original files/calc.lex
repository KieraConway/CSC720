%{
#include <stdio.h>

#define YY_DECL int yylex()

#include "calc.tab.h"

%}

%%

[ \t]	;
[0-9]+	{yylval.ival = atoi(yytext); return NUM; }
\n	{return '\n';}
"+"	{return '+';}
"-"	{return '-';}
"*"	{return '*';}
"/"	{return '/';}
"quit"	{return QUIT;}

%%
