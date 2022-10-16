class Phone:
    manufacturer ='china'
    def __init__(self,brand,price,color=None):
        self.brand = brand
        self.price =price
        self.color = color

    def send_sms(self,number,text):
        sms=f'sending: {text} to {number}'
        return sms


myphone=Phone('oppo',5000,'blue')
print(myphone.brand,myphone.price,myphone.color)