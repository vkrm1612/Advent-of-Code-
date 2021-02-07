input_data = list(open('day6.txt'))
answers=[]
dummy=[]
lenghth=[]
for x in input_data:
    if x=='\n':
        answers.append(dummy)
        dummy=[]
    if x!='\n':
        x=x.replace('\n','')
        dummy.append(x)

counter=0
for x in answers:
    i=0
    dummy_1=[]
    while i<len(x):
        y=set(x[i])
        dummy_1.append(y)
        i+=1
    r = dummy_1[0]
    for x in dummy_1:
        r=r.intersection((x))
    counter+=len(r)

print(counter)