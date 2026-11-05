from tp02.gsi_project.Academic_Element import AcademicElement 

from module import Module 
from tp02.gsi_project.unite import Unite

class Semestre (AcademicElement):
    def __init__(self, name,):

        super().__init__(name, title="semestre title")
        
        self.unites = []
        
    def calculate_coef(self):
        return sum(unt.calculate_coef() for unt in self.unites)
    def add_unite(self, unite):
        self.unites.append(unite)



    def calculate_average(self):
        total = 0
        coef = self.calculate_coef()
        for unt in self.unites :
            total += unt.calculate_average() * unt.calculate_coef ()
        return total / coef
    
    def calculate_credit(self):
        pass

if __name__ == "__main__":



    s1 = Semestre("s1")
    

    u1 = Unite("u1")
    u2 = Unite("u2")
    u3 = Unite("u3")

    mti = Module(
        name="MTI",
        title="Methods and Technologies of implementation",
        coef=3,
        credit=5,
        hours_td=0)
    
    aabd = Module(
        name="AABD",
        title="Architecture et administration des bases de données",
        coef=2,
        credit=4,
        hours_tp=0 #the other parameters par default
    )
    rcb = Module(
        name="rcb",
        title="Reseaux des couches basses/ Reseaux avances",
        coef=3,
        credit=6,
        hours_td=1.5)
    
    algoa = Module(
        name="algoa",
        title="Algorithmique avancée et complexité",
        coef=2,
        credit=4,
        hours_tp=0 #the other parameters par default
    )

    ray_module = Module(
        name="ray",
        title="ryn rhmani",
        coef=7,
        credit=9,
        hours_td=24)
    
    u1.add_module(mti)
    u1.add_module(algoa)
    u2.add_module(rcb)
    u2.add_module(aabd)
    u3.add_module(ray_module)

        
    
    mti.set_grades(tp=18, td=None, exam=15)
    algoa.set_grades(tp=None, td=11, exam=7)

    
    rcb.set_grades(tp=14, td=15, exam=13)
    aabd.set_grades(tp=14, td=None, exam=12)
    
    ray_module.set_grades(tp=13, td=13, exam=13)

    

    s1.add_unite(u1)
    s1.add_unite(u2)
    s1.add_unite(u3)
    print (f"the average of [{mti.name}] is : {mti.calculate_average()}")
    print (f"the average of [{algoa.name}] is : {algoa.calculate_average()}")
    print (f"the credit of [{mti.name}] is : {mti.calculate_credit()}")
    print (f"the credit of [{algoa.name}] is : {algoa.calculate_credit()}")
    print (f"the credit of [{u1.name}] is : {u1.calculate_credit()}")
    print(f"the average of [{u2.name}] is : {u2.calculate_average()}")
    print (f"the average of [{s1.name}] is : {s1.calculate_average()}")