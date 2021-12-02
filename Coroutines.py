from gevent import monkey
import gevent
import time
monkey.patch_all()


def coroutine_print(block):
    for i in block:
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    item_list = [i for i in range(0, 256)]
    step = 32
    jobs = []
    for i in range(0, len(item_list), step):
        block = item_list[i: i + step]
        jobs.append(gevent.spawn(coroutine_print, block))
    gevent.joinall(jobs)