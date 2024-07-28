class Smartphone:
    
    def __init__(self, brand, model, number):
            self.brand = brand
            self.model = model
            self.number = number
    
    def sayBrand(self):
            print(self.brand, "-", end="")
    
    def sayModel(self):
            print(self.model, ".", end="")
    
    def sayNumber(self):
            print(self.number)       
