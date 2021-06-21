#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging


from telegram import ParseMode
from telegram.utils.helpers import mention_html

from utils.config_loader import config

logger = logging.getLogger(__name__)


def leave_chat_from_message(message, context):
    context.bot.send_message(chat_id=message.chat_id,
                             text='Hey, Thank you for adding ⌈ ⚡️⚡️ Google Drive Clone Bot ⚡️⚡️ ⌋ to this Group. ' + config.AS_STRING.format(context.bot.username),
                             parse_mode=ParseMode.HTML)
    context.bot.send_message(chat_id=message.chat_id, text='\n\nUnfortunately I am not allowed to be used here 😔 \n If you want to use me in this group, ask my owner to authorize me 😉 or deploy me on Heroku from https://github.com/tacmp-neel/CloneBot_Heroku.')
    if message.from_user:
        mention_html_from_user = mention_html(message.from_user.id,
                                              message.from_user.full_name.full_name)
        text = '🔙 Left Unauthorzed Group : \n │ Name : {} ({}). \n │ Added by : {} {}. \n │ Message : {}'.format(
            html.escape(message.chat.title),
            message.chat_id,
            mention_html_from_user,
            message.from_user.id,
            message.text)
    else:
        text = '🔙 Left Unauthorzed Group : \n │ Name : {} ({}). \n │ Message : {}'.format(
            html.escape(message.chat.title),
            message.chat_id,
            message.text)
    context.bot.leave_chat(message.chat_id)
    logger.warning(text)
    context.bot.send_message(chat_id=config.USER_IDS[0], text=text, parse_mode=ParseMode.HTML)
