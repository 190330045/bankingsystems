class User():
    def __init__(self,name,age,gender,phno):
        self.name=name
        self.age=age
        self.gender=gender
        self.phone_number=phno
    def show_details(self):
        print("person details")
        print(" ")
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
        print("mobile_no:",self.phone_number)

class Bank(User):
    def __init__(self,name,age,gender,phno):
        super().__init__(name,age,gender,phno)
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance+=amount
        print("Your account has been credited of RS/-",self.balance,"sucessfully")
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("Insufficient balance\navailable balance in your account RS/-",self.balance)
        else:
            self.balance-=self.amount
            print("Sucessfully withdrawn\nremaining balance RS/-",self.balance)
    def view_balance(self):
        self.show_details()
        print("current balance in your account RS/-",self.balance)

b=Bank("harry",20,"male",9848240246)
b.deposit(10000)
b.withdraw(9000)
b.view_balance()