import argparse

__all__ = ["parseargs"]

def parseargs():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    #
    #Parse the 'list' command
    #
    list = subparsers.add_parser('list')
    list.set_defaults(command='list')
    list.add_argument('type',choices=['tasks','clients'])

    #
    #Parse the 'add' command
    #
    add = subparsers.add_parser('add')
    add.set_defaults(command='add')
    add_subparsers = add.add_subparsers()

    add_task = add_subparsers.add_parser('task')
    add_task.set_defaults(type='task')
    add_task.add_argument('taskString')
    add_task.add_argument('clientName')

    add_client = add_subparsers.add_parser('client')
    add_client.set_defaults(type='client')
    add_client.add_argument('clientName')

    #
    #Parse the 'delete' command
    #
    delete = subparsers.add_parser('delete')
    delete.set_defaults(command='delete')
    delete_subparsers = delete.add_subparsers()
  
    delete_task = delete_subparsers.add_parser('task')
    delete_task.set_defaults(type='task')
    delete_task.add_argument('taskId', type=int)

    delete_client = delete_subparsers.add_parser('client')
    delete_client.set_defaults(type='client')
    delete_client.add_argument('clientName')

    args = parser.parse_args()

    if 'taskString' in args:
        taskString = args.taskString
    else:
        taskString = None

    if 'taskId' in args:
        taskId = args.taskId
    else:
        taskId = None

    if 'clientName' in args:
        clientName = args.clientName
    else:
        clientName = None

    return (args.command,args.type,taskString,taskId,clientName)
