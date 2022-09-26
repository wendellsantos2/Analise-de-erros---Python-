import csv
from time import sleep
import requests
from controller.Erro import Erro
 
from model.Conexao import Conexao 
import os
import shutil
from pathlib import Path
class SlmController():
    
    @staticmethod
    def buscar_enviar_log(slm): 
        # Módulo básico de extração
        retorno_log = SlmController.efetuar_requisicao_log(slm.url_conexao)
        # Módulo básico de gravação
        nomedoarquivo = 'controller/logs.txt'
        arquivoaberto = open(nomedoarquivo, 'w', encoding='utf-8')
        arquivoaberto.write(retorno_log)
        arquivoaberto.close()
      
    @staticmethod
    def separar_txt(): 
        arquivos_log = open('controller/logs.txt', 'r').readlines()
        filename = 1
        for linha in range(len(arquivos_log)):
            if linha % 250 == 0:
                open(str(filename) + '.txt', 'w+').writelines(arquivos_log[linha:linha+250])
                filename += 1
                
                
    def mover_pasta():
        logs = [logs_txt for logs_txt in os.listdir() if '.txt' in logs_txt.lower()]
        for log in logs:
            pasta = 'arquivos_logs/' + log  
            shutil.move(log, pasta)    
        
                        
    @staticmethod      
    def ler_logs_da_pasta():
       dados = ""
       cont = 1
       for filename in os.listdir("../Demanda_SLM_txt/arquivos_logs/"):
            with open(os.path.join("../Demanda_SLM_txt/arquivos_logs/", filename), 'r') as logs:
                dados = csv.DictReader(logs,delimiter="|",fieldnames=['tipo','data','mensagem','detalhe','log'])
                itens = " "
                for conteudo_arquivo in dados:
                    log = (conteudo_arquivo)
                    ex = (log['tipo'])
                    if ex == 'EXCEPTION ':
                        linhas = Erro(tipo_error=log['tipo'],data_error=log['data'],mensagem_error=log['mensagem'] ,descricao_error=log['detalhe'],log=log['log'],)
                        itens += f"""('{linhas.tipo_error}','{linhas.data_error}','{linhas.mensagem_error}','{linhas.descricao_error}','{linhas.log}'),"""
                        cont+=1
                        Conexao.enviar_para_o_banco(cont,itens)
     
            Conexao.excluir_arquivo(filename)
            
    @staticmethod
    def efetuar_requisicao_log(url_slm):
        requisicao = None
        try:
            requisicao = requests.get(url_slm).text
               
        except:
            requisicao = "Falha ao adquirir log"
        finally:
            return requisicao      


    @staticmethod       
    def excluir_log(url_slm):
        try:
            requisicao = requests.get(url_slm).text
        except:
            requisicao = "Falha ao Excluir"
        finally:
            return requisicao
                                
                    
                    
                    
                
       