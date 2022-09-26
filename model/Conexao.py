from pathlib import Path
import mysql.connector
class Conexao():
    
    def connection():
        conn = mysql.connector.connect(
            host="localhost", port=3306, user="root",
            password="", db="log"
        )
        return conn
     
     
    def enviar_para_banco(itens):
        conn = Conexao.connection() 
        cursor = conn.cursor()
        sql = f"""insert ignore into logs(tipo_erro,data_erro,mensagem_erro,detalhe_erro,log) values """
        cursor.execute(sql + itens)
        conn.commit()
         
        
        
    @staticmethod                
    def enviar_para_o_banco(cont,itens):
      if cont >= 1000:
         Conexao.enviar_para_banco(itens[:-1]) 
      
          
         
         
    @staticmethod
    def excluir_arquivo(filename):
            filePath=Path(f"arquivos_logs/{filename}")
            try:
                filePath.unlink()
            except OSError as e:
                print(f"Error:{ e.strerror}")