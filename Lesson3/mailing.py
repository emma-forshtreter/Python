from address import Address

class Mailing:
    
    def __init__(self, to_address: Address, from_address: Address, cost: int, track: str):
            self.to_address = to_address
            self.from_address = from_address
            self.cost = cost
            self.track = track     
            
    def sayToAddress(self):
            print("Куда: ", self.to_address)
              
    def sayFromAddress(self):
            print("Откуда: ", self.from_address)
            
    def sayCost(self):
            print("Стоимость: ", self.cost)
            
    def sayTrack(self):
            print("Трэк: ", self.track)             
    