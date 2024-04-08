class pet: 
    def __init__(self, __name, __animal_type, __age):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age
    
    def set_name(self):
        self.__name = input("Write your pets name, ")
    
    def set_animal_type(self):
        self.__animal_type = input("Write what type of animal your is, ")
    
    def set_age(self):
        self.__age = input("Write your pets age, ")
    
    def get_name(self):
        print(f'Pets name is: {self.__name}')
    
    def get_animal_type(self):
        print(f'The pet is a: {self.__animal_type}')
    
    def get_age(self):
        print(f'Pets age is: {self.__age}')