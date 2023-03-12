%{
/**** The beginnings of a calculator. ****/
#include <stdlib.h>
#include <stdio.h>
struct tokenInfo
{
  char *name;
  double  value;
  int lineNumber;
};
typedef struct tokenInfo tokenInfo;
struct tokenInfo2
{
  tokenInfo ti;
};  
struct tokenInfo2 yylval;
%}

%%

[a-z]   {
	   yylval.ti.value = 0;
	   yylval.ti.name =  (char *) strdup(yytext);
	   printf("VARIABLE: %s\n", yylval.ti.name);
        }

[0-9]+  {  
           yylval.ti.value = atoi(yytext);
	   yylval.ti.name = NULL;
           printf("INTEGER: %0.0f\n", yylval.ti.value);
        }

:=    printf("ASSIGNMENT\n");
\+     printf("PLUS\n");
\*     printf("MULTIPLY\n");

\n    printf("NEWLINE\n");

[ \t]   ;

.       printf("Invalid character\n");

%%

int yywrap() {
 return 1;
}

main( argc, argv )
int argc;
char **argv;
{
  ++argv, --argc;  /* skip over program name */
  if ( argc > 0 )
    yyin = fopen( argv[0], "r" );
  else
    yyin = stdin;
  
  yylex();
}
