
#simple class
class Person:
    def __init__(self,person_name:str,year_of_birth:int,ht_inches:int=None):
        self.__name=person_name
        self.__date_of_birth=year_of_birth
        self.__height=ht_inches
        self.abc=None
    
    def get_year_of_birth(self):
        return self.__date_of_birth
        
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        if (self._has_any_number(new_name)):
            print("Sorry person name can't have number.")
            return
        self.__name=new_name
        
    def _has_any_number(self,string):
        return '0' in string 
    
    def get_summary(self):
        return f"Name:{self.__name} DOB:{self.__date_of_birth} Height:{self.__height if self.__height is not None else 'Invaild'}"
    
person_list=[Person('Zulkarnine',1990,72),
             Person('shehab',1980),
             Person('sarker',1993,65),
             Person('baz',2020,80),
             Person('Ban',1945),
             Person('Ben',2020,72)]

# for person in person_list:
#     if person.get_year_of_birth()>=1930:
#         print(person.get_summary())

class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int,email_id:str,student_id:str):
        super().__init__(person_name, year_of_birth)
        self.id=student_id
        self.email=email_id
    
    def get_summary(self):
        return f"Name:{str(self.get_name())} Email:{self.email} Birth: {self.get_year_of_birth()}"
    def __str__(self):
        return f"Name:{self.get_name()} Email:{self.email} Birth: {self.get_year_of_birth()}"

student=Student("sarker",2003,'abcd@gmail.com','1234gfesf')
print(student)
student.set_name('Mahi')
print(student)