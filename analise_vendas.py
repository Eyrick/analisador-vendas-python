import pandas as pd

CAMINHO_ARQUIVO = 'data/dados_vendas.csv'

def Carregar_Dados(caminho):
	try: 
		dataFrame = pd.read_csv(caminho)
		print("✅ Dados Carregados com Sucesso.")
		return dataFrame
	
	except(FileNotFoundError): 
		print(f"❌ Erro: Arquivo não encontrado no caminho: {caminho}")
		return None
	except UnicodeDecodeError:
		print("Aviso: Falha na codificação UTF-8. Tentando 'latin-1'...")
	try:
		# Tenta a codificação alternativa
		dataFrame = pd.read_csv(caminho, encoding='latin-1') 
		print("✅ Dados carregados com sucesso (Latin-1).")
		return dataFrame
	except Exception as e:
		# Se falhar no latin-1, captura a exceção final
		print(f"❌ Erro final de carregamento: {e}")
		return None
	except(Exception):
		print(f"❌ Erro inesperado ao carregar dados: {Exception}")

def Limpar_e_Transfomar(df):
	print("\n\n---Iniciando Tratamento de dados---\n\n")

	#Tratamento de Nulos
	print("\nValores nulos por coluna (antes do tratamento):")
	print(df.isnull().sum())
	
	#Tratamento de Datas 
	df['Order Date'] = pd.to_datetime(df['Order Date'])
	df['Ship Date'] = pd.to_datetime(df['Ship Date'])

	#Feature: Coluna Mês
	df['Mês_Perdido'] =  df['Order Date'].dt.to_period('M')


if __name__ == "__main__":
	dataFrame_vendas = Carregar_Dados(CAMINHO_ARQUIVO)
	
	if dataFrame_vendas is not None:
		print("\n---Inspeção Inicial do Banco de Dados---\n")
		print("Primeiras Linhas:")
		print(dataFrame_vendas.head())
		print("Informações de tipos e nulos:")
		print(dataFrame_vendas.info())

		print(Limpar_e_Transfomar(dataFrame_vendas))
		
	else:
		print("\nPrograma encerrado por falta de arquivos para leitura")