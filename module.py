from tp02.gsi_project.Academic_Element import AcademicElement 



class Module(AcademicElement):
    def __init__(self, name, title, coef, credit, hours_td = 1.5, hours_tp = 1.5, continous_percent = 40, exam_percent = 60, teaching_mode = "in_preson"):
        super().__init__(name, title)
        #self.week = 15  he will inherate this from AcademicElement

        self.name = name
        self.title = title
        self.coef = coef
        self.credit = credit

        #self.hours_lecture = hours_lecture  also this will inherate from AcademicElement
        self.hours_td = hours_td
        self.hours_tp = hours_tp


        self.teaching_mode = teaching_mode
        self.evaluation_continuous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        self.total_hours = self.weeks * (self.hours_lecture + self.hours_td + self.hours_tp)
        self.grades = {"tp": None, "td": None, "exam": None }


    def set_grades(self, tp=None, td=None, exam=None):
            if tp is not None:
                self.grades["tp"] = tp
            if td is not None:
                self.grades["td"] = td
            if exam is not None:
                self.grades["exam"] = exam

    def summary(self):
            return (
                f"Module : {self.title}({self.name})\n"
                f"Coefficient: {self.coef}, credit: {self.credit}\n"
                f"Teaching mode: {self.teaching_mode}\n"
                f"Hours: total:{self.total_hours}, lecture:{self.hours_lecture}, td:{self.hours_td}, tp:{self.hours_tp}\n"
                f"Evaluation mode: continous: {self.evaluation_continuous_percent}, exam: {self.evaluation_exam_percent} ")
        
    def calculate_average(self):
            
        if self.grades["tp"] is None and self.grades["td"] is not None :
            continous_average = self.grades ["td"]
        elif self.grades["td"] is None and self.grades["tp"] is not None :
           continous_average = self.grades ["tp"]
        else:
            continous_average = (self.grades["tp"] + self.grades["td"]) / 2


        return (( continous_average * self.evaluation_continuous_percent) +( self.grades["exam"] * self.evaluation_exam_percent)) /100

   
   
    def calculate_credit(self):
            return self.credit if self.calculate_average() >= 10 else 0
if __name__ == "__main__":
    MTI = Module(
        name="MTI",
        title="Methods and Technologies of implementation",
        coef=3,
        credit=5,
        hours_td=0
        #the other parameters par default 
    )
    AABD = Module(
        name="AABD",
        title="Architecture et administration des bases de données",
        coef=2,
        credit=4,
        hours_tp=0
    )
    MTI.set_grades(tp=18, td=None, exam=15)
    AABD.set_grades(tp=None, td=6, exam=2)
    print(MTI.summary())
    print(f"moyenne is : {MTI.calculate_average()}/20")
    print(f"credit is : {MTI.calculate_credit()}")

    print(f"moyenne is : {AABD.calculate_average()}/20")
    print(f"credit is : {AABD.calculate_credit()}")
                  
                  
