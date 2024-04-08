#define the employee class
class employee:
    #define the __init__ function with the name, ID_number, department, and job title as arguments
    def __init__(self, name, ID_number, department, job_title):
        #set the name
        self.__name = name
        #set the ID number
        self.__ID_number = ID_number
        #set the department
        self.__department = department
        #set the job title
        self.__job_title = job_title
    
    #define the get_name method
    def get_name(self):
        #return the name that was set by the programm
        return self.__name
    
    #define the get_ID_number method
    def get_ID_number(self):
        #return the ID number that was set by the programm
        return self.__ID_number
    
    #define the get_department method
    def get_department(self):
        #return the department that was set by the programm
        return self.__department
    
    #define the get_job_title method
    def get_job_title(self):
        #return the job title that was set by the programm
        return self.__job_title
                                 
        
