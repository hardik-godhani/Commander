from flask import Flask
from flask import render_template
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/commands')
def get_commands():
    return jsonify([
        {'name': 'Sonaar panel', 'command': 'ng s -o'},
        {'name': 'Portfolio panel', 'command': 'ng s -o'},
    ])


@app.route('/commands', methods=['POST'])
def create_command():
    return 'Create new command!'


@app.route('/commands/<int:index>', methods=['POST'])
def update_command(index):
    return 'Update command %d' % index


@app.route('/commands/<int:index>', methods=['DELETE'])
def delete_command(index):
    return 'Delete command %d' % index


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
