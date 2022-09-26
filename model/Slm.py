

class Slm():
    
    def __init__(self, ip, porta, end_point):
        self.ipSlm, self.portaSlm, self.end_point = ip, porta, end_point
    
    @property
    def url_conexao(self):
        return f'http://{self.ipSlm}:{self.portaSlm}/{self.end_point}' 
    
    