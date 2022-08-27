u = input('enter the username :')
E = input('enter the e-mail :')
p = input('enter the password')
cp =input('confirm password') 
g = input ('enter the gender')

if len(u)>4 and len(u)< 25:
    if '@' in E:
        if p == cp:
            print('your are register') 
        else:
            print('password not match')
    else:
        print('E-mail is invalid')
else:
    print('username must be between 4 and 25 char')                