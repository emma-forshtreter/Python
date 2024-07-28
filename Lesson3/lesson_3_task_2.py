from smartphone import Smartphone

lst = ['Samsung', 'Galaxy A5', '+71234567890', 'Huawei', 'Nova 12i', '+71122334455', 'Honor', 'X9b', '+71112223334', 'iPhone', '15', '+79998887776', 'ASUS', 'Zenfone 10', '+73334445556']

length = len(lst)

for i in range(0,length,3):
    phone = Smartphone(lst[i], lst[i+1], lst[i+2])

    phone.sayBrand()
    phone.sayModel()    
    phone.sayNumber()