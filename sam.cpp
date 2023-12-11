#include<iostream>
#include<stdlib>

int main()
{
	int a,b,c,d;
	cin>>a>>b;
	if(a>b)
	  c = a+b;
	if(b>a)
	  c = a-b;
	cout<<a<<b<<c;
	d = a+b+c;
}
