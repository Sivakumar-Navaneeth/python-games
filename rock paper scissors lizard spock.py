import random
print('''PLAY
ROCK, PAPER, SCISSORS, LIZARD, SPOCK''')
t='yup'
m=c=0
while t=='yup':
    s=input('enter your choice: ')
    l=['rock','paper','scissors','lizard','spock']
    a=random.randint(0,4)
    s_=l[a]
    if s==s_:
        print('your choice ',s,' computer choose ',s_,'\n........DRAW......\n\n')
        c+=1
        m+=1
    elif ((s=='scissors' and s_=='paper') or (s=='scissors' and s_=='lizard') or (s=='paper' and s_=='rock') or (s=='rock' and s_=='lizard') or (s=='lizard' and s_=='spock') or (s=='spock' and s_=='scissors') or (s=='lizard' and s_=='paper') or (s=='paper' and s_=='spock') or (s=='spock' and s_=='rock') or (s=='rock' and s_=='scissors')):
        print('your choice ',s,' computer choose ',s_,'\n........YOU WIN!!!!......\n\n')
        m+=2
    else:
        print('your choice ',s,' computer choose ',s_,'\n........YOU LOSE.......\n\n')
        c+=2
    t=input('enter "yup" to continue: ')
print('your score = ',m)
print('computer score = ',c)
if c>=m:
    print('________.........COMPUTER WINS......__________')
elif m>=c:
    print('___________..........YOU WIN........__________')
else:
    print('__________............DRAW..........__________')
