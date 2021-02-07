input_=open('day5.txt')
data=list(map(lambda x:x.replace('\n',''),input_))
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
highest_seat=0
for i in data:
    x=decode(i[:7],0,127,['F','B'])
    y=decode(i[7:],0,7,['L','R'])
    seat_num=(x*8)+y
    if seat_num>highest_seat:
        highest_seat=seat_num
print(f'The highest seat number : {highest_seat}')