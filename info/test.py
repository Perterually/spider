import pymysql

def random_li():
    li = []
    for i in range(0, 1000000):
        li.append(i)
    del li[100000]
    return li




def brute_force(li):
    i = 0
    while True:
        if i not in li:
            return i
        i += 1

