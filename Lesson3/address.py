class Address:
    
    def __init__(self, index, town, street, house, flat):
            self.index = index
            self.town = town
            self.street = street
            self.house = house
            self.flat = flat
        
    def sayIndex(self):
            print("Индекс: ", self.index)
              
    def sayTown(self):
            print("Город: ", self.town)
            
    def sayStreet(self):
            print("Улица: ", self.street)
            
    def sayHouse(self):
            print("Номер дома: ", self.house)
            
    def sayFlat(self):
            print("Номер квартиры: ", self.flat)                        
