input_=open('day5.txt')
data=list(map(lambda x:x.replace('\n',''),input_))
seat_nums=[]
def decode(row, low, high, terms):
    for i in row:
        mid = low + (high - low) // 2

        if high - low == 1 :
            if i == terms[0]:
                return int(low)
            if i == terms[1]:
                return int(high)
        if i == terms[0]:
            high = mid
        if i == terms[1]:
            low=mid+1

for i in data:
    x=decode(i[:7],0,127,['F','B'])
    y=decode(i[7:],0,7,['L','R'])
    seat_num=(x*8)+y
    seat_nums.append(seat_num)

seat_nums.sort()
j=seat_nums[0]-1
for i in range(len(seat_nums)):
    j+=1
    if seat_nums[i]!=j:
        break

print(f'My seat number : {j}')
print(seat_nums)