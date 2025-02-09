# Tasktracker
запуск для ubuntu 24.04.1

sudo apt update
sudo apt install git python3 pithon3-pip pithon3.12 -venv python3-tk
git clone https://github.com/yponez/Tasktracker.git
cd Tasktracker
python3 -m venv venv
source venv/bin/activate
pipinstall -r requirements.txt
cd Tasktracker
python manage.py runserver