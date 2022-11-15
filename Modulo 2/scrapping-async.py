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
            # response.text retorna o conteúdo da resposta, em unicode. Basicamente, refere-se ao conteúdo da resposta binária. 
            #As solicitações do Python geralmente são usadas para buscar o conteúdo de um URI de recurso específico. 
            #Sempre que fazemos uma solicitação para um URI especificado por meio do Python, ele retorna um objeto de resposta. 
            #Agora, esse objeto de resposta seria usado para acessar determinados recursos, como conteúdo, cabeçalhos, etc
            html = await response.text()
#await: A segunda significa que a corrotina será paralisada naquele ponto aguardando um resultado futuro. Em outras palavras, 
#o controle de execução será dado à outra corroutina e só será retomado quando o resultado ficar pronto.
            print("Body:", html[:15], "...")
#Por fim ele mostra o tipo de conteudo e especificamente a linha numero 15

# Por fim, executamos  asyncio.run(main()) , isso cria um loop de eventos e executa todas as tarefas dentro dele.
#Depois que todas as tarefas forem concluídas, o loop de eventos será destruído automaticament
asyncio.run(main())
