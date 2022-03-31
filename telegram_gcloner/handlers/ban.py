#!/usr/bin/python3
# -*- coding: utf-8 -*-
import copy
import logging

from telegram import Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext, Filters

from utils.config_loader import config
from utils.fire_save_files import thread_pool
from utils.restricted import restricted_admin

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('ban', ban, filters=Filters.chat(config.USER_IDS[0]), pass_args=True))
    dispatcher.add_handler(CommandHandler('unban', unban, filters=Filters.chat(config.USER_IDS[0]), pass_args=True))


@restricted_admin
def ban(update: Update, context: CallbackContext):
    if not context.args:
        ban_list = context.bot_data.get('ban', None)
        if ban_list:
            update.message.reply_text('\n'.join(map(str, ban_list)))
        return
    if not context.args[0].isdigit:
        update.message.reply_text('/ban user_id')
        return
    user_id = int(context.args[0])
    if not context.bot_data.get('ban', None):
        context.bot_data['ban'] = [user_id]
    elif user_id not in context.bot_data['ban']:
        new_ban = copy.deepcopy(context.bot_data['ban'])
        new_ban.append(user_id)
        context.bot_data['ban'] = new_ban
    else:
        update.message.reply_text('✔️ User Already Exists in the Blacklist.')
        return
    context.dispatcher.update_persistence()
    tasks = thread_pool.get(user_id, None)
    if tasks:
        for t in tasks:
            t.kill()
            logger.debug('Task {} was stopped due to user {} is banned.'.format(t.ident, user_id))
            break
    update.message.reply_text('✅ User Added in the Blacklist.')
    logger.info('{} is banned.'.format(user_id))
    return


@restricted_admin
def unban(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].isdigit:
        update.message.reply_text('/unban user_id')
        return
    user_id = int(context.args[0])
    if user_id in context.bot_data.get('ban', []):
        new_ban = copy.deepcopy(context.bot_data['ban'])
        new_ban.remove(user_id)
        context.bot_data['ban'] = new_ban
        context.dispatcher.update_persistence()
        update.message.reply_text('✅ User Removed in the Blacklist.')
        logger.info('{} is unbanned.'.format(user_id))
        return
    else:
        update.message.reply_text('✖️ User is not Present in the Blacklist.')
        return
