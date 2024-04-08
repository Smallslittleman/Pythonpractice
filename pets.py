#Class for setting a pets name, age, and type
class pet: 
    #defining the init method with the name, animal type, and age as the arguments
    def __init__(self, __name, __animal_type, __age):
        #name attribute
        self.__name = __name
        #animal type attribute
        self.__animal_type = __animal_type
        #age attribute
        self.__age = __age
    
    #defining the set name method
    def set_name(self):
        #set the pets name to the users input
        self.__name = input("Write your pets name, ")
    
    #defining the set animal type method
    def set_animal_type(self):
        #Set the pets animal type to the users input
        self.__animal_type = input("Write what type of animal your is, ")
    
    #defining the set age method
    def set_age(self):
        #Set the pets age to the users input
        self.__age = input("Write your pets age, ")
    
    #defining the get name method
    def get_name(self):
        #print the pets name that the user input
        print(f'Pets name is: {self.__name}')
    
    #defining the get animal type method
    def get_animal_type(self):
        #print the pets animal type that the user input
        print(f'The pet is a: {self.__animal_type}')
    
    #defining the get age method
    def get_age(self):
        #print the pets age that the user input
        print(f'Pets age is: {self.__age}')