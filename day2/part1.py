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
    counter=0
    for x in range(0,len(password[i])):
        exa=list(password[i])
        if letter[i]==exa[x]:
            counter+=1
    if counter in range(minimum[i],maximum[i]+1):
        valid_passwords.append(password[i])

print(f'The valid passwords are  : {len(valid_passwords)}')

