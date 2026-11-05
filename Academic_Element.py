from abc import ABC, abstractmethod

class AcademicElement(ABC):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.weeks = 15
        self.coef = 0
        self.credit = 0
        self.hours_lecture = 1.5
        self.hours_td = 1.5
        self.hours_tp = 1.5



    @abstractmethod
    def calculate_average(self):
        pass

    @abstractmethod
    def calculate_credit(self):
        pass