print('''PLAY
......MASTER MIND.......

rules:
+  = no is there in that pos
x  = no is not there 
.  = no is there but not in that position
YOU GET TO CHOSE YOUR LVL (1,3-tough , 4,7-medium , 8 and above-difficult)
HOW MANY TRIES DO YOU WANT''')

c_=int(input('enter the number : '))

import random
l_=str(random.randint(10000,99999))
for j in range (c_):
    l=(input('enter 5 the digits : \n'))
    for k in range (5):
        if l==l_:
            print('<<<<<<<<.....you won!!!!....>>>>>>>>')
            break
            
        if int(l[k])==int(l_[k]):
            print('+',end='')
            
        elif (l[k])not in l_:
            print('x',end='')
            
        elif l[k] in l_:
            print('.',end='')
            
    if l==l_:
        break
    print('\n')
    
if l_!=l:
    print('<<<<<<<<.....you lost!!!!....>>>>>>>>')
