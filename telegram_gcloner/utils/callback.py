#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram.ext import CallbackContext

logger = logging.getLogger(__name__)


def callback_delete_message(context: CallbackContext):
    (chat_id, message_id) = context.job.context
    try:
        context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        logger.warning('cannot delete message {}: {}'.format(message_id, e))
