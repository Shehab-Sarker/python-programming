
#simple class
class Person:
    def __init__(self,person_name,date_of_birth,ht):
        self.__name=person_name
        self.date_of_birth=date_of_birth
        self.ht=ht
        
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
        return f"Name:{self.__name}\nDOB:{self.date_of_birth}\nHeight:{self.ht}"
    
a_person=Person("SHEHAB SARKER","27.09.2003","5.6 inchi")
# b_person=Person("Zulkarnine")

print(a_person.get_name())
# print(b_person.get_name())
print(a_person.get_summary())
a_person.set_name("Zulkarnine")
print(a_person.get_summary())
a_person.set_name("0shehab")
print(a_person.get_name())
