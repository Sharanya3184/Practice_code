class Nokia:
    company = "nokia"
    website = "www.nokia.com"

    def contact_details(self):
        print("Address chennai")
        print("Phone: 1234567890")

class Nokia_3310(Nokia):
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def show_details(self):
        return f"Model: {self.model} \nPrice: {self.price}"

obj = Nokia()
obj.contact_details()
obj2 = Nokia_3310("Nokia 3310", 1000)
obj2.show_details()