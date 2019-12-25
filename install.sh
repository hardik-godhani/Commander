echo "Commander Installation started..."
{
    pip3 --version &&
    echo "pip3 already Installed"
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
echo "Commander Installed now you can also run it with './commander.sh'"
./commander.sh