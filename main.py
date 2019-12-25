#!/env/bin/python
import readline
from os.path import expanduser
from tabulate import tabulate
import json
import os


# for user's home directory findout
home = expanduser('~')
commandTxt = home + "/.config/commander/command.txt"
currentDir = os.getcwd()

try:
    z = open(commandTxt, "a+")
    # os.mkdir(home + "/.config/commander")
except:
    os.mkdir(home + "/.config/commander")
    z = open(commandTxt, "a+")
z.close()


def runCommand(i):
    arr = cmd_read()
    if i <= len(arr):
        os.system("gnome-terminal -- bash -c '" + arr[i][1] + "; exec bash'")
    else:
        print("No command found at this position. check for available commands by using 'list'.")


def createCommand(x):
    y = input("Enter Command: ")
    cmd = [x, y]
    arr = cmd_read()
    arr.append(cmd)
    cmd_write(arr)
    print("Command Added Successfully")


def deleteCommand(id):
    arr = cmd_read()
    if id <= len(arr):
        del arr[id]
        cmd_write(arr)
        print("Command Deleted Successfully")
    else:
        print("No command found at this position. check for available commands by using 'list'.")


def helpShow():
    print('''
    Help menu
    run <id> : run the command at given id in new terminal
    add <name> : add the command name and after this enter command
    delete <id> : delete the command at given id
    list : Show all commands in a table with id
    help : shows Help menu  ''')


def showCommand():
    r = open(commandTxt, "r")
    hasdd = r.read()
    if hasdd != '':
        print("         Commands")
        print(tabulate(json.loads(hasdd), headers=[
              'Id', 'Name', 'Command'], tablefmt='presto', showindex='always', numalign="right"))
    else:
        print("No commands found. use 'help' for adding a new commands.")
    r.close()


def cmd_write(li):
    a = open(commandTxt, "w+")
    cmd_list = json.dumps(li)
    a.write(cmd_list)
    a.close()


def cmd_read():
    r = open(commandTxt, "r")
    data = r.read()
    if len(data) == 0:
        return []
    else:
        return json.loads(data)
    r.close()


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele + ' '
    return str1


def switcher(cmd):
    cd = cmd.split(' ')
    if cmd.startswith("run "):
        if cd[1].isnumeric():
            runCommand(int(cd[1]))
        else:
            print("Invalid Command")
    elif cmd.startswith("delete "):
        if cd[1].isnumeric():
            deleteCommand(int(cd[1]))
        else:
            print("Invalid Command")
    elif cmd.startswith("add "):
        if len(cd) == 2:
            createCommand(cd[1])
        else:
            del cd[0]
            createCommand(listToString(cd))
    elif cmd == "list":
        showCommand()
    elif cmd == "help":
        helpShow()
    else:
        print("Invalid Command")


# for continous process
while True:
    print("\n Welcome to Commander")
    inp = input(">")
    if inp == 'exit':
        break
    else:
        switcher(inp)
