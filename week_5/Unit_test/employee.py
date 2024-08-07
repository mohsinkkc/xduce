class Employee:

    raise_amt=1.05

    def __init__(self,first_name,last_name,pay):
        self.first_name=first_name
        self.last_name=last_name
        self.pay=pay

    def email(self):
        return f'{self.first_name}.{self.last_name}@gmail.com'

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)