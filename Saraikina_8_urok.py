print ('   Task 1')
print ("Enter a string of up to 10000 characters")
n_1 = int (input())
res_1 = []
if 1 <= n_1 <= 10000:
   for i_1 in range(n_1):
         a_1 = int (input())
         if abs(a_1) <= 1000000:
            res_1.append(a_1)
         else:
            print (f'{a_1} the number modulo exceeds 10e5')
     
else:
    print('The number of elements exceeds 10000')
res_1.reverse()
print (*res_1)

print ('   Task 2')
print ("Enter the number N (1 ≤ N ≤ 100,000)")
n_2 = int (input())
res_2 = [] 
rev = []
print ("Enter N numbers (1 ≤ Ai ≤ 10e9) separated by a space")
tmp = list(map(int, input().split()))
if (1 <= n_2) and (n_2 <= 100000):
    for i in tmp:  
          res_2.append(i)
for c in range(len(res_2)):
    rev.append(c) 
    c + 1
if c+1 >  rev[-1]:
     rev[0] = res_2[-1]       
print (*rev)

print ('   Task 3')

print ('Enter the maximum boat load')
max_masa = int(input())
print ('Enter the number of fishermen')
n = int(input())
res = []
print ('Enter the weight of each fisherman in each new row (as a column):')
if ((max_masa >= 1) and (max_masa <= 10**7)) and ((n >= 1) and (n <= 100)):
    for y in range(n):
        m_r = int(input())
        if m_r <= max_masa:
            res.append(m_r)
        else:
            print('The boat will not withstand the weight of a fisherman')
    ret = (sorted(res))
    ret.reverse()
else:
    print ("The maximum load or the number of fishermen does not meet the condition")   
cnt, l, r = 0, 0, len(ret) - 1  
while r >= l:  
    if ret[l] + ret[r] <= max_masa:
        r -= 1  
    l += 1  
    cnt += 1  
print(f"Minimum number of boats => {cnt}")
