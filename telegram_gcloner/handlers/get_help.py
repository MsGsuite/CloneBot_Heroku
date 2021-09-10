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
    message = 'Send a Google Drive link, or forward a message with a Google Drive link to manually transfer.\n' \
              'Configuration with /sa and /folders is required.\n\n' \
              '📚 Bot Commands:\n' \
              ' │ /folders - Set favorite folders\n' \
              ' │ /sa - Private chat only, upload a ZIP containing SA accounts with this command as the subject.\n' \
              ' │ /help - Output this message\n'
              ' │ /ban - Ban a Telegram User ID from using the Bot.\n'
              ' │ /unban - Reallow a Telegram User ID from using the Bot that was earlier banned.\n'
              ' │ /vip - Add a Telegram User ID to the VIP Access List.\n'
              ' │ /unvip - Remove a Telegram User ID to the VIP Access List.\n'
              ' │ /id - Get your Telegram User  ID.\n'
              ' │ /contact - Get the contacts details of the owner of the Bot.\n'
    rsp = update.message.reply_text(message)
    rsp.done.wait(timeout=60)
    message_id = rsp.result().message_id
    if update.message.chat_id < 0:
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, message_id))
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, update.message.message_id))
