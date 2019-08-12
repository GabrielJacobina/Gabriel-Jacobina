# -*- coding: utf-8 -*-
import json
import funcoes as f
import os.path
from datetime import datetime

def rodar(nome_arquivo, nome_arquivo_tmp):
	url = 'https://www.ifb.edu.br/brasilia/noticiasbrasilia'

	#Chamada das funções que estão em um arquivo auxiliar
	soup = f.pegaPagina(url)
	imagem = f.buscarImagem(soup)
	horario = f.buscarHorario(soup)
	titulo = f.buscarTitulo(soup)
	descricao = f.buscarDescricao(soup)
	link = f.buscarLink(soup)

	lista_horario = []
	lista_imagem = []
	lista_titulo = []
	lista_imagem = []
	lista_descricao = []
	lista_link = []

	for i in range(0, len(horario)):
		lista_horario.append(horario[i].strip())
		lista_imagem.append(imagem[i])
		lista_titulo.append(titulo[i])
		lista_descricao.append(descricao[i])
		lista_link.append(link[i])

	lista_noticia = []
	for i in range(0, len(lista_titulo)):
		noticia = {
			lista_horario[i] : (lista_titulo[i],
								lista_descricao[i],
								lista_imagem[i],
								lista_link[i])
		}
		lista_noticia.append(noticia)

	'''nome_arquivo_tmp = 'Data_hora.tmp'
	nome_arquivo = 'noticias.json' '''

	# Converte todas as datas das notícias resgatadas nessa execução de str para datetime
	lista_data = []
	for i in range(len(lista_noticia)):
		data_hora = list(lista_noticia[i].keys())[0]
		data_hora = datetime.strptime(data_hora, '%d/%m/%y  %Hh%M')
		lista_data.append(data_hora)
	
	if (os.path.exists(nome_arquivo)):
		arquivo_json = open(nome_arquivo, 'r')
		dados_json = json.loads(arquivo_json.read())
		arquivo_json.close()

		arquivo_tmp = open(nome_arquivo_tmp,'r')
		ultima_data = datetime.strptime(arquivo_tmp.read(), '%d/%m/%y  %Hh%M')
		arquivo_tmp.close()
		
		for i in range(len(lista_data)-1, -1, -1):
			data_hora = lista_data[i]
			if data_hora > ultima_data:
				#Salvar essa notícia
				dados_json.insert(0,lista_noticia[i])
				
		dados_json_new = json.dumps(dados_json, ensure_ascii=False, indent = 2)
		arquivo = open(nome_arquivo,'w')
		arquivo.write(dados_json_new)
		arquivo.close()
	else:
		for x in range(len(lista_data)-1, -1, -1):
			i = x
		dados_json = json.dumps(lista_noticia, ensure_ascii=False, indent = 2)
		arquivo = open(nome_arquivo,'w')
		arquivo.write(dados_json)
		arquivo.close()
	arquivo_tmp = open(nome_arquivo_tmp,'w')
	arquivo_tmp.write(list(lista_noticia[i].keys())[0])
	arquivo_tmp.close()

if(__name__ == "__main__"):
	rodar()