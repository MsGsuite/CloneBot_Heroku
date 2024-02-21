<h1 align="center">✪ CloneBot - Heroku/Railway/Qovery/Clever-Cloud/Scalingo/Okteto Version ❅<br></h1> 

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
- [Host it to Railway](https://railway.app)
- [Host it to Qovery](https://www.qovery.com/)
- [Host it to Clever-Cloud](https://www.clever-cloud.com)
- [Host it to Scalingo](https://scalingo.com)
- [Host it to Heroku](https://www.heroku.com)
- [Host it to Okteto](https://www.okteto.com)

#### ❌ Drawbacks
- Does not support files upload (only copy)
- You cannot copy the data to My Drive

Note : there are hidden features, check at the source code of the bot to find them 🙃

<br/>

### ⚠ You need [service accounts (sa)](https://telegra.ph/How-to-create-and-use-service-accounts-sa-03-31) to use the bot
<br/><br/>

## 💠 Host the bot on your computer

--> https://github.com/MsGsuite/CloneBot
<br/><br/>

## 📱 Run the bot on your phone using termux

--> https://telegra.ph/Clone-Bot-Termux-04-30
<br/><br/>

## ⚛️ Deploying on Heroku

https://www.heroku.com/deploy

[![Deploy](https://telegra.ph/file/e7d224c45cf1d106a28fa.png)](Heroku_Deployment.md)



𝙈𝙚𝙩𝙝𝙤𝙙 - 2 : ᴠɪᴀ ᴇᴅɪᴛɪɴɢ ʀᴇᴘᴏ ɴᴀᴍᴇ ᴀɴᴅ ʟɪɴᴋ

[![Deploy](https://telegra.ph/file/e7d224c45cf1d106a28fa.png)](https://telegra.ph/Temporary-Heroku-Deployment-Method-for-MSGuite-CloneBot-11-23)



## ☂ Deploying on Railway.app

1. For Direct Deploy,Click on the Below Button<br/>
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
4. Wait a little bit.You will see that your app has been deployed to Railway and then you can clone without any Time Limit.<b>Railway does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b><br/><br/>

## 🌟 Deploying on Qovery

<b>This Method does not work anymore as Qovery has stopped Open Signup</b>

<img src="https://i.imgur.com/VT7bQZb.png" alt="Deploy to Qovery"/>

𝐒𝐓𝐄𝐏𝐒-
<BR>
1. Login to Qovery via Github Account.Fork this Repo.
2. Then create a new Environment followed by new app.Just follow the On-Screen Instructions.
3. Then select Deploy App from Repo and click the Repo in your Account.
4. From settngs of the App scroll down and change Deploy Method from Buildpacks to DockerFile
5. Then go to variables and add the below Environment Variables one by one with proper values.
> path_to_gclone =./gclone  ⚠ Don't touch this
>
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> 
> telegram_token = go to @BotFather and send /newbot to get one
> 
> gclone_para_override = leave this empty if you don't know how to use it
>
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

6. Wait a little bit.You will see that your app has been deployed to Qovery and then you can clone without any Time Limit.<b><br/>Qovery does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b><br><br>

## 💎 Deploying on Clever-Cloud

<a href="https://bit.ly/CloneBot_CleverCloud"><img src="https://img.shields.io/badge/Clever%20Cloud%20Deploy%20Guide-grey?style=for-the-badge&logo=telegraph"></a>

<br>This Service provides enough resources so that the Bot can run for 40 days without the need to add CC.<b><br/>Clever Cloud does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b><br><br>

<br>Thanks to [Katarina](https://github.com/tiararosebiezetta) for the addition of this Service.

## 🗡️ Deploying on Scalingo

[![Deploy](https://cdn.scalingo.com/deploy/button.svg)](https://dashboard.scalingo.com/create/app?source=https://github.com/tiararosebiezetta/CloneBot_Scalingo)

<br>This Service provides enough resources so that the Bot can run for 30 days without the need to add CC.<b><br/>Scalingo does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b><br><br>

<br>Thanks to [Katarina](https://github.com/tiararosebiezetta) for the addition of this Service.

## 💫 Deploying on Okteto

For quick use, use this repo directly and deploy it to Okteto Cloud. Customize docker-compose.yml as you want if needed.

You need to fillup the below variables in order to use it in Okteto 

> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
> 
> telegram_token = go to @BotFather and send /newbot to get one
> 
> PORT = Add PORT as an environmental variable, and add 8080. Use Cron Job to ping the App every 30 mins else the bot will sleep
>
> user_ids = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

<br>This Service is like Heroku as it does not mention any definite number of days in Free Trial.<b><br/>Okteto does not restart App every 24 hours meaning you can clone large data which can run for days at a time </b><br><br>

## 📢 Follow us:
- Team drive generator : https://msgsuite.eu.org/
- Telegram channel : https://t.me/MsGsuite
- Telegram chat : https://t.me/MsGsuiteChat

## ❤️ Credits & thanks :
- [wrenfairbank](https://github.com/wrenfairbank/telegram_gcloner) for the original python script
- [smartass08](https://github.com/smartass08/telegram_gcloner) to adapt the scrip to heroku
- [anymeofu](https://github.com/anymeofu/CloneBot) for making the Direct Heroku deployable Version
- Zero-The-Kamisama to making me discover this amazing bot and the detailed instructions
- [zorgof](https://t.me/zorgof) for the termux script
- [Aishik Tokdar](https://github.com/aishik2005) for Adding Guide to Deploy on Railway.app , Qovery , Clever Cloud , Scalingo and some other Code Improvements.Also Added Heroku Workflow Deployment Method.
- [Katarina](https://github.com/tiararosebiezetta) for adding the ability to be deployed to Clever Cloud and Scanlingo
- [Miss Emily](https://github.com/missemily2022) for adding Support of Okteto Cloud Deployment as well as improving little layout
