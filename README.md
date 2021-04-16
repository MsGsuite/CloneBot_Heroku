## ⚛️ Deploying on Heroku

<p><a href="https://heroku.com/deploy"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" alt="Deploy to Heroku" /></a></p>


1. Fill the following values : 

> gclone_para_override = leave this empty if you don't know how to use it
>
> [General] =  ⚠ Don't touch this
>
> group_ids = your telegram group ID (leave it blank if you don't want to add one). To get your group id, go to @MissRose_bot and type /id
>
> path_to_gclone =./gclone  ⚠ Don't touch this
>
> telegram_token = go to @BotFather and send /newbot to get one
>
> user_ids = -1 = Your user id (go to @MissRose_bot and type /id to get your id) - If you want to authorize multiple users, add a comma between each ID (ex: 150654065,5897065)

2. Click on Deploy app...
3. When it's over, go to : https://dashboard.heroku.com/apps/YOURAPPNAME/resources (remplace YOURAPPNAME by your appname 🙃)
4. Then click on the ✏ and check $0.00 option and click on confirm.

Now you can start your bot !




## ❤️ Credits & thanks :
- [wrenfairbank](https://github.com/wrenfairbank/telegram_gcloner) for the original python script
- [smartass08](https://github.com/smartass08/telegram_gcloner) to adapt the scrip to heroku
- [anymeofu](https://github.com/anymeofu/CloneBot) for making the Direct Heroku deployable Version
- Zero-The-Kamisama to making me discover this amazing bot and the detailed instructions
