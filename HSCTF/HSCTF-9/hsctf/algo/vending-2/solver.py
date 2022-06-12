from pwn import *
import random
import copy

# A Python program to count all subsets with given sum.
 
# dp[i][j] is going to store True if sum j is
# possible with array elements from 0 to i.
dp = [[]]
 
found = None
def display(v):
	print(v)
 
# A recursive function to print all subsets with the
# help of dp[][]. list p[] stores current subset.
def printSubsetsRec(arr, i, sum, p):
	global found
	if found:
		return
   
	# If we reached end and sum is non-zero. We print
	# p[] only if arr[0] is equal to sum OR dp[0][sum]
	# is True.
	if (i == 0 and sum != 0 and dp[0][sum]):
		p.append(arr[i])
		found = copy.deepcopy(p)
		return
 
	# If sum becomes 0
	if (i == 0 and sum == 0):
		found = copy.deepcopy(p)
		p = []
		return
 
	# If given sum can be achieved after ignoring
	# current element.
	if (dp[i-1][sum]):
		# Create a new list to store path
		b = []
		b.extend(p)
		printSubsetsRec(arr, i-1, sum, b)
 
	# If given sum can be achieved after considering
	# current element.
	if (sum >= arr[i] and dp[i-1][sum-arr[i]]):
		p.append(arr[i])
		printSubsetsRec(arr, i-1, sum-arr[i], p)
 
# Prints all subsets of arr[0..n-1] with sum 0.
def printAllSubsets(arr, n, sum):
	if (n == 0 or sum < 0):
		return
 
	# Sum 0 can always be achieved with 0 elements
	global dp
	dp = [[False for i in range(sum+1)] for j in range(n)]
 
	for i in range(n):
		dp[i][0] = True
 
	# Sum arr[0] can be achieved with single element
	if (arr[0] <= sum):
		dp[0][arr[0]] = True
 
	# Fill rest of the entries in dp[][]
	for i in range(1, n):
		for j in range(0, sum + 1):
			if (arr[i] <= j):
				dp[i][j] = (dp[i-1][j] or dp[i-1][j-arr[i]])
			else:
				dp[i][j] = dp[i - 1][j]
 
	if (dp[n-1][sum] == False):
		return
 
	# Now recursively traverse dp[][] to find all
	# paths from dp[n-1][sum]
	p = []
	printSubsetsRec(arr, n-1, sum, p)

# r = remote('35.204.95.14', 1337)
# res = r.recv()
# print(res)
# r.sendline(input())
# for oo in range(12):
# 	found = None
# 	r.sendline('Display')
# 	res = r.recvuntil('Balance')
# 	print(res)
# 	items = []
# 	res = res.decode()
# 	items_string = res.split('Coins')[0]
# 	items_string = items_string.split('Items:')[1]
# 	for item in items_string.split('\n'):
# 		item = item.strip()
# 		if item == '' or not item or item == 'Items:':
# 			continue
# 		items.append(int(item.split(':')[1][1:]))

# 	coins = []
# 	coins_string = res.split('Coins:')[1]
# 	for coin in coins_string.split('\n'):
# 		coin = coin.strip()
# 		if coin == '' or not coin or coin == 'Balance':
# 			continue
# 		coins.append(int(coin.split(':')[1][1:]))

