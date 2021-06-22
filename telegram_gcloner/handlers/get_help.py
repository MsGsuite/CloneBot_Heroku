#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram.ext import Dispatcher, CommandHandler

from utils.config_loader import config
from utils.callback import callback_delete_message
from utils.restricted import restricted

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('help', get_help))


@restricted
def get_help(update, context):
    message = 'Send a Google Drive link, or forward a message with a Google Drive link to copy the files.\n' \
              'Pre - Configuration with /sa and /folders is required is necessary to use the Bot on Telegram.\n\n' \
              'Bot modified by Aishik Tokdar/NL Wizard (@aishik_tokdar) \n\n' \
              '📚 Commands:\n' \
              ' │ /start - Start the Bot\n' \
              ' │ /sa - Upload the Serivce Account zip file to use the Bot\n' \
              ' │ /folders - Select the Shared Drives where you wish to save your files and folders\n' \
              ' │ /ban - Ban a Telegram User ID from using the Bot\n' \
              ' │ /unban - Reallow a Telegram User ID from using the Bot that was earlier banned\n' \
              ' │ /contact - Get the contacts details of the owner of the Bot\n' \
              ' │ /help - Get Information about the Bot\n' \
              ' │ /id - Get your Telegram User  ID\n' \
              ' │ /vip - Add a Telegram User ID to the VIP Access List\n' \
              ' │ /unvip - Remove a Telegram User ID to the VIP Access List\n' \
    rsp = update.message.reply_text(message)
    rsp.done.wait(timeout=60)
    message_id = rsp.result().message_id
    if update.message.chat_id < 0:
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, message_id))
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, update.message.message_id))
