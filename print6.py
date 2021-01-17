name=input('Username: ')

if len(name)<=5:
    print('Username not long enough')
elif len(name)>50:
    print('Username is too long')
else :
    print('Username accepted')
