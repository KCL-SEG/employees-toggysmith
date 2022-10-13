"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly_salary = None, hours_worked = None, hourly_pay = None, bonus_commission = None, contract_commission = None, number_of_contracts = None):
        self.name = name
        self.monthly_salary = monthly_salary
        self.hours_worked = hours_worked
        self.hourly_pay = hourly_pay
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.number_of_contracts = number_of_contracts

    def get_pay(self):
        pay = 0

        if self.hours_worked != None: # They have a hourly contract
            pay += self.hourly_pay * self.hours_worked
        elif self.monthly_salary != None: # They have a salary contract
            pay += self.monthly_salary

        if self.bonus_commission != None: # They have a bonus commission
            pay += self.bonus_commission
        elif self.contract_commission != None: # They have a contract commission
            pay += self.contract_commission * self.number_of_contracts

        return pay

    def __str__(self):
        r_str = ""

        if self.hours_worked != None:
            r_str += f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_pay}/hour"
        else:
            r_str += f"{self.name} works on a monthly salary of {self.monthly_salary}"

        if self.bonus_commission != None:
            r_str += f" and receives a bonus commission of {self.bonus_commission}."
        elif self.contract_commission != None:
            r_str += f" and receives a commission for {self.number_of_contracts} contract(s) at {self.contract_commission}/contract."
        else:
            r_str += "."

        r_str += f" Their total pay is {self.get_pay()}."

        return r_str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly_pay = 25, hours_worked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly_salary = 3000, contract_commission = 200, number_of_contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours_worked = 150, hourly_pay = 25, contract_commission = 220, number_of_contracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly_salary = 2000, bonus_commission = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hourly_pay = 30, hours_worked = 120, bonus_commission = 600)
