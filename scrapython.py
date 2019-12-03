
## Consulta por CNPJ para extrair e EMAIL de site de listagem de cnpj via Python e BeautifulSoup
## Site exemplo https://cnpj.biz/ mas pode ser outro

from bs4 import BeautifulSoup
import urllib.request

urlpage='endereco'
url='email'

f = open('listfile.txt')
for line in f:
  urlpage = 'https://cnpj.biz/'+line
  url = 'vazio'
  print(urlpage)
  page = urllib.request.urlopen(urlpage)
  soup = BeautifulSoup(page, 'html.parser')
  ####### print(soup)
  for link in soup.find_all('a'):
      if "mailto" in link.get('href'):
          url = link.get('href')
  print(url)
  arquivo = open('emaillist.txt', 'r')
  conteudo = arquivo.readlines()
  conteudo.append(line','url)
  arquivo = open('emaillist.txt', 'w')  # Abre novamente o arquivo (escrita)
  arquivo.writelines(conteudo)
  arquivo.close()

f.close()
