import json
import os
from os.path import expanduser
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
app = Flask(__name__)


class Command:
    def __init__(self, name, command):
        self.name = name
        self.command = command


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


# for user's home directory findout or create
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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/commands')
def get_commands():
    res = cmd_read()
    resp = []
    for i in res:
        resp.append({'name': i[0], 'command': i[1]})
    return jsonify(resp)


@app.route('/commands', methods=['POST'])
def create_command():
    body = request.get_json()
    app.logger.debug(body['name'])
    cmd = [body['name'], body['command']]
    arr = cmd_read()
    arr.append(cmd)
    cmd_write(arr)
    return 'Create new command!'


@app.route('/commands/<int:index>', methods=['POST'])
def update_command(index):
    body = request.get_json()
    arr = cmd_read()
    arr[index][0] = body['name']
    arr[index][1] = body['command']
    cmd_write(arr)
    return 'Update command %d' % index


@app.route('/commands/<int:index>', methods=['DELETE'])
def delete_command(index):
    arr = cmd_read()
    if index <= len(arr):
        del arr[index]
        cmd_write(arr)
    else:
        return 'Command not found at index: %d' % index, 404
    return 'Delete command %d' % index


@app.route('/commands/<int:index>/run')
def run_command(index):
    resp = []
    arr = cmd_read()
    resp = {'name': arr[index][0], 'command': arr[index][1]}
    os.system("gnome-terminal -t '" +
              arr[index][0] + "' -- bash -c '" + arr[index][1] + "; exec bash'")
    return jsonify(resp)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
