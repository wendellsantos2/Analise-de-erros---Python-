from controller.SlmController import SlmController
from model.Slm import Slm
import schedule
import time
#import datetime
class Main():
     
    @staticmethod   
    def job():
        dados_config = Main.adquirir_configs()
        slm = Main.adquirir_acesso_slm(dados_config)
        Main.baixar_log(slm)
        Main.separar_txt()
        Main.mover_txt()
        Main.ler_varios_logs()
       # Main.excluir_log()
 
    @staticmethod
    def adquirir_configs():
        with open('.EditorConfig', 'r') as conf:
            dados = {}
            for j in conf.readlines():
                if j.strip() != '':
                    dados_repasse = j.replace('\n', '').split('=')
                    dados[dados_repasse[0]] = dados_repasse[1]
            return dados      

    @staticmethod   
    def adquirir_acesso_slm(dados_config):
        return Slm(
            ip=dados_config['ip_slm'],
            porta=dados_config['porta_slm'],
            end_point=dados_config['endpoint_slm'])

    @staticmethod
    def ler_varios_logs():
        SlmController.ler_logs_da_pasta()

    @staticmethod
    def mover_txt():
        SlmController.mover_pasta()
        
    @staticmethod    
    def separar_txt():
        SlmController.separar_txt()
        
    @staticmethod
    def baixar_log(slm):
        SlmController.buscar_enviar_log(slm)
 
    def excluir_log(slm):
        SlmController.excluir_log()

    #funcinamento por horario
if __name__ == "__main__":
      schedule.every().day.at("11:10").do(Main.job)
      schedule.every().day.at("10:30").do(Main.job)
      while True:
        schedule.run_pending()
        time.sleep(1)
        
    


    