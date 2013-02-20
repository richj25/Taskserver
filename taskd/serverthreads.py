import threading
import socket
import time
import globaldefines
import clientlist
import flags
from netutils import *

__all__ = ["ClientManagerThread","TaskServerThread"]

class ClientManagerThread(threading.Thread):
    def run(self):
        print "ClientManagerThread running"
        while not flags.shutdown:
            for client in clientlist.clientlist.client_list:
                if client.active == False:
                    if self.activate_client(client.clientName) == "Success":
                        client.active = True
                        client.failedactivationcommands = 0
                    else:
                        client.failedactivationcommands += 1
            time.sleep(1.0)

    def activate_client(self,clientName):
        fqdn = socket.getfqdn(clientName)
        HOST, PORT = fqdn, globaldefines.COMMAND_PORT
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST,PORT))
            time.sleep(15)
            sock.send("Activate")
            line = receive(sock,"No reply from task client")
            if line != fqdn: 
                raise NameMismatchError("Task client name mismatch: Should be " + clientName + " received " + line) 
            sock.send(socket.gethostname())
            line = receive(sock,"No reply from task client")
            if line == "Activated":
                retval =  "Success"

        except (TimeoutError,NameMismatchError) as message:
            print message
            retval =  "Failure"
        except socket.error as (value,message):
            if sock: 
                sock.close()            
            retval =  "Failure"
        finally:
            sock.close()
            return retval


