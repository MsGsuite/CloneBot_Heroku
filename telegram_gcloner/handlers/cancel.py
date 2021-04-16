#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram.ext import Dispatcher, CallbackQueryHandler

from utils.helper import alert_users
from utils.restricted import restricted

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CallbackQueryHandler(cancel, pattern=r'^cancel$'))


@restricted
def cancel(update, context):
    query = update.callback_query
    if query.message.chat_id < 0 and \
            (not query.message.reply_to_message or
             query.from_user.id != query.message.reply_to_message.from_user.id):
        alert_users(context, update.effective_user, 'invalid caller', query.data)
        query.answer(text='Yo-he!', show_alert=True)
        return
    # query.message.edit_reply_markup(reply_markup=None)
    query.message.delete()
