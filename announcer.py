import socket
import subprocess
import time
#Announcer to know details about the devices that runs an announce to a server
server = '127.0.0.1'
port = 2882


class Announcer:
    """Announcer"""
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        while True:
            try:
                self.sock.connect((server, port))
            except ConnectionRefusedError:
                time.sleep(5)
                continue
            break
        message = subprocess.check_output(["ip", "addr"])
        sent_total = 0
        message_length = len(message)
        while sent_total < message_length:
            sent = self.sock.send(message[sent_total:])
            if sent == 0:
                raise RuntimeError("Socket borked dude")
            sent_total = sent_total + sent
        self.sock.close()
if __name__ == '__main__':
    nouncer = Announcer()
    nouncer.send()
