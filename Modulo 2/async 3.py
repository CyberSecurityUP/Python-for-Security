#import asyncio

#async def ola_mundo():
 #  print('Olá ...')
  # await asyncio.sleep(1)
  # print('... Mundo!')

#asyncio.run(ola_mundo())


#import aiohttp
#import asyncio

#async def main():

#    async with aiohttp.ClientSession() as session:

 #       pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'
  #      async with session.get(pokemon_url) as resp:
   #         pokemon = await resp.json()
    #        print(pokemon['name'])

#asyncio.run(main())

#Neste código, é criada uma corrotina chamada main, que está sendo
#executada com o loop de eventos asyncio. Aqui, estamos iniciando
#uma sessão do cliente aiohttp, um objeto único que pode ser usado
#para várias solicitações individuais e que, por padrão,
#pode se conectar com até 100 servidores diferentes ao mesmo tempo.
#Com esta sessão, estamos fazendo
#uma solicitação à API Pokémon e aguardando uma resposta.

#import aiohttp
#import asyncio
#import time

#start_time = time.time()


#async def main():

 #   async with aiohttp.ClientSession() as session:

  #      for number in range(1, 151):
    #        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
   #         async with session.get(pokemon_url) as resp:
     #           pokemon = await resp.json()
      #          print(pokemon['name'])

#asyncio.run(main())
#print("--- %s seconds ---" % (time.time() - start_time))

#Desta vez, também vamos calcular a duração de todo processo.

import aiohttp
import asyncio
import time

start_time = time.time()


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

#Este exemplo usa um código totalmente sem bloqueio, por isso o tempo total para executar as 150 solicitações
#será quase igual ao tempo de execução da solicitação mais demorada.
#Os números exatos variam conforme a conexão de Internet.

