import aiohttp
import asyncio
import time

#Criando um metodo que vai realizar o download de um arquivo para coletar informações, gerando uma sessao http na url para realizar o procedimento
async def download_file(url):
  print(f'Iniciando o download {url}')
  async with aiohttp.ClientSession() as session:
    async with session.get(url)
    content = await resp.read()
    print(f"Finalizando o download {url}")
    return content
#Nessa etapa ele vai ler o conteudo do arquivo criado com nome async_{name} e vai abrir o arquivo em modo binario assim ele nao altera os dados conforme sao gravados
async def write_file(name, content):
  filename = f'async_{name}.html'
  with open(filename, 'wb') as f:
    print(f'Lendo o arquivo {filename}')
    f.write(content)
    print(f'finalizando a leitura {filename}')
#Aqui sera as tarefas que ele vai executar com o arquivo
async def scrape_task(name, url):
  content = await download_file(url)
  await wirte_file(name, content)

async def main():
  tasks = []
  for name, url in enumerate(open('urls.txt').readlines()):
    tasks.append(scrape_task(name,url))
  await asyncio.wait(tasks)
 
if __name__ == '__main__':
  t - time.perf_counter()
  asyncio.run(main())
  t2 = time.perf_counter() - t
  print(f'Tempo corrido: {t2:02.f} segundos')
