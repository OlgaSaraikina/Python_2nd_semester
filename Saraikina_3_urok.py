# �������1
print('Task 1')
print("  Welcom. Enter the pet's details")
print("   1.Type of pet")
typ = (input('   >>'))
print("   2.Age of the pet")
age = (input('   >>'))
print("   3.Pet's nickname")
name = (input('   >>'))
run =(f'   {typ}, {age}, {name}')
print(run)

# �������2
print('Task 2')
print("   Write human development beginning with, in five stages: 1.Dryopithecus")
ot = input("    2.")
tt = input("    3.")
ff = input("    4.")
yf = input('    5.')
res = '    1.Dryopithecus','=> 2.',ot,'=> 3.',tt,'=> 4.',ff,'=> 5.',yf
print(   *res)
print('       The correct answer:')
print("    1.Dryopithecus","2.Australopithecus","3.Homo habilis","4.Homo erectus","5.Homo sapiens", sep='=>')