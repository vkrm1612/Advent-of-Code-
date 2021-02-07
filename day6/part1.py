input_data = list(open('day6.txt'))
dummy=[]
answers=[]
number=[]
for x in input_data:
    if x=='\n':
        answers.append(dummy)
        dummy=[]
    if x!='\n':
        x=x.replace('\n','')
        dummy.append(x)
counter=0
for group in answers:
    i=[]
    for person in group:
        for _ans_ in person:
            i.append(_ans_)
    i=list(set(i))
    counter+=len(i)

print(f'no of answerd marked yes : {counter}')