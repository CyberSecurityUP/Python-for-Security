import asyncio
import aiohttp
import time

start_time = time.time()

async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon['name']


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, 150):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
                print(pokemon)
                
asyncio.run(main())
print("%s Tempo percorrido" % (time.time() - start_time))



#async def hello_world():
 #   print("Hello...")
  #  await asyncio.sleep(5)
   # print("World")
#asyncio.run(hello_world())