items = [132745, 180450, 88392, 179516, 189718, 190662, 141437, 185084, 177853, 193465, 173266, 134932, 185942, 134843, 89441, 184516, 169621, 129556, 130662, 175899, 186122, 139124, 173044, 180963, 175225, 185458, 138986, 182507, 87901, 172653, 139826, 188523, 173033, 191197, 125222, 187322, 180783, 187656, 171401, 139742, 139074, 125107, 173910, 186467, 176589, 131436, 180785, 132611, 132481, 187275, 187534, 181966, 176847, 87334, 176531, 165071]
coins = [41062, 49053, 42918, 45362, 48566, 49731, 47719, 44790, 45867, 49873, 47315, 47058, 46373, 43074, 41881, 45863, 45466, 49703, 49162, 46737, 49856, 41852, 49450, 49010, 47669, 41660, 48796, 41320, 42798, 41370, 42643, 47809, 43797, 48595, 47053, 45459, 41281, 42684, 42841, 49857, 45960, 41267, 49635, 41880, 47433, 45907, 45425, 42802, 42261, 44787, 43861, 40477, 49149, 43254, 45740, 48905, 45120, 48512, 45929, 47084, 49584, 45054, 49546, 43922, 49296, 44068, 45459, 42243, 41028, 42194, 46113, 48985, 45537, 49252, 40336, 46422, 44233, 48643, 45003, 44309, 49482, 48164, 42947, 49734, 47414, 46178, 42574, 42349, 48141, 45102, 45645, 40689, 44555, 49676, 45753, 43934, 46194, 42555, 42031, 44096, 43876, 49978, 44029, 42269, 45947, 42222, 41681, 40680, 47601, 41253, 47865, 42475, 45889, 41763, 42018, 40891, 43366, 48044, 40937, 40558, 46386, 40989, 49896, 44171, 40006, 42020, 40060, 48761, 49128, 40249, 40685, 46653, 47174, 48836, 41322, 47694, 42254, 43890, 44990, 44071, 48854, 41002, 46464, 45075, 42474, 48431, 41343, 47224, 49867, 44297, 43149, 40647, 48111, 47495, 49728, 40507, 49392, 47626, 45657, 49307, 47417, 45859, 47376, 40227, 49860, 40269, 45739, 43672, 42392, 45857, 41882, 45461, 48185, 42724, 41560, 44159, 45734, 40793, 40419, 42852, 42881, 49962, 42717, 47376, 44038, 47651, 49993, 42154, 42911, 40759, 41448, 40188, 42601, 47145, 43930, 49241, 42118, 48193, 42351, 49342]

print(items)
print(coins)
diff = sum(coins) - sum(items)
print("Maximum :: ", diff)

fake_coins = copy.deepcopy(coins)
fake_coins = sorted(fake_coins)[::-1]

fake_items = copy.deepcopy(items)

res = {}

# first find perfects

sorted_items = sorted(fake_items)[::-1]
for j in range(0, 150):
	for i in range(49):
		item = sorted_items[i]
		if item in res:
			continue
		print("Solving item : ", item)
		printAllSubsets(fake_coins, len(fake_coins), item + j)
		if found:
			diff -= j
			print(item, j, found, len(res), "diff ::", diff)
			res[item] = found
			for f in found:
				del fake_coins[fake_coins.index(f)]
			del fake_items[fake_items.index(item)]
			found = None

print('Remain items :: ', fake_items)
print('Remain coins :: ', fake_coins)

for o in range(100000):
	candidate_res = {}
	random.shuffle(fake_coins)
	arr = []
	cnt = 0
	for i in range(len(fake_coins)):
		if sum(arr) < fake_items[cnt]:
			arr.append(fake_coins[i])
		else:
			candidate_res[fake_items[cnt]] = arr
			arr = [fake_coins[i]]
			cnt += 1
	abs_diff = 0
	candidate_res[fake_items[6]] = arr
	if len(candidate_res) < 7 or sum(candidate_res[fake_items[6]]) < fake_items[6]:
		continue
	
	res |= candidate_res
	break

print(res)
print(fake_coins)

for o in range(56):
	for coin in res[items[i]]:
		insert_string = f'Insert {coins.index(coin) + 1}'
		print(insert_string)
		r.sendline(insert_string)
		ans = r.recv()
		print(ans)
	buy_string = f'Buy {o + 1}'
	r.sendline(buy_string)
	print(buy_string)
	ans = r.recv()
	print(ans)

ans = r.recv()
print(ans)

# ans = r.recv()
# print(ans)
# for i in range(6):
#     print(items[i])
#     for j in range(len(res[i])):
#         print(f"Insert {coins.index(res[i][j]) + 1}")
#     print(f"Buy {i + 1}")
# 54584 [19462, 18999, 16313] 54774
# 46149 [16083, 14828, 9077, 6008] 45996
# 34957 [12388, 11797, 11382] 35567
# 32092 [6852, 6739, 8324, 10363] 32278
# 27405 [13621, 13934] 27555
# 23718 [10809, 9799 , 5607] 26215
