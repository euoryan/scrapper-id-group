from telethon import TelegramClient, sync
from telethon.tl.types import Channel
import pandas as pd
import asyncio

async def get_filtered_groups():
    api_id = input('Digite seu API ID: ')
    api_hash = input('Digite seu API Hash: ')
    phone = input('Digite seu número de telefone (com código do país): ')
    filter_text = input('Digite o texto que deve conter no nome do grupo: ')

    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone)

    groups_data = []
    
    async for dialog in client.iter_dialogs():
        if isinstance(dialog.entity, Channel) and filter_text in dialog.name:
            groups_data.append({
                'nome': dialog.name,
                'id': dialog.id
            })

    df = pd.DataFrame(groups_data)
    df.to_excel('grupos_filtrados.xlsx', index=False)
    print('Arquivo grupos_filtrados.xlsx gerado com sucesso!')

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(get_filtered_groups())