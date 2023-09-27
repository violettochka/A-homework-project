class Employee():
    def __init__(self,  name, rank,  salary_one_day):
        self.name = name
        self.salary_one_day = salary_one_day
        self.rank = rank

    def __str__(self):
        return f'{self.rank.upper()}: {self.name}'   

    def __eq__(self, other):
        return self.salary_one_day == other.salary_one_day 

    def __lt__(self, other):
        return self.salary_one_day < other.salary_one_day

    def __gt__(self, other):
        return self.salary_one_day > other.salary_one_day             


    def work(self):
        return "{self.name} come to the office "

class Recruiter(Employee):
    def work(self):
        super().work()
        return f"{self.name} come to the office and start to hiring \n"


class Developer(Employee):
    def work(self):
        super().work()
        return f"{self.name} come to the office and start to coding\n"

recruiter1 = Recruiter('Oleg','reguiter', 50) 
recruiter2 = Recruiter('Marina',"requiter", 100)
print(recruiter1.__str__())
print(recruiter1.work())
print(recruiter2.__str__())
print(recruiter2.work())

developer1 = Developer('Kristina','developer', 75)
developer2 = Developer('Denis','developer', 75)
print(developer1.__str__())
print(developer1.work())
print(developer2.__str__())
print(developer2.work())

print(developer2 == developer1)
print(developer1 > recruiter1)
print(developer1 < recruiter2)