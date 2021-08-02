
import tkinter as tk
import socket
from socket import gethostbyname
import threading


my_ip = gethostbyname(socket.gethostname())
print(my_ip)