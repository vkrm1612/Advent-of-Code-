file=open('day3.txt','r')
data=[x.strip() for x in file ]
slopes=[[1,1],[3,1],[5,1],[7,1],[1,2]]
cordinates=[tress*100 for tress in data]
product_0f_trees=1
for slope in slopes:
    right , down = slope
    x=0
    y=0
    no_of_trees=0
    while y < len(cordinates)-1:
        x+=right
        y+=down
        #print(y,x)
        if cordinates[y][x]=='#':
            no_of_trees+=1
    product_0f_trees=product_0f_trees*no_of_trees

print(f'product of number of trees encounterd : {product_0f_trees}')

