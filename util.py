import threading
from queue import Queue
import socket

class myscan:
    def __init__(self, t_IP, startPort, endPort):
        self.t_IP = t_IP
        self.startPort = startPort
        self.endPort = endPort

    def mainScan(self):
        #можно понизить число для роста скорости или повысить для гарантии работы с большим пингом
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()
        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((self.t_IP, port))
                with print_lock:
                    print(port, 'is open')
                con.close()
            except:
                pass


        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()


        q = Queue()

        for x in range(4096):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(self.startPort, self.endPort):
            q.put(worker)

        q.join()
