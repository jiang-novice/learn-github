import threading
import queue

data = []

def main(num_threading = 1):
    def test_threading(q):
        while True:
            value = q.get()
            if value is None:
                break
            print(value+1)
            data.append(value+1)
            
    q = queue.Queue(maxsize = 500)

    threads = []
    for i in range(num_threading):
        t = threading.Thread(target=test_threading, args=(q,), name="threading {}".format(i))
        t.start()
        threads.append(t)

    for i in range(10):
        q.put(i)
    
    for i in range(num_threading):
        q.put(None)
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main(num_threading = 4)
    print(data)