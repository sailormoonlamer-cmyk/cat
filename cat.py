class cats:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def cat(self):
        print(f'Привет моего кота зовут {self.name} и ему {self.age} лет')
        
        
        
cat = cats("маркис", 5)
cat.cat()
