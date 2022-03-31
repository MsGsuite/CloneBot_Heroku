#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging

from telegram import ParseMode
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram.utils.helpers import mention_html

from utils.config_loader import config

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, add_group))


def add_group(update, context):
    message = 'joined: {} {}'.format(mention_html(update.message.new_chat_members[0].id,
                                                  html.escape(update.message.new_chat_members[0].full_name)),
                                     update.message.new_chat_members[0].id)
    logger.info(message)
    context.bot.send_message(chat_id=config.USER_IDS[0], text=message, parse_mode=ParseMode.HTML)
    if update.message.chat_id not in config.GROUP_IDS:
        if update.message.new_chat_members[0].id == context.bot.id:
            mention_html_from_user = mention_html(update.message.from_user.id,
                                                  html.escape(update.message.from_user.full_name))
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text='『{}』Thank you for adding this MsgSuite CloneBot bot to the group. {}'
                                     .format(mention_html_from_user,
                                             config.AD_STRING.format(context.bot.username)),
                                     parse_mode=ParseMode.HTML)
            context.bot.send_message(chat_id=update.message.chat_id, text='I am not authorized to be here 😔. \n So I am leaving this group. \n Ask my owner to allow me in your group.')
            message = '🔙 Left Uunauthorized Group : \n │ Name : {} ({}). \n │ Bot Added by{} {}. \n │ Message : {}'.format(
                update.message.chat.title,
                update.message.chat_id,
                mention_html_from_user,
                update.message.from_user.id,
                update.message.text)
            context.bot.leave_chat(update.message.chat_id)
            logger.warning(message)
            context.bot.send_message(chat_id=config.USER_IDS[0], text=message, parse_mode=ParseMode.HTML)
