import select

class NameMismatchError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

class TimeoutError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

def receive(sock,message):
    sock.setblocking(0)
    ready = select.select([sock],[],[],5.0)
    if ready[0]:
        return sock.recv(1024)
    else:
        raise TimeoutError(message)
