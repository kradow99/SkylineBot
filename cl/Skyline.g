grammar Skyline;

root : instr | EOF ;
instr : (assig | sl) ;
assig : ID IS sl ;
sl : LPAR sl RPAR
  | RES sl
  | sl MUL sl
  | sl MUL number
  | sl ADD sl
  | sl ADD number
  | sl RES number
  | ID | simple | comp | random ;

simple : LPAR number COMMA number COMMA number RPAR ;
comp : LSQUA simple (COMMA simple)* RSQUA ;
random : LCURL number COMMA number COMMA number COMMA number COMMA number RCURL ;

number : LPAR number RPAR | NUM ;


IS : ':=' ;
LPAR : '(' ;
RPAR : ')' ;
LSQUA: '[' ;
RSQUA: ']' ;
LCURL: '{' ;
RCURL: '}' ;
COMMA : ',' ;
ID : CHAR (CHAR | NUM)* ;
CHAR : [A-Z] | [a-z] ;
NUM : [0-9]+ ;
ADD : '+' ;
RES : '-' ;
MUL : '*' ;
WS : [ \t\r\n]+ -> skip ;
