

#include <stdio.h>

int main()

{

char main[20]="Yash raj zade";

int i=0,j=0;

while(main[i]!='\0')

{

if( main[i]==32 && j<1)

{

printf("%c.",main[i+1]);

j++;

}

else if(i==0)

printf("%c.",main[0]);

else if(main[i]==32)

{

while(main[i]!='\0')

{

printf("%c",main[i+1]);

i++;

}

}

i++;

}

}
