# Installation steps To use Commander
> Utilites Installation
1) For installing python 3 use this link "https://www.python.org/"
2) If you’re using Python 3.4 (or greater), then PIP comes installed with Python by default. or you have install pip via

    Windows
    1) For download the "get-pip.py" installer script "https://bootstrap.pypa.io/get-pip.py". Now right-click on the link and select Save As… and save it to any safe location, such as your Downloads folder.
    2) Open the Command Prompt and navigate to the get-pip.py file.
    3) Run the following command: "python get-pip.py"

    Mac
    + Run following command in Terminal "sudo easy_install pip"

    Linux / Unix
     + Run one of the following command in Terminal as you use package manager in your system.
        1) Advance "sudo apt-get install python3-pip"
        2) Pacman "sudo pacman -S python-pip"
        3) Yum "sudo yum install python3 python3-wheel"
        4) Dandified "sudo dnf install python3 python3-wheel"
        5) Zypper "sudo zypper install python3-pip python3-setuptools python3-wheel"
3) Now Install local environment with this code "sudo pip3 install virtualenv"

> Steps to install

1) go to Commander Directory
2) run this code "sudo virtualenv env" and you can see a vnev folder created in commander.
3) run this code "source env/bin/activate"
4) run this code "sudo pip3 install -r requirements.txt" and reopen terminal

Now just run "python3 main.py" in Commander folder and enjoy.
