print ('   Task 1')
print ('Enter a word without a space to check the palindrome:')
tmp = input()
c = tmp[::-1]
if tmp == c:
    print ('yes')
else:
    print ('no')

print ('   Task 2')
print ('Enter a string of up to 1000 characters:')
st = input()
if len(st) <= 1000:
    st = st.split(' ')
    n = 0
    while n < len(st):
        if st[n] == '':
            del st[n]
            n -= 1
        else:
            n += 1
    st = ' '.join(st)
    print(st)
else:
    print ('Error: Enter a string of up to 1000 characters')


