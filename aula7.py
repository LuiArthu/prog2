class apagandor:
    def __init__(self, a, b, c):
        self.Memoria_RAM = a
        self.CPU = b
        self.SO = c

    def LIGAR(self):
        print("LIGANDO...")
        
    def trabalhando(self):
        print(f" Memoria:{self.Memoria_RAM} \n CPU:{self.CPU}\n Sistena operacional:{self.SO}")

    def DESLIGAR(self):
        print("DESLIGANDO.")

coisa = apagandor('16gb', 'processador', 'windwos 11')

coisa.LIGAR()
coisa.trabalhando()
coisa.DESLIGAR()