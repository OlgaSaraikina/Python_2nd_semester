
print ("   Task 1")
print ("Enter the number of iterations:")
g = int (input())
cntg = 0
print ("Enter the numbers:")
for x in range(g):
    ch = int (input())
    if ch == 0:
        cntg += 1
if cntg != 0:
    print(cntg)
else:
    print ("There are no zeros here")
    
print ("   Task 2")
print ("Enter a natural number up to 2e9:")
n = int (input())
cnt = 0
if n > 0 and n <= 2000000000:
    for i in range(1,n+1):
      if n % i == 0:
            cnt +=1
    print (f"Number of divisors = {cnt}")
else:
    print ("a negative number")

print ("   Task 3")
print ("Enter the numbers a and b, where a is less than b:")
a, b = map(int, input().split())
if a<=b:
   for y in range(a, b+1):
     if  y % 2 == 0:
        print(y, end=' ')   
else:
    print ("a is more b")
