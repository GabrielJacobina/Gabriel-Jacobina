import telebot
import json
import os.path
from time import sleep
from datetime import datetime

def rodar(arquivo_noticias, arquivo_tmp):
	bot = telebot.TeleBot("830508513:AAFzKIgoWaKkPoDMig3Fa_tCBFKGIGxQogY")

	a = open(arquivo_noticias, 'r')
	noticias = json.loads(a.read())
	a.close()
	

	chat_id = -348118127
	chanel_id = -1001202036776

	lista_chaves = []
	for i in range(len(noticias)):
		chave = list(noticias[i].keys())[0]
		lista_chaves.append(chave)
	
	lista_data = []
	for i in range(len(noticias)):
		data_hora = list(noticias[i].keys())[0]
		data_hora = datetime.strptime(data_hora, '%d/%m/%y  %Hh%M')
		lista_data.append(data_hora)
	
	#formata a notícia para se tornar uma mensagem
	'''noticia = (noticias[i][lista_chaves[i]])
	mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])'''

	#se o arquivo existe envia noticias novas e atualiza o arquivo
	if (os.path.exists(arquivo_tmp)):

		arquivo_tmp = open(arquivo_tmp,'r')
		ultima_data = datetime.strptime(arquivo_tmp.read(), '%d/%m/%y  %Hh%M')
		arquivo_tmp.close()

		for i in range(len(noticias)-1, -1, -1):
			print(i)
			
			noticia = (noticias[i][lista_chaves[i]])
			mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])
			data_hora = lista_data[i]

			if data_hora > ultima_data:
				bot.send_message(chat_id, 
												mensagem,
												parse_mode = "markdown")
				bot.send_message(chanel_id, 
												mensagem, 
												parse_mode = "markdown")			
			sleep(1)
	#se o arquivo não existe, ele envia as noticias no canal e cria o arquivo com a data da ultima noticia enviada
	else:	
		for i in range(len(noticias)-1, -1, -1):	
			noticia = (noticias[i][lista_chaves[i]])
			mensagem ="_{0}_ \n*{1}* \n\n{2}\n\n [.]({3}).\n {4}\n".format(lista_chaves[i],noticia[0],noticia[1],noticia[2],noticia[3])
			
			bot.send_message(chat_id, 
											mensagem,
											parse_mode = "markdown")
			bot.send_message(chanel_id, 
											mensagem, 
											parse_mode = "markdown")
		sleep(1)

	arquivo_tmp = open('ultima_noticia_bot.tmp','w')
	arquivo_tmp.write(list(noticias[i].keys())[0])
	arquivo_tmp.close()

	#apaga o arquivo de noticias.json
	os.remove(arquivo_noticias)

if(__name__ == "__main__"):
	rodar()