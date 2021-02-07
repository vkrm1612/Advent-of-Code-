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

pure_valid_passports=0
for n in valid_dictionary:
    counter=0
    if 1919 < int(n['byr']) <2003 and 2009 <  int(n['iyr']) <2021 and  2019 < int(n['eyr']) < 2031 :
        counter+=1
    if n['hcl'][0] == '#' and len(n['hcl']) == 7:
        counter+=1
    if n['ecl'] == 'amb' or n['ecl'] == 'blu' or n['ecl'] == 'brn' or n['ecl'] == 'gry' or n['ecl'] == 'grn' or n['ecl'] == 'hzl' or n['ecl'] == 'oth':
        counter+=1
    if len(n['pid']) == 9:
        counter+=1
    vari=n['hgt']
    if vari[-2:] == 'cm':
        if 149 < int(vari[:-2])  < 194:
            counter+=1
    if vari[-2:] == 'in':
        if 58 < int(vari[:-2])  < 77:
            counter+=1

    if counter == 5 :
        pure_valid_passports+=1
print(f'no. of valid passports : {pure_valid_passports}')
