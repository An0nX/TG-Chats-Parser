from pyrogram import Client
import asyncio
from pyrogram.errors import FloodWait, BadRequest
from pyrogram.types import ChatPermissions
import tgcrypto
from colorama import Fore
import dbm
import re
from time import sleep

def dbm_base():
    file = dbm.open( 'api.dbm' ,'c')
    try:
        file['api_id']
    except:
        file['api_id'] = input('Введите api_id:')
        file['api_hash'] = input('Введите api_hash:')
    file.close()
    return dbm.open( 'api.dbm' ,'r')
file = dbm_base()
api_id = int(file['api_id'].decode())
api_hash = file['api_hash'].decode()

dbm_base()

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        supergroups = list()
        groups = list()
        channels = list()
        bots = list()
        users = list()
        async for dialog in app.get_dialogs():
            if f'{dialog.chat.type}' == 'ChatType.SUPERGROUP':
                supergroups.append(f'{dialog.chat.title}:{dialog.chat.username}')
            if f'{dialog.chat.type}' == 'ChatType.GROUP':
                groups.append(f'{dialog.chat.title}:{dialog.chat.username}')
            if f'{dialog.chat.type}' == 'ChatType.CHANNEL':
                channels.append(f'{dialog.chat.title}:{dialog.chat.username}')
            if f'{dialog.chat.type}' == 'ChatType.BOT':
                if f'{dialog.chat.last_name}' != 'None':
                    bots.append(f'{dialog.chat.first_name} {dialog.chat.last_name}:@{dialog.chat.username}')
                else:
                    if f'{dialog.chat.first_name}' == 'None' and f'{dialog.chat.username}' == 'None':
                        continue
                    if f'{dialog.chat.username}' == 'None':
                        users.append(f'{dialog.chat.first_name}:None')
                    else:
                        bots.append(f'{dialog.chat.first_name}:@{dialog.chat.username}')
            if f'{dialog.chat.type}' == 'ChatType.PRIVATE':
                if f'{dialog.chat.last_name}' != 'None':
                    users.append(f'{dialog.chat.first_name} {dialog.chat.last_name}:@{dialog.chat.username}')
                else:
                    if f'{dialog.chat.first_name}' == 'None' and f'{dialog.chat.username}' == 'None':
                        continue
                    if f'{dialog.chat.username}' == 'None':
                        users.append(f'{dialog.chat.first_name}:None')
                    else:
                        users.append(f'{dialog.chat.first_name}:@{dialog.chat.username}')
        print('Супергруппы:\n\n')
        with open('supergroups.txt', 'w', encoding="utf-8") as file1:
            for i in supergroups:
                print(f'{i}\n')
                try:
                    file1.write(f'{i}\n')
                except UnicodeEncodeError:
                    file1.write(f'{i}\n')
        print('\nГруппы:\n\n')
        with open('groups.txt', 'w', encoding="utf-8") as file2:
            for j in groups:
                print(f'{j}\n')
                try:
                    file2.write(f'{j}\n')
                except UnicodeEncodeError:
                    file2.write(f'{j}\n')
        print('\nКаналы:\n\n')
        with open('channels.txt', 'w', encoding="utf-8") as file3:
            for s in channels:
                print(f'{s}\n')
                try:
                    file3.write(f'{s}\n')
                except UnicodeEncodeError:
                    file3.write(f'{s}\n')
        print('\nБоты:\n\n')
        with open('bots.txt', 'w', encoding="utf-8") as file4:
            for a in bots:
                print(f'{a}\n')
                try:
                    file4.write(f'{a}\n')
                except UnicodeEncodeError:
                    file4.write(f'{a}\n')
        print('\nЮзеры:\n\n')
        with open('users.txt', 'w', encoding="utf-8") as file5:
            for b in users:
                print(f'{b}\n')
                try:
                    file5.write(f'{b}\n')
                except UnicodeEncodeError:
                    file5.write(f'{b}\n')

asyncio.run(main())