%{

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

extern int yylex();
extern int yyparse();
extern FILE* yyin;

void yyerror(const char* s);
%}

%union {
	int ival;
}

%token<ival> NUM
%token QUIT
%left '+' '-'
%left '*' '/'

%type<ival> exp

%start calculation

%%

calculation: 
    | calculation line
;

line: '\n'
    | exp '\n' { printf("\tResult: %i\n", $1); } 
    | QUIT '\n' { printf("bye!\n"); exit(0); }
;

exp: NUM		{ $$ = $1; }
    | exp '+' exp	{ $$ = $1 + $3; }
    | exp '-' exp	{ $$ = $1 - $3; }
    | exp '*' exp	{ $$ = $1 * $3; }
    | exp '/' exp	{ $$ = $1 / $3; }
;

%%

main() {
	yyin = stdin;

	do { 
		yyparse();
	} while(!feof(yyin));
}

void yyerror(const char* s) {
	fprintf(stderr, "Parse error: %s\n", s);
	exit(1);
}
