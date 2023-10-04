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

    def check_salary(self, days):
        salary_days = self.salary_one_day * days
        return f"{self.name}, your salary for {days} days is {salary_days}\n"

    def work(self):
        return "{self.name} come to the office "


class Recruiter(Employee):
    def work(self):
        super().work()
        return f"{self.name} come to the office and start to hiring "


class Developer(Employee):
    def __init__(self, name, rank, salary_one_day, *tech_stack):
        super().__init__(name, rank, salary_one_day)
        self.tech_stack = tech_stack

    def work(self):
        return f"{self.name} come to the office and start to coding"

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(self.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(self.tech_stack)

    def add_develop(self, other):
        name = f"{self.name } {other.name}" 
        tech_stack = self.tech_stack + other.tech_stack
        if self.salary_one_day > other.salary_one_day:
            salary_one_day = self.salary_one_day
        else:
            salary_one_day = other.salary_one_day  
        new_developer = f"New developer was created! \nName: {name}, stack: {set(tech_stack)}, salary: {salary_one_day}"
        return new_developer
        

       
recruiter1 = Recruiter('Oleg','reguiter', 50) 
recruiter2 = Recruiter('Marina',"requiter", 100)

developer1 = Developer('Kristina','developer', 75, 'second tehnologi', 'third tehologi', 'fifth tehnologi')
developer2 = Developer('Denis','developer', 175, 'first tehnologi', 'second tehnologi', 'fifth tehnologi')
developer3 = Developer('Maria', 'developer', 200, 'sixth texnologi', 'first tehnologi')

print(recruiter1)
print(recruiter1.work())
print(recruiter1.check_salary(21))

print(recruiter2)
print(recruiter2.work())
print(recruiter2.check_salary(7))

print(developer1)
print(developer1.work())
print(developer1.check_salary(10))

print(developer2)
print(developer2.work())
print(developer1.check_salary(15))

print(developer2.salary_one_day == developer1.salary_one_day)
print(developer1.salary_one_day > recruiter1.salary_one_day)
print(developer1.salary_one_day < recruiter2.salary_one_day)

print("------------------------------------------------")

print(developer1.tech_stack == developer2.tech_stack)
print(developer1.tech_stack > developer2.tech_stack)
print(developer1.tech_stack < developer2.tech_stack)

print("------------------------------------------------")

print(developer1.add_develop(developer2))
print(developer3.add_develop(developer1))