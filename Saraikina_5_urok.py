#Task 1
print("      Task 1")
print('Enter any number')
c = input()
c = int(c)
if (c < 0) and c%2 != 0:
    print("A negative is not an even number")
elif c < 0 and c%2 == 0:
    print("A negative even number")
elif c > 0 and c%2 != 0:
    print("A positive non-even number")
elif c > 0 and c%2 == 0:
    print("A positive even number")
else:
    print('the zero number')
#Task 2
print("      Task 2")    
print("Enter the word: ")
st = input() 
a = st.count('a') 
e = st.count('e') 
i = st.count('i') 
o = st.count('o') 
u = st.count('u') 
y = st.count('y') 
if a != 0:
    print ("a -", st.count('a'))
else:
    print("a = False") 
if e != 0:
    print ("e -", st.count('e'))
else:
    print("e = False") 
if i != 0:
    print ("i -", st.count('i'))
else:
    print("i = False") 
if o != 0: 
      print ("o -", st.count('o'))
else:
    print("o = False") 
if u != 0: 
      print ("u -", st.count('u'))
else:
    print("u = False") 
if y != 0: 
      print ("y -", st.count('y'))
else:
    print("y = False") 
w = a + e + i + o + u
l = len(st)
print(f"Vowel letters: {w}") 
print(f"Consonant letters: {l - w}")

#Task 3
print("      Task 3")    
print ("Minimum investment amount:")
x = int (input())
print ("The volume of Ivan investments")
d = int (input())
print ("The volume of Mikle investments:")
b = int (input())
if d >= x and b >= x:
    print("2")
elif (d+b) >= x:
    if d >= x: 
        print("ivan")     
    elif b >= x:
       print("mike")
    else:
       print ("1")
else: 
    print("0")
