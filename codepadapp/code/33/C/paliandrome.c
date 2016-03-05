#include <stdio.h>

int main(){
    // type your code here
int a=121,r,s=0,n;
n=a;
while(n>0)
{
r=n%10;
s=s*10+r;
n=n/10;
}
if(a == s)
printf("paliandrome");
else
printf("not paliandrome");

    return 0;
}
