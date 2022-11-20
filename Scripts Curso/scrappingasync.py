import aiohttp
import asyncio

async def main():
# Primeiramente definimos uma sessão de cliente com aiohttp:
    async with aiohttp.ClientSession() as session:
        #Em seguida, com nossa sessão, executamos uma resposta get em uma única URL:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            #Em terceiro lugar, observe como usamos a palavra-chave await na frente de response.text() assim:
            html = await response.text()
#await: A segunda significa que a corrotina será paralisada naquele ponto aguardando um resultado futuro. Em outras palavras, o controle de execução será dado à outra corroutina e só será retomado quando o resultado ficar pronto.
            print("Body:", html[:15], "...")

# Por fim, executamos  asyncio.run(main()) , isso cria um loop de eventos e executa todas as tarefas dentro dele.
#Depois que todas as tarefas forem concluídas, o loop de eventos será destruído automaticament
asyncio.run(main())
