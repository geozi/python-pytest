class User:
    """
    The User class represents an application user.
    
    """    
    count = 0
    
    def __init__(self, first_name, last_name, age ):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        User.count += 1
    
    # Getters 
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property 
    def age(self):
        return self._age
    
    
    # Setters
    
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    
    @age.setter 
    def age(self, age):
        self._age = age
