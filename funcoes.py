from urllib.request import urlopen
from bs4 import BeautifulSoup

#Testa a página se esta online
def pegaPagina(url):
  try:
    resposta = urlopen(url)
    soup = BeautifulSoup(resposta.read(), "html.parser")
    return soup
  except:
    print("erro na função pega pagina")

#Busca a hora/data 
def buscarHorario(soup):
  horario = []
  for item in soup.find_all('div', class_='span2 tileInfo'):
    horario.append(item.find_all('li'))
  for i in range(0, len(horario)):
    horario[i] = "{0} {1}".format(horario[i][2].get_text(), horario[i][3].get_text())
  return horario

#Busca a imagem da notícia
def buscarImagem(soup):
    imagem = []
    for item in soup.find_all('div', class_='tileItem'):
      if item.find_all('img'):
        imagem.append('https://www.ifb.edu.br' + item.find_all('img')[0].attrs['src'])
      else:
        imagem.append('https://www.ifb.edu.br' + '/images/IFBVertical.png')
    return imagem

#Busca o ttítulo da notícia
def buscarTitulo(soup):
    titulo = []
    for item in soup.select('.tileHeadline'):
      texto = item.get_text().strip()
      titulo.append(texto)
    return titulo

#Busca a descrição da notícia
def buscarDescricao(soup):
    descricao = []
    for item in soup.select('.description'):
      texto = item.get_text().strip()
      descricao.append(texto)
    return descricao

#Busca o link da notícia
def buscarLink(soup):
    link_noticia = []
    for item in soup.select('.tileHeadline'):
      link_noticia.append('https://www.ifb.edu.br' + item.a.get('href'))
    return link_noticia

#from time import sleep

'''def loopCronometro(soup):
  for contagem in range(0,5):
    arquivo = open(noticias.json, 'r')
    for i in rande list(lista_noticia[i].keys())[0]
  return resposta'''