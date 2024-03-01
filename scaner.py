import sys
import socket
import threading
from queue import Queue

from util import myscan

if len(sys.argv) == 4:
    try:
        target = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort = int(sys.argv[3])
    except(ValueError):
        print("Неверный формат номера портов")
        sys.exit(400)
    try:
        t_IP = socket.gethostbyname(target)
    except(Exception):
        print("Неверный формат ввода IP")
        sys.exit(400)
    print(target, startPort, endPort)
else:
    print("Формат запуска: Python scaner.py <IP адрес в формате 3.4.5.6(согласно стандарту)> <стартовое значение диапазона портов для сканирования> <конечное значение диапазона для сканирования>")
    sys.exit(400)

scan = myscan(t_IP, startPort, endPort)
scan.mainScan()
