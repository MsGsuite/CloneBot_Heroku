<h1 align="center">⚛️ Clonebot with Heroku/Railway/Qovery Support ⚡<br></h1> 

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
- [Host it to Heroku](https://github.com/MsGsuite/CloneBot_Heroku#%EF%B8%8F-deploying-on-heroku)
- [Host it to Railway]
- [Host it to Qovery]

#### ❌ Drawbacks
- Does not support files upload (only copy)
- You cannot copy the data to My Drive

Note : there are hidden features, check at the source code of the bot to find them 🙃

Update : I have listed most of the hidden features in Telegram_Bot_Commands.txt in the root of this Repo

<br/>

### ⚠ You need [service accounts (sa)](https://telegra.ph/How-to-create-and-use-service-accounts-sa-03-31) to use the bot
<br/><br/>

## 💠 Host the bot on your Local PC

--> https://github.com/MsGsuite/CloneBot
<br/><br/>

## 📱 Run the bot on your phone using Termux

--> https://telegra.ph/Clone-Bot-Termux-04-30
<br/><br/>

## ⚛️ Deploying on Heroku

 [🎬 Click me for the video tutorial](https://drive.google.com/file/d/1HniSEGUOptbZmHVXuOPULnzpyBBhgw3l/view?usp=sharing)
 
1. Click on the button below :
<p><a href="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2F&template=https://github.com/msgsuite/clonebot_heroku"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" alt="Deploy to Heroku" /></a></p>


2. Fill the following values : 

> gclone_para_override = leave this blank is you don't know how to use it
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> telegram_token = go to @BotFather and send /newbot to get on
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

3. Click on Deploy app...
4. When it's over, go to : https://dashboard.heroku.com/apps/YOURAPPNAME/resources (replace YOURAPPNAME by your appname 🙃)
5. Then click on the ✏ and check $0.00 option and click on confirm.
6. Now you can start your bot !
<br/><br/>

## ☂ Deploying on Railway.app

1. For Direct Deploy,Click on the Below Button
<p><a href="https://railway.app/new/template?template=https://github.com/aishik2005/CloneBot&envs=telegram_token,user_ids,group_ids"><img src="https://img.shields.io/badge/Deploy%20To%20Railway-black?style=for-the-badge&logo=railway" alt="Deploy to Railway" /></a></p>


2. Fill the following Environment Values as per below Instructions: 

> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> telegram_token = go to @BotFather and send /newbot to get one
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

3. Click on Deploy

Wait a little bit.You will see that your app has been deployed to Railway and then you can clone without any Time Limit.<b>Railway does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b>

## 🌟 Deploying on Qovery
<p><img src="https://www.eu-startups.com/wp-content/uploads/2021/03/qovery.jpg" alt="Deploy to Railway" /></p>

1.Login to Qovery via Github Account.Fork this Repo.

2.Then create a new Environment followed by new app.Just follow the On-Screen Instructions.

3.Then select Deploy App from Repo and click the Repo in your Account.

4.From settngs of the App scroll down and change Deploy Method from Buildpacks to DockerFile

5.Then go to variables and add the below Environment Variables one by one with proper values.

> gclone_para_override = leave this blank is you don't know how to use it
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> telegram_token = go to @BotFather and send /newbot to get on
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

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
- [Aishik Tokdar](https://t.me/aishik2005) for Adding Guide to Deploy on Railway.app and Qovery and some othr Code Improvements
