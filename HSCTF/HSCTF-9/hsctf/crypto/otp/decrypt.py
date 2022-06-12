import random
from Crypto.Util.number import bytes_to_long, long_to_bytes

def secure_seed():
	x = 0
	d = dict()
	# x is a random integer between 0 and 100000000000
	for i in range(100000000):
		x = random.randint(0, random.randint(0, 10))
		if x in d:
			d[x] += 1
		else:
			d[x] = 1
	
	print(d)
	return 0

# generated with secure_seed for 10**8 and then 100x
nums = {0: 2746269100, 1: 1836258200, 6: 518068300, 3: 1078472600, 2: 1381439700, 4: 851457900, 5: 669404400, 9: 173505200, 8: 274492300, 7: 388027300, 10: 82605000}

res = 0
for x, y in nums.items():
    res += x * y

print(res)
for i in range(res - 10**6, res + 10**7):
    random.seed(i)

    flag = 444466166004822947723119817789495250410386698442581656332222628158680136313528100177866881816893557
    l = 328
    k = random.getrandbits(l)
    flag = flag ^ k

    try:
        flag = long_to_bytes(flag).decode()
    except:
        continue
    
    if 'flag' in flag:
        print(flag)
        break
# flag :: flag{c3ntr4l_l1m1t_th30r3m_15431008597}