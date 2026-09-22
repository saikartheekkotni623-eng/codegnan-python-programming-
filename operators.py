Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthimatic operators
a=5
b=4

print(a+b)
9
print(a-b)
1
print(a*b)
20
print(a//b)
1
print(a/b)
1.25
print(a%b)
1
print(a**b)
625
#assignment
a=6
b=3
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
9
a-=1
a
8
a*=5
a
40
a//=2
a
20
a/=3
a
6.666666666666667
a**=2
a
44.44444444444445
a%=4
a
0.44444444444444997
  a
  
SyntaxError: unexpected indent
a
0.44444444444444997
#comparison
a=7
b=9
a<b
True
a<=b
True
a>b
False
a=>b
SyntaxError: invalid syntax
a<=b
True
b<=a
False
a!=b
True
a==b
False
a=5
b=5
a==b
True
#logical
a=10
b=11
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
not True
False
not False
True
#identity
#is,is not
a=5
type(a) is int
True
>>> type(a) is not int
False
>>> type(a)is float
False
>>> type(a) is not float
True
>>> #membership
>>> a=4,5,6,7,8,9,10
>>> 10 in a
True
>>> 20 in a
False
>>> 34 not in a
True
