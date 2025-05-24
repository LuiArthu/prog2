class vo():
    def __init__(self, planta):
        self.planta = planta
        
    def exibe_planta (self):
        print(self.planta)

class pai (vo):
    def __init__(self, planta, planta2):
        super().__init__(planta)
        self.planta2 = planta2
    
    def exibe_planta (self):
        print(f"{self.planta} e {self.planta2}")

class eu (pai):
    def __init__(self, planta, planta2, planta3):
        super().__init__(planta, planta2)
        self.planta3 = planta3

    def exibe_planta (self):
        super().exibe_planta()
        return (f"e {self.planta3}")

vo = vo("batata")
pai = pai("batata","uva")
eu = eu("batata","uva", "maca")

print('-------vo------')
vo.exibe_planta()
print('------pai------')
pai.exibe_planta()
print('-----filho-----')
eu.exibe_planta()