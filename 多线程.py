# -*- coding: utf-8 -*-
# Author: 小狼狗

import threading
import time
import queue

SHARE_Q = queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 3   #设置线程个数

class MyThread(threading.Thread) :

    def __init__(self, func, i) :
        super(MyThread, self).__init__()
        self.func = func
        self.thread = i
    #重写run函数
    def run(self) :
        print("{} is running!".format(self.thread))
        self.func()
        print("{} is done!".format(self.thread))

def worker() :
    global SHARE_Q
    while not SHARE_Q.empty():
        item = SHARE_Q.get() #获得任务
        print("Processing : ", item)
        # 引发阻塞
        time.sleep(1)

def main() :
    global SHARE_Q
    threads = []
    for task in range(10) :  #向队列中放入任务
        SHARE_Q.put(task)
    for i in range(_WORKER_THREAD_NUM) :
        thread = MyThread(worker, i)
        #线程准备就绪，等待CPU调度
        thread.start()
        threads.append(thread)
    # 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout
    for thread in threads :
        thread.join()

if __name__ == '__main__':
    main()

