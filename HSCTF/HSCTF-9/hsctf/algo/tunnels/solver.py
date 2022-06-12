from pwn import *
import random
import copy
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # seq = [2, 2, 3, 4, 5, 5, 6, 7]
    cnt_all, cnt_true = 0, 0
    status = True

    r = remote('tunnels.hsctf.com', 1337)

    for o in range(200):
        if not status:
            break
        flag = False
        for i in range(8):
            n = random.randint(1, 8)
            r.sendline(str(n))
            res = r.recv()
            res = res.decode()
            if 'correct' in res and 'incorrect' not in res:
                print(f"connection {name} ::: step {o + 1} ::: guess {n}")
                flag = True
                break     
                
        cnt_all += 1
        if flag:
            cnt_true += 1
        # print("Solved ? ", flag)
        print(f"Connection {name} :: solved {cnt_true} from {cnt_all}")
        if (cnt_all - cnt_true) > 15:
            status = False
    res = r.recv()
    print(res)
    res = r.recv()
    print(res)

NUMBER_OF_CONNECTIONS = 50

# seq = [2, 2, 4, 4, 5, 5, 7, 7] 80%
# seq = [2, 3, 4, 4, 5, 5, 6, 7] 65%
# seq = [2, 3, 4, 4, 5, 6, 7, 8] 80%
# seq = [2, 2, 3, 4, 5, 5, 6, 7] 80%
# seq = [2, 2, 3, 4, 5, 6, 7, 7]

threads = list()
for index in range(NUMBER_OF_CONNECTIONS):
    logging.info("Main    : create and start thread %d.", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()
    logging.info("Main    : thread %d done", index)

for j in range(NUMBER_OF_CONNECTIONS):
    res = r[j].recv()
    print(res)
    res = r[j].recv()
    print(res)