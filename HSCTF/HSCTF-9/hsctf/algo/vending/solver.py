from pwn import *
import random
import copy

r = remote('vending-machine.hsctf.com', 1337)
res = r.recv()
r.sendline('Display')
res = r.recvuntil('Balance')
print(res)

items = []
res = res.decode()
items_string = res.split('Coins')[0]
for item in items_string.split('\n'):
    item = item.strip()
    if item == '' or not item or item == 'Items:':
        continue
    items.append(int(item.split(':')[1][1:]))

coins = []
coins_string = res.split('Coins:')[1]
for coin in coins_string.split('\n'):
    coin = coin.strip()
    if coin == '' or not coin or coin == 'Balance':
        continue
    coins.append(int(coin.split(':')[1][1:]))

print(items)
print(coins)

fake_coins = copy.deepcopy(coins)

res = []

for o in range(100000):
    candidate_res = []
    random.shuffle(fake_coins)
    arr = []
    cnt = 0
    for i in range(len(fake_coins)):
        if sum(arr) < items[cnt]:
            arr.append(fake_coins[i])
        else:
            candidate_res.append(arr)
            arr = [fake_coins[i]]
            cnt += 1
    abs_diff = 0
    candidate_res.append(arr)
    if len(candidate_res) < 6 or sum(candidate_res[5]) < items[5]:
        continue
    
    res = candidate_res
    break

print(res)

for o in range(6):
    for coin in res[o]:
        insert_string = f'Insert {coins.index(coin) + 1}'
        print(insert_string)
        r.sendline(insert_string)
        ans = r.recv()
        print(ans)
    buy_string = f'Buy {o + 1}'
    r.sendline(buy_string)
    print()
    ans = r.recv()
    print(ans)

ans = r.recv()
print(ans)
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
