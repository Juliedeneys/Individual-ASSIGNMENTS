#%% white and blue
class Student: 
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
        
 
    def show_all(self):
        print(self.name + " " + self.last_name + " is a " + self.age + 
              " year-old student of the " + self.master + " masters programme.")
        
   
    
students = [
Student("Alejandro", "Meneses", "27", "MCSBT"),
Student("Agata", "Kaczmarek", "31","MDBI"),
Student("Anastasia", "Lasunina", "25", "MDBI"),
Student("Anikken", "Barstad Gjeruldsen", "27", "MDBI"),
Student("Candela", "Noya", "24", "MDBI"),
Student("Daniil", "Osipov", "21", "MDBI"),
Student("David", "Barrero Gonzalez", "31", "MCSBT"),
Student("Edem", "Francois", "28", "MCSBT"),
Student("Eduardo", "Paraja", "23", "MDBI"),
Student("Florian", "Diegruber", "25", "MCSBT"),
Student("Hannah", "Oldorf", "23", "MCBT"),
Student("Isabella", "Rosenthal", "27", "MDBI"),
Student("Javier", "Fernandez", "24", "MCSBT"),
Student("Lukas", "Hauser", "28","MDBI"),
Student("Leila", "Tazi", "27", "MCSBT"),
Student("Laura", "Kageneck", "23", "MCSBT"),
Student("Monica", "Alvarenga","28", "MDBI"),
Student("Natalie", "Cedeno", "26", "MDBI"),
Student("Octavio", "Ramírez", "28", "MDBI"),
Student("Tancredi", "Bernard", "21", "MCSBT"),
Student("Yasmine", "Lyagoubi", "23", "MDBI"),
Student("Arthur", "Maroquene-Froissart","23", "MCSBT")
]
        

def function_to_show_them_all():
    
    for student in students:
        student.show_all()

    