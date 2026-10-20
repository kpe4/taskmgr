import multiprocessing as mp
import os

def worker():
    print(f"PID: {os.getpid()}")
    print(f"PPID: {os.getppid()}")
def workers(name):
    print(f"Процесс {name}, PID: {os.getpid()}")
    print(f"Процесс {name}, PPID: {os.getppid()}")

if __name__ == "__main__":
    print(f"Главный процесс, PID: {os.getpid()}")


    for i in range(4):
        p = mp.Process(worker())
        a = mp.Process(target=workers, args=(i,))
        a.start()
        a.join()
        p.start()
        p.join()