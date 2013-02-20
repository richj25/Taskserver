import time
import threading

__all__ = ["clientlist"]

class Client:
    def __init__(self,clientName):
        self.clientName = clientName
        self.active = False
        self.failedactivationcommands = 0
        self.tasks = list() 


class Task:
    def __init__(self,taskString):
        self.taskString = taskString
        self.taskId = int(time.time())

class ClientList:
    client_list = list() 
    lock = threading.Lock()

    def synchronize(lock):
        def wrap(f):
            def new_function(*args):
                lock.acquire()
                try:
                    return f(*args)
                finally:
                    lock.release()
            return new_function
        return wrap

    @synchronize(lock)               
    def addclient(self,clientName):
        reply = []
        if self.inlist(clientName) != -1:
            str = "Client '" + clientName + "' is already present in the client list."
            reply.append(str)
        else:
            self.client_list.append(Client(clientName)) 
        return reply

    @synchronize(lock)
    def addtask(self,clientName,taskString):
        reply = []
        if self.inlist(clientName) != -1:
            self.client_list[self.inlist(clientName)].tasks.append(Task(taskString))
        else:
            str = "Client '" + clientName + "' is not present in the client list."
            reply.append(str)
        return reply

    @synchronize(lock)
    def deleteclient(self,clientName):
        reply = []
        if self.inlist(clientName) != -1:
            self.client_list.remove[self.inlist(clientName)]
        else:
            str = "Client '" + clientName + "' is not present in the client list."
            reply.append(str)
        return reply

    @synchronize(lock)
    def deletetask(self,taskId):
        reply = []
        found = False
        for client in self.client_list:
            for idx, task in enumerate(client.tasks):
                if taskId == str(task.taskId): 
                    client.tasks.remove[idx]
                    found = True
        if not found:
            reply.append("Task not found")
        return reply

    @synchronize(lock)
    def listclients(self):
        reply = []
        header = "Client name"
        reply.append(header)
        for client in self.client_list:
            reply.append(client.clientName)
        return reply

    @synchronize(lock)
    def listtasks(self):
        reply = []
        header = "Client name              TaskID                   Task string"
        reply.append(header)
        for client in self.client_list:
            for task in client.tasks:
                entry = '{0:<24} {1:<24} {2:<24} '.format(client.clientName,str(task.taskId),task.taskString)
                reply.append(entry)
        return reply

    @synchronize(lock)
    def gettask(self,clientName):
        for client in self.client_list:
            if re.match(clientName,client.clientName):
                if client.tasks.length() != 0:
                    return client.tasks.pop[0].taskString
                else:
                    return "No task"
        return "No client"
     
    def inlist(self,clientName):
        for idx, elem in enumerate(self.client_list):
           if clientName == elem.clientName: return idx
        return -1
       

clientlist = ClientList()
        
