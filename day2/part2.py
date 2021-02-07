file=open('day2.txt','r')
minimum=[]
maximum=[]
letter=[]
password=[]
for line in file:
    prase=line.split('\n')
    prase1=prase[0].split()
    prase2=prase1[0].split('-')
    prase3=list(prase1[1])
    minimum.append(int(prase2[0]))
    maximum.append(int(prase2[1]))
    letter.append(prase3[0])
    password.append(prase1[2])
valid_passwords=[]
for i in range(0,1000):
    code=list(password[i])
    if len(code)>=maximum[i]:
        if letter[i]==code[minimum[i]-1] or letter[i]==code[maximum[i]-1]:
            if letter[i] == code[minimum[i] - 1] and letter[i] == code[maximum[i] - 1]:
                pass
            else:
                valid_passwords.append(password[i])

print(f'The Total valid passwords are : {len(valid_passwords)}')
