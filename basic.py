"basic python codes in different ways:"

#1 even odd
n=int(input("enter a number: "))
if n%2==0:
    print("even")
else:
    print("odd")
    
    
# without %
n=int(input("enter a number: "))
if n & 1==0:
    print("even")
else:
    print("odd")
    
# using recuring:
n=int(input("enter a nuber: "))
print("even" if n%2==0 else "odd")

# using function:
def oddeven(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(oddeven(12))

# using lambda:
n=int(input("enter a number: "))
result=lambda n: ("even" if n%2==0 else "odd")
print(result(n))

# ==============================================================================

# 2 find largest number of three numbers:

# find largest of three 
a=10
b=20
c=30
print(max(a,b,c))

# without max
a=10
b=20
c=30
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")

# using ternary operator:
a=10
b=20
c=30
largest=(a if a >b and a>c else(b if b>c else c))
print(largest)

#=============================================================================

## wap to swap two numbwe without using tird:

a=10
b=20
a,b=b,a
print(a,b)

a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)

a=10
b=20
a=a*b
b=a//b
a=a//b
print(a,b)

a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)

# ==============================================================================

#wap to check weather a numbere is prime or not:

n=int(input("enter a number: "))
if n<=0:
    print("not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime number")
        
# using function:
def isprime(n):
    if n<=0:
        return "not prime"
    else:
        for i in range(2,n):
            if n%i==0:
                return "not prime"
                break
        else:
            return "isprime"
print(isprime(11))


# ==============================================================================







