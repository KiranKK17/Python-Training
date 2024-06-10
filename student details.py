class student:
    def __init__(self, name ,roll_number, password):
        self.name=name #public attribute
        self._roll_number=roll_number #protected attribute
        self.__password=password #private attribute
        
    def display_details(self):
        print("Name:", self.name)
        print("Roll Number:", self._roll_number)
        #private attribute accessed within the class
        print("Password:", self.__password)
        
        #getter method for accessing private attribute
        def get_password(self):
            return self.__password
        
        #setter method for modifying private attribute
        def set_password(self, new_password):
            self.__password= new_password


#creating an instance of the student class
student=student("Pogu Sravya Geervani", "2205A41L15", "Ammulu1404")

#accessing public attributes directly
print("Name(Public):", student.name)

#accessing protected attribute(not recommended)
print("Roll Number(Protected):", student._roll_number)

#accessing private attribute using getting method
#print("Password (Private):", student.get_password)


student.display_details()