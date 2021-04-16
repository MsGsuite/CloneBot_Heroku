#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from functools import wraps

from utils.callback import callback_delete_message
from utils.config_loader import config

logger = logging.getLogger(__name__)


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        ban_list = context.bot_data.get('ban', [])
        # access control. comment out one or the other as you wish. otherwise you can use any of the following examples.
        # if user_id in ban_list:
        if user_id in ban_list or user_id not in config.USER_IDS:
            logger.info('Unauthorized access denied for {} {}.'
                        .format(update.effective_user.full_name, user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_private(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        ban_list = context.bot_data.get('ban', [])
        if user_id in ban_list or chat_id < 0:
            logger.info('Unauthorized access denied for private messages {} {}.'
                        .format(update.effective_user.full_name, user_id))
            if chat_id < 0:
                rsp = update.message.reply_text('Private chat only!')
                rsp.done.wait(timeout=60)
                message_id = rsp.result().message_id
                context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                           context=(update.message.chat_id, message_id))
                context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                           context=(update.message.chat_id, update.message.message_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_private_and_group(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        ban_list = context.bot_data.get('ban', [])
        if user_id in ban_list or (chat_id < 0 or chat_id not in config.GROUP_IDS):
            logger.info('Unauthorized access denied for private and group messages{} {}.'
                        .format(update.effective_user.full_name, user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_group_only(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        ban_list = context.bot_data.get('ban', [])
        if user_id not in config.USER_IDS and (user_id in ban_list or chat_id > 0 or chat_id not in config.GROUP_IDS):
            logger.info('Unauthorized access denied for group only messages {} {}.'
                        .format(update.effective_user.full_name, user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_group_and_its_members_in_private(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        ban_list = context.bot_data.get('ban', [])
        allow = False
        if user_id in config.USER_IDS:
            allow = True
        elif user_id not in ban_list:
            if chat_id < 0:
                if chat_id in config.GROUP_IDS:
                    allow = True
            else:
                for group_id in config.GROUP_IDS:
                    info = context.bot.get_chat_member(chat_id=group_id, user_id=update.effective_user.id)
                    if info.status in ['creator', 'administrator', 'member']:
                        allow = True
                        break
        if allow is False:
            logger.info('Unauthorized access denied for group and its members messages{} {}.'
                        .format(update.effective_user.full_name, user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_user_ids(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        if user_id not in config.USER_IDS:
            logger.info('Unauthorized access denied for {} {}.'
                        .format(update.effective_user.full_name, user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def restricted_admin(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if not update.effective_user:
            return
        user_id = update.effective_user.id
        chat_id = update.effective_chat.id
        if user_id != config.USER_IDS[0]:
            logger.info("Unauthorized admin access denied for {} {}.".format(update.effective_user.full_name, user_id))
            return
        if chat_id < 0:
            return
        return func(update, context, *args, **kwargs)
    return wrapped
