from ast import literal_eval
from pwn import *

r = remote('travelling-salesman.hsctf.com', 1337)
res = r.recv()

while True:
    res = r.recv(1024)
    if '[' not in res.decode():
        res = r.recv(1024)
    print('res', res)
    res = res.decode()
    arr = literal_eval(res.split('\n')[0])
    arr = sorted(arr)
    string_arr = ' '.join(map(str, arr))
    print(string_arr)
    r.sendline(string_arr)