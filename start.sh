echo "$general" >> "telegram_gcloner/config.ini"
echo "$path" >> "telegram_gcloner/config.ini"
echo "$telegram_token" >> "telegram_gcloner/config.ini"
echo "$user_ids" >> "telegram_gcloner/config.ini"
echo "$group_ids" >> "telegram_gcloner/config.ini"
echo "$gclone_para_override" >> "telegram_gcloner/config.ini"
npm install http-server -g
http-server -p $PORT &
python3 telegram_gcloner/telegram_gcloner.py
