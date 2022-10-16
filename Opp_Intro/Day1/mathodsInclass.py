def add(a,b):
    sum=a+b
    print(sum)


def deduct(x,y):
    result=x-y
    return result


class Phone:
    color='black'
    features=['camera','waters proof','can be use as hammer']

    def call(self):
        print('Calling.......')
    def send_sms(self,number,text):
        sms=f'sending: {text} to :{number}...'
        return sms


my_phone=Phone()
my_phone.call()
sms=my_phone.send_sms('01787878787','Hi how are you')
print(sms)