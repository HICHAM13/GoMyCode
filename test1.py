print("hello GoMyCode")
poids = int(input("poids : "))
unité = input("(K) g or (L)bs: ")
if unité.upper  == "K":
    converted = poids / 0.45
    print ("poids en Kg : " + str(converted))
else:
    converted = poids * 0.45
    print("poinds en lbs :" + str(converted))
#Question 1
n = int(input('enter a number : '))
t = str(n)
t1 = t+t
t2= t+t+t
final = n + int(t1)+int(t2)
print("The result is : ", final)
#QUESTION 2
num=int(input('enter a number : '))
t1=num % 2
if t1>0:
    print("This is an odd number")
else:
    print("this is an even number")
#Question 3
dm=[]
for x in range(2000,3200):
    if (x%7==0)and(x%5!=0):
        dm.append(str(x))
print(','.join(dm))
#Question 4
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a number to compute factorial : "))
print(factorial(n))