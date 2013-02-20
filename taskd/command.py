import clientlist

__all__ = ["execute_command"]

class CommandProcessor:
    @classmethod
    def execute_command(self,command,type,taskString,taskId,clientName):
        if command == 'list':
            return self.list_command(type)
        if command == 'add':
            return self.add_command(type,clientName,taskString)
        if command == 'delete':
            return self.delete_command(type,clientName,taskId)

    @classmethod
    def list_command(self,type):
        if type == 'clients': return clientlist.clientlist.listclients()
        if type == 'tasks': return clientlist.clientlist.listtasks()

    @classmethod
    def add_command(self,type,clientName,taskString):
        if type == 'client': return clientlist.clientlist.addclient(clientName)
        if type == 'task': return clientlist.clientlist.addtask(clientName,taskString)

    @classmethod
    def delete_command(self,type,clientName,taskId):
        if type == 'client': return clientlist.clientlist.deleteclient(clientName)
        if type == 'task': return clientlist.clientlist.deletetask(taskId)
