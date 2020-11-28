#Polymorphism
class Computer_Science(): 
    def Degree(self): 
        print("Degree offered for Computer Science is B.E / B.Tech") 
  
    def Jobs(self): 
        print("Computer Science jobs - Software Engineer / Business Analyst") 
  
    def preference(self): 
        print("Computer Science is Preferred more by women")
        
#Uses same method names as Computer_Science()
class Mechanical(): 
    def Degree(self): 
        print("Degree offered for Mechanical is B.E.") 
  
    def Jobs(self): 
        print("Mech jobs - Hardware Specialist,Mechanical Engineer") 
  
    def preference(self): 
        print("Mechanical is preferred more by men") 

#Creating objects for both Classes  
obj_CS = Computer_Science() 
obj_Mech = Mechanical() 
for course in (obj_CS, obj_Mech): 
    course.Degree() 
    course.Jobs() 
    course.preference() 
