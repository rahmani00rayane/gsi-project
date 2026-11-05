from tp02.gsi_project.Academic_Element import AcademicElement 

from module import Module 

class Unite (AcademicElement):
    def __init__(self, name,):

        super().__init__(name, title="unite title")
        
        self.modules = []
        
        
        
    def add_module(self, module):
        self.modules.append(module)

    def calculate_coef(self):
        sum_mdl = 0
        for mdl in self.modules :
            sum_mdl += mdl.coef

        self.coef = sum_mdl
        return self.coef
    

    def calculate_credit(self):
        sum_crd = 0
        for mdl in self.modules :
            sum_crd += mdl.credit if mdl.calculate_average() >= 10 else 0

        self.credit = sum_crd
        return self.credit if self.calculate_average() >= 10 else 0
    
    def calculate_average(self):
        sum_avg = 0
        for mdl in self.modules :
            sum_avg += mdl.calculate_average() * mdl.coef
        return sum_avg / self.calculate_coef()
if __name__ == "__main__":

    u1 = Unite("u1")
    u2 = Unite("u2")

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
        hours_td=0)
    
    algoa = Module(
        name="algoa",
        title="Algorithmique avancée et complexité",
        coef=2,
        credit=4,
        hours_tp=0 #the other parameters par default
    )
        
    mti.set_grades(tp=18, td=None, exam=15)
    aabd.set_grades(tp=14, td=None, exam=12)
    rcb.set_grades(tp=4, td=5, exam=3)
    algoa.set_grades(tp=None, td=11, exam=10)


    u1.add_module(mti)
    u1.add_module(aabd)
    u2.add_module(rcb)
    u2.add_module(algoa)
    print(f"{u1.name} : {[m.name for m in u1.modules]} \n{u2.name} : {[m.name for m in u1.modules]}")  # to be honest .. i got help from ai to write this line
    
    
    
    u1.calculate_coef()
    u1.calculate_credit()
    u2.calculate_coef()
    u2.calculate_credit()
    u1.calculate_average()
    u2.calculate_average()
    print (f" the coefficient of [{u1.name}] is : {u1.coef}")
    print (f" the average of [{u1.name}] is : {u1.calculate_average()}")
    print (f" the credit of [{u1.name}] is : {u1.credit}")


    print (f" the coefficient of [{u2.name}] is : {u2.coef}")
    print (f" the average of [{u2.name}] is : {u2.calculate_average()}")
    print (f" the credit of [{u2.name}] is : {u2.calculate_credit()}")