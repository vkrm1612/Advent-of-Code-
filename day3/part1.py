input=open("day3.txt",'r')
cordinates=list(map(lambda x: x.strip(),input))
cordinates=[row*(len(cordinates)+1) for row in cordinates]
right , down = 3,1
x=0
y=0
counter=0
while y<len(cordinates)-1:
    x+=right
    y+=down
    if cordinates[y][x]=='#':
        counter+=1
print(f'no of trees encountered : {counter}')