from django.dispatch import Signal,receiver

#creating signals
notification = Signal(providing_args= ['request','user'])


#receiver function
@receiver(notification)
def show_notification(sender, **kwargs):
    print('sender :', sender)
    print(f'kwarge :{kwargs}')
    print('Notification')