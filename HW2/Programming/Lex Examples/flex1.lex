Fall 2006
Program Development 4
An example Flex program
/* either indent or use %{ %} */
%{
int num_lines = 0;
int num_chars = 0;
%}
%%
\n ++num_lines; ++num_chars;
. ++num_chars;
%%
int main(int argc, char **argv)
{
yylex();
printf("# of lines = %d, # of chars = %d\n",
num_lines, num_chars );
}