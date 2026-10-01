class CreditCard:
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPI:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Paytm:
    def pay(self, amount):
        print("Paid ₹", amount, "using Paytm")

class Payment:
    def __init__(self, method):
        self.method = method

    def make_payment(self, amount):
        self.method.pay(amount)

payment = Payment(UPI())
payment.make_payment(500)

payment = Payment(CreditCard())
payment.make_payment(1000)

payment = Payment(Paytm())
payment.make_payment(750)