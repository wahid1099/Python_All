

class YtChannel:
    def __init__(self):
        self.subscribers = []
        self.cur_time = None

    def notifyuser(self, modifier):
        for subscriber in self.subscribers:
            if modifier != subscriber:
                subscriber.update(self)

    def subcribechannel(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        try:
            self.subscribers.remove(subscriber)
        except ValueError:
            pass


class Youtube(YtChannel):
    def __init__(self, name=''):

        self.name = name

    def notify(self, time):
        print(self.name, ':', time)


class subscribeduser(YtChannel):
    def __init__(self, name):
        pass

    def sendNotification(self, time):
        pass
