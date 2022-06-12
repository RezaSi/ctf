from pwn import *

r = remote('hacking.hsctf.com', 1337)
res = r.recv()
print(res)
r.sendline(input())

adj = []
mark = dict()

def dfs(node, virus_starter):
    mark[(node, virus_starter)] = True
    for u in adj[node]:
        if (u, virus_starter) not in mark:
            dfs(u, virus_starter)


all_hacks = []
for i in range(6):
    arr = r.recvline().decode()
    all_hacks.append(arr.split(','))

with open('out.txt', 'w') as f:
    for item in all_hacks:
        f.write("%s\n" % item)
