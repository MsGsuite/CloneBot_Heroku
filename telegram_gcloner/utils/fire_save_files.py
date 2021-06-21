#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import html
import logging
import os
import re
import subprocess
import threading

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from utils.config_loader import config
from utils.google_drive import GoogleDrive

logger = logging.getLogger(__name__)


thread_pool = {}


class MySaveFileThread(threading.Thread):
    def __init__(self, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.daemon = True
        self.args = args
        self.critical_fault = False
        self.owner = -1

    def run(self):
        update, context, folder_ids, text, dest_folder = self.args
        self.owner = update.effective_user.id
        thread_id = self.ident
        is_multiple_ids = len(folder_ids) > 1
        is_fclone = 'fclone' in os.path.basename(config.PATH_TO_GCLONE)
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        gd = GoogleDrive(user_id)
        message = ' Bot Modified by Aishik Tokdar/NL Wizard (@aishik_tokdar) \n \n ╭──────⌈ 📥 Copying 📥 ⌋──────╮\n│\n├ 📂📂 Destinaton Folder/Shared Drive：{}\n'.format(dest_folder['path'])
        inline_keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=f'🚫 Stop File Transfer 🚫', callback_data=f'stop_task,{thread_id}')]])

        reply_message_id = update.callback_query.message.reply_to_message.message_id \
            if update.callback_query.message.reply_to_message else None
        rsp = context.bot.send_message(chat_id=chat_id, text=message,
                                       parse_mode=ParseMode.HTML,
                                       disable_web_page_preview=True,
                                       reply_to_message_id=reply_message_id,
                                       reply_markup=inline_keyboard)
        rsp.done.wait(timeout=60)
        message_id = rsp.result().message_id

        for folder_id in folder_ids:
            destination_path = folder_ids[folder_id]

            command_line = [
                config.PATH_TO_GCLONE,
                'copy',
                '--drive-server-side-across-configs',
                '-P',
                '--stats',
                '1s',
                '--ignore-existing'
            ]
            if config.GCLONE_PARA_OVERRIDE:
                command_line.extend(config.GCLONE_PARA_OVERRIDE)
            elif is_fclone is True:
                command_line += [
                    '--checkers=256',
                    '--transfers=256',
                    '--drive-pacer-min-sleep=1ms',
                    '--drive-pacer-burst=5000',
                    '--check-first'
                ]
            else:
                command_line += [
                    '--transfers',
                    '8',
                    '--tpslimit',
                    '6',
                ]
            gclone_config = os.path.join(config.BASE_PATH,
                                         'gclone_config',
                                         str(update.effective_user.id),
                                         'current',
                                         'rclone.conf')
            command_line += ['--config', gclone_config]
            command_line += [
                '{}:{{{}}}'.format('gc', folder_id),
                ('{}:{{{}}}/{}'.format('gc', dest_folder['folder_id'], destination_path))
            ]

            logger.debug('command line: ' + str(command_line))

            process = subprocess.Popen(command_line,
                                       bufsize=1,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       encoding='utf-8',
                                       errors='ignore',
                                       universal_newlines=True)
            progress_checked_files = 0
            progress_total_check_files = 0
            progress_transferred_file = 0
            progress_total_files = 0
            progress_file_percentage = 0
            progress_file_percentage_10 = 0
            progress_transferred_size = '0'
            progress_total_size = '0 Bytes'
            progress_speed = '-'
            progress_speed_file = '-'
            progress_eta = '-'
            progress_size_percentage_10 = 0
            regex_checked_files = r'Checks:\s+(\d+)\s+/\s+(\d+)'
            regex_total_files = r'Transferred:\s+(\d+) / (\d+), (\d+)%(?:,\s*([\d.]+\sFiles/s))?'
            regex_total_size = r'Transferred:[\s]+([\d.]+\s*[kMGTP]?) / ([\d.]+[\s]?[kMGTP]?Bytes),' \
                               r'\s*(?:\-|(\d+)\%),\s*([\d.]+\s*[kMGTP]?Bytes/s),\s*ETA\s*([\-0-9hmsdwy]+)'
            message_progress_last = ''
            message_progress = ''
            progress_update_time = datetime.datetime.now() - datetime.timedelta(minutes=5)
            while True:
                try:
                    line = process.stdout.readline()
                except Exception as e:
                    logger.debug(str(e))
                    if process.poll() is not None:
                        break
                    else:
                        continue
                if not line and process.poll() is not None:
                    break
                output = line.rstrip()
                if output:
                    # logger.debug(output)
                    match_total_files = re.search(regex_total_files, output)
                    if match_total_files:
                        progress_transferred_file = int(match_total_files.group(1))
                        progress_total_files = int(match_total_files.group(2))
                        progress_file_percentage = int(match_total_files.group(3))
                        progress_file_percentage_10 = progress_file_percentage // 10
                        if match_total_files.group(4):
                            progress_speed_file = match_total_files.group(4)
                    match_total_size = re.search(regex_total_size, output)
                    if match_total_size:
                        progress_transferred_size = match_total_size.group(1)
                        progress_total_size = match_total_size.group(2)
                        progress_size_percentage = int(match_total_size.group(3)) if match_total_size.group(
                            3) else 0
                        progress_size_percentage_10 = progress_size_percentage // 10
                        progress_speed = match_total_size.group(4)
                        progress_eta = match_total_size.group(5)
                    match_checked_files = re.search(regex_checked_files, output)
                    if match_checked_files:
                        progress_checked_files = int(match_checked_files.group(1))
                        progress_total_check_files = int(match_checked_files.group(2))
                    progress_max_percentage_10 = max(progress_size_percentage_10, progress_file_percentage_10)
                    message_progress = '├──────⌈ 📥📥File Transfer in Progress📥📥 ⌋──────' \n \
                                       '├ 🗂 Source : <a href="https://drive.google.com/open?id={}">{}</a>\n│\n' \
                                       '├ ✔️ Checks： <code>{} / {}</code>\n' \
                                       '├ 📥 Transfers： <code>{} / {}</code>\n' \
                                       '├ 📦 Size：<code>{} / {}</code>\n{}' \
                                       '├ ⚡️Speed：<code>{}</code> \n' \
                                       '├ 📥 Transfer Rate : <code>{}</code> \n' \
                                       '├ ⏳ ETA: <code>{}</code>\n' \
                                       '├ ⛩ Progress：[<code>{}</code>] {: >4}%\n│\n' \
                                       '├ Bot Modified by Aishik Tokdar/NL Wizard (@aishik_tokdar) \
                                       '├──────⌈ ⚡️⚡️ Google Drive Clone Bot ⚡️⚡️ ⌋──────' \n \
                        .format(
                        folder_id,
                        html.escape(destination_path),
                        progress_checked_files,
                        progress_total_check_files,
                        progress_transferred_file,
                        progress_total_files,
                        progress_transferred_size,
                        progress_total_size,
                        f'Speed：<code>{progress_speed_file}</code>\n' if is_fclone is True else '',
                        progress_speed,
                        progress_eta,
                        '●' * progress_file_percentage_10 + '○' * (
                                progress_max_percentage_10 - progress_file_percentage_10) + ' ' * (
                                10 - progress_max_percentage_10),
                        progress_file_percentage)

                    match = re.search(r'Failed to Copy: Failed to create Destination Folder', output)
                    if match:
                        message_progress = '{}\n│<code>Write Permission Error.Please check your service account settings.</code>'.format(message_progress)
                        temp_message = '{}{}'.format(message, message_progress)
                        # logger.info('写入权限错误，请确认权限'.format())
                        try:
                            context.bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                          text=temp_message, parse_mode=ParseMode.HTML,
                                                          disable_web_page_preview=True,
                                                          reply_markup=inline_keyboard)
                        except Exception as e:
                            logger.debug('Error {} occurs when editing message {} for user {} in chat {}: \n│{}'.format(
                                e, message_id, user_id, chat_id, temp_message))
                        process.terminate()
                        self.critical_fault = True
                        break

                    match = re.search(r"couldn't list directory", output)
                    if match:
                        message_progress = '{}\n│<code>Read Permission File.Source Folder is not available to copy </code>'.format(message_progress)
                        temp_message = '{}{}'.format(message, message_progress)
                        # logger.info('读取权限错误，请确认权限：')
                        try:
                            context.bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                          text=temp_message, parse_mode=ParseMode.HTML,
                                                          disable_web_page_preview=True,
                                                          reply_markup=inline_keyboard)
                        except Exception as e:
                            logger.debug('Error {} occurs when editing message {} for user {} in chat {}: \n│{}'.format(
                                e, message_id, user_id, chat_id, temp_message))
                        process.terminate()
                        self.critical_fault = True
                        break

                    if message_progress != message_progress_last:
                        if datetime.datetime.now() - progress_update_time > datetime.timedelta(seconds=5):
                            temp_message = '{}{}'.format(message, message_progress)
                            try:
                                context.bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                              text=temp_message, parse_mode=ParseMode.HTML,
                                                              disable_web_page_preview=True,
                                                              reply_markup=inline_keyboard)
                            except Exception as e:
                                logger.debug(
                                    'Error {} occurs when editing message {} for user {} in chat {}: \n│{}'.format(
                                        e, message_id, user_id, chat_id, temp_message))
                            message_progress_last = message_progress
                            progress_update_time = datetime.datetime.now()

                    if self.critical_fault:
                        message_progress = '{}\n│\n│ User terminated'.format(message_progress)
                        process.terminate()
                        break

            rc = process.poll()
            message_progress_heading, message_progress_content = message_progress.split('\n│', 1)
            link_text = 'Unable to fetch link of destinaton folder.'
            try:
                link = gd.get_folder_link(dest_folder['folder_id'], destination_path)
                if link:
                    link_text = '\n│ \n│      👉 <a href="{}">Link</a> 👈'.format(link)
            except Exception as e:
                logger.info(str(e))

            if self.critical_fault is True:
                message = '{}{} ❌\n│{}\n│{}\n│'.format(message, message_progress_heading, message_progress_content,
                                                     link_text)
            elif progress_file_percentage == 0 and progress_checked_files > 0:
                message = '{}{} ✅\n│ File already exists!\n│ {}\n│'.format(message, message_progress_heading, link_text)
            else:
                message = '{}{}{}\n│{}\n│{}\n│\n│'.format(message,
                                                      message_progress_heading,
                                                      '✅' if rc == 0 else '❌',
                                                      message_progress_content,
                                                      link_text)

            try:
                context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message,
                                              parse_mode=ParseMode.HTML, disable_web_page_preview=True,
                                              reply_markup=inline_keyboard)
            except Exception as e:
                logger.debug('Error {} occurs when editing message {} for user {} in chat {}: \n│{}'.format(
                    e, message_id, user_id, chat_id, message))

            if self.critical_fault is True:
                break

        message += '\n╰──────⌈ ✅ Finished ! ⌋──────╯'
        try:
            context.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message,
                                          parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        except Exception as e:
            logger.debug('Error {} occurs when editing message {} for user {} in chat {}: \n│{}'.format(
                e, message_id, user_id, chat_id, message))
        update.callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text='Done', callback_data='cancel')]]))

        logger.debug('User {} has finished task {}: \n│{}'.format(user_id, thread_id, message))
        tasks = thread_pool.get(user_id, None)
        if tasks:
            for t in tasks:
                if t.ident == thread_id:
                    tasks.remove(t)
                    return

    def kill(self):
        self.critical_fault = True
