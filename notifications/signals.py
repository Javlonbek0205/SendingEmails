from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserNotification

@receiver(post_save, sender=UserNotification)
def send_notification(sender, instance, created, **kwargs):
    # Doimo oxirgi foydalanuvchini olish
    latest_user = UserNotification.objects.latest('pk')  # Oxirgi foydalanuvchi
    print('Oxirgi foydalanuvchi:', latest_user.name)

    # Email jo'natish
    latest_user.send_mail()
