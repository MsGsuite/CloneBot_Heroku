<h1 align="center">⚛️ Clonebot with Railway/Qovery Support ⚡<br></h1> 

<br />

<p align="center">CloneBot is a telegram bot that allows you to copy folder/team drive to team drives. One of the main advantage of this bot is that you can host it to Heroku for free.<p/>

<!-- > ## A simple bot to copy and duplicate team drives -->
<p align="center">
  <img src="https://i.imgur.com/QkxmCOp.png" />
</p>

<br />

#### ✅ Advantages
- Use server side copy
- Bypass the 750Gb a day limit thanks to Service accounts
- Duplicate team drive
- Copy public folders & files to team drives
- [Host it to heroku](https://github.com/MsGsuite/CloneBot_Heroku)

#### ❌ Drawbacks
- Does not support files upload (only copy)
- You cannot copy the data to My Drive

Note : there are hidden features, check at the source code of the bot to find them 🙃
<br/><br/>

### ⚠ You need [service accounts (sa)](https://telegra.ph/How-to-create-and-use-service-accounts-sa-03-31) to use the bot
<br/><br/>

## ⚛️ Deploying on Heroku
--> https://github.com/MsGsuite/CloneBot_Heroku
<br/><br/>

## 📱 Run the bot on your phone using termux

--> https://telegra.ph/Clone-Bot-Termux-04-30
<br/><br/>

## 💠 Host the bot on your computer

1. Download the repo : https://github.com/MsGsuite/CloneBot/archive/refs/heads/master.zip
2. Open the config.ini file (inside the telegram_gcloner folder) and fill the following values :


> path_to_gclone =./gclone  ⚠ Don't touch this
>
> telegram_token = go to @BotFather and send /newbot to get one
>
> user_ids = -1 = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)
> 
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> 
> gclone_para_override = leave this empty if you don't know how to use it

3. Install [python](https://www.python.org/downloads/)
4. open CMD and cd to the folder containing the bot
5. run `pip install -r requirements.txt`
6. cd to the telegram_gcloner folder and run : `py telegram_gcloner.py`
7. Start your bot and you can copy your data !
<br/><br/>

## ☂ Deploying on Railway.app

1. For Direct Deploy,Click on the Below Button
 
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Faishik2005%2Fclonebot&envs=group_ids%2Ctelegram_token%2Cgclone_para_override%2Cpath_to_gclone%2Cuser_ids&optionalEnvs=gclone_para_override&group_idsDesc=your+telegram+group+ID+%28leave+it+blank+if+you+don%27t+want+to+add+one%29.+To+get+your+group+id%2C+go+to+%40MissRose_bot+and+type+%2Fid&telegram_tokenDesc=go+to+%40BotFather+and+send+%2Fnewbot+to+get+one&gclone_para_overrideDesc=Dont+fill+any+value+for+this+Var&path_to_gcloneDesc=%E2%9A%A0+Don%27t+touch%2Fchange+this+value.+++++++++++++++++++++++++If+you+see+the+value+empty+then+fill+it+as+%27+.%2Fgclone+%27&user_idsDesc=Your+user+id+%28go+to+%40MissRose_bot+and+type+%2Fid+to+get+your+id%29+-+If+you+want+to+authorize+multiple+users%2C+add+a+comma+between+each+ID+%28ex%3A+150654065%2C5897065%29&referralCode=GD5pqS)

2. Fill the following Environment Values as per below Instructions: 

> path_to_gclone =./gclone  ⚠ Don't touch this
>
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> 
> telegram_token = go to @BotFather and send /newbot to get one
> 
> gclone_para_override = leave this empty if you don't know how to use it
>
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)
> 



3. Click on Deploy

Wait a little bit.You will see that your app has been deployed to Railway and then you can clone without any Time Limit.<b>Railway does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b>

## 🌟 Deploying on Qovery
<p><img src="https://www.eu-startups.com/wp-content/uploads/2021/03/qovery.jpg" alt="Deploy to Railway" /></p>

1.Login to Qovery via Github Account.Fork this Repo.

2.Then create a new Environment followed by new app.Just follow the On-Screen Instructions.

3.Then select Deploy App from Repo and click the Repo in your Account.

4.From settngs of the App scroll down and change Deploy Method from Buildpacks to DockerFile

5.Then go to variables and add the below Environment Variables one by one with proper values.

> path_to_gclone =./gclone  ⚠ Don't touch this
>
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> 
> telegram_token = go to @BotFather and send /newbot to get one
> 
> gclone_para_override = leave this empty if you don't know how to use it
>
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)
> 

6.Then Click Start App. Click Show Logs

Wait a little bit.You will see that your app has been deployed to Qovery and then you can clone without any Time Limit.<b>Qovery does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b>


## 📢 Follow us:
- Google Team Drive Generator : https://td.msgsuite.workers.dev/
- Enterprise Team Drive Generator : https://td.ultraindex.workers.dev/   (Will work only when I open)
- Telegram Channel : https://t.me/MsGsuite
- Telegram Chat : https://t.me/MsGsuiteChat

## ❤️ Credits & thanks :
- [wrenfairbank](https://github.com/wrenfairbank/telegram_gcloner) for the original python script
- [smartass08](https://github.com/smartass08/telegram_gcloner) to adapt the scrip to heroku
- [anymeofu](https://github.com/anymeofu/CloneBot) for making the Direct Heroku deployable Version
- Zero-The-Kamisama to making me discover this amazing bot and the detailed instructions
- [zorgof](https://t.me/zorgof) for the termux script
- [Aishik Tokdar](https://t.me/aishik2005) for Adding Guide to Deploy on Railway.app and Qovery and some other Code Improvements
