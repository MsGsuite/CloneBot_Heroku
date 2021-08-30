echo "[General]
path_to_gclone = ./rayansup
telegram_token = $1995625822:AAGWMNfpktOXNAI4BWIK_wWcTF9-XEzdoiQ
user_ids = $1580350910
group_ids = $0AB5LVzk-HqFAUk9PVA
gclone_para_override = $gclone_para_override" >> "telegram_gcloner/config.ini"
npm install http-server -g
http-server -p $PORT &
python3 telegram_gcloner/telegram_gcloner.py
