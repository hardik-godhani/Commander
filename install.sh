echo "Starting commander installation..."
{
    pip3 --version &&
    echo "pip3 already installed"
    } || {
    echo "install pip3 first"
    return
}
{
    virtualenv --version &&
    echo "virtualenv is already installed."
    } || {
    sudo pip3 install virtualenv
}
virtualenv env
source env/bin/activate
# pip install tabulate
pip3 install -r requirements.txt
deactivate
echo "Commander installation complete! You can now run it with './commander.sh' command"
./commander.sh