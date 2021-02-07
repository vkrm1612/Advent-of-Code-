input=list(open('day4.txt').read().split('\n\n'))
data=[]
passport_dictionary=[]
valid_dictionary=[]
for x in input:
    y=x.replace('\n',' ')
    data.append(y)
def dicting(item):
    lisst=item.split()
    items ={}
    for x in lisst:
        key,value=x[:3],x[4:]
        items[key]=value
    return items
for i in data:
    y=dicting(i)
    passport_dictionary.append(y)
j=-1
while j < len(passport_dictionary)-1:
    j += 1

    if len(passport_dictionary[j])>7:
        valid_dictionary.append(passport_dictionary[j])
    if len(passport_dictionary[j])==7:
        li_1=[]
        for it in passport_dictionary[j]:
            li_1.append(it)
        bo = False
        for p in li_1:
            if p=='cid':
                bo=True
        if bo==False:
           valid_dictionary.append(passport_dictionary[j])

print(f'total valid passports :{len(valid_dictionary)}')
