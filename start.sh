echo "Cloning Repo...."
git clone https://github.com/KR-BOTZ/rent-bot3 /rent-bot3
cd /rent-bot3
pip3 install -U -r requirements.txt
echo "Starting Bot.... "
python3 bot.py
