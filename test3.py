import threading
balance=0
Local=threading.local()
def pub():
    global balance
    balance = balance + Local.num
    balance = balance - Local.num
def run(num):
    for i in range(1000000):
        Local.num=num
t1=threading.Thread(target=run,args=("5",))
t2=threading.Thread(target=run,args=("3",))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)