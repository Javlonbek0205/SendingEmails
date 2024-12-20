# Django User Notification System

Bu loyihada foydalanuvchilarga email xabarnomalarini yuborish uchun ishlatiladigan Django modellar va signal mexanizmlaridan foydalaniladi. Har safar `UserNotification` modelida yangi yozuv qo'shilganda, tizim avtomatik ravishda email yuboradi.

## Fayllar Tuzilishi

### 1. **signals.py**

`signals.py` fayli Django signals mexanizmi yordamida foydalanuvchining xabarini saqlashda va yangi yozuv qo'shilganda (post_save) ishlatiladi.

- **`post_save` signal** yordamida har safar `UserNotification` modeliga yangi yozuv qo'shilganda, `send_notification` funksiyasi ishga tushadi.
- Bu funksiya oxirgi foydalanuvchining xabarini olish va email yuborish uchun `send_mail` metodini chaqiradi.

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserNotification

@receiver(post_save, sender=UserNotification)
def send_notification(sender, instance, created, **kwargs):
    latest_user = UserNotification.objects.latest('pk')  # Oxirgi foydalanuvchi
    print('Oxirgi foydalanuvchi:', latest_user.name)

    # Email jo'natish
    latest_user.send_mail()
