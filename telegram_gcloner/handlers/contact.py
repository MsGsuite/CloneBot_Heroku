#!/usr/bin/python3
# -*- coding: utf-8 -*-
import html
import logging

from telegram import ParseMode
from telegram.ext import Dispatcher, CommandHandler
from telegram.utils.helpers import mention_html

from utils.callback import callback_delete_message
from utils.config_loader import config
from utils.restricted import restricted_private

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('contact', contact, pass_args=True))


@restricted_private
def contact(update, context):
    text = update.message.text.strip('/contact')
    if text:
        context.bot.send_message(chat_id=config.USER_IDS[0],
                                 text='📬 Received message from {} ({}):'.format(
                                     mention_html(update.effective_user.id, html.escape(update.effective_user.name)),
                                     update.effective_user.id),
                                 parse_mode=ParseMode.HTML)
        context.bot.forward_message(chat_id=config.USER_IDS[0],
                                    from_chat_id=update.message.chat_id,
                                    message_id=update.message.message_id)
        logger.info('{} ({}) left a message: {}'.format(update.effective_user.name, update.effective_user.id, text))
        rsp = update.message.reply_text('Roger that 👍')
        rsp.done.wait(timeout=60)
        message_id = rsp.result().message_id
        if update.message.chat_id < 0:
            context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                       context=(update.message.chat_id, message_id))
            context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                       context=(update.message.chat_id, update.message.message_id))
    else:
        rsp = update.message.reply_text('You\'re so shy, don\'t you want to say anything?\n' +
                                        config.AD_STRING.format(context.bot.username),
                                        ParseMode.HTML)
        rsp.done.wait(timeout=60)
        message_id = rsp.result().message_id
        if update.message.chat_id < 0:
            context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                       context=(update.message.chat_id, message_id))
            context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                       context=(update.message.chat_id, update.message.message_id))
