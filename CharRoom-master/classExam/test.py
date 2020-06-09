import queue
class msg:
    def __init__(self):
        pass;
if __name__ == "__main__":
    queueList = queue.Queue(maxsize=5)
    queueList.put(str("a"))
    print(type(queueList.get()))