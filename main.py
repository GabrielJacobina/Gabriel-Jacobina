import minerador_IFB
import Telegram_Bot

def escolhe_sistema():

		print("\nQual sistema deseja rodar?\n")

		print("(1) Minerador de Notícias IFB \n(2) Canal de notícias Telegram\n")

		sistema = int(input("Qual sistema? "))

		if(sistema == 1):
				print("Rodando minerador de notícias")
				minerador_IFB.rodar('noticias.json','ultima_noticia_minerador.tmp')
		elif(sistema == 2):
				print("Rodando canal de noticias Telegram")
				Telegram_Bot.rodar('noticias.json', 'ultima_noticia_bot.tmp')

if(__name__ == "__main__"):
		escolhe_sistema()