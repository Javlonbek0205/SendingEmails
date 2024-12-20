from django.db import models
from .services import send_email
from django.http import JsonResponse

# Create your models here.
class UserNotification(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    class Meta:
        get_latest_by = 'pk'
    def __str__(self):
        return self.name

    def send_mail(self):
        subject = 'Hello this is a homework'
        email = self.email

        context = {
            'latest_user': self.name,
            'message': self.message
        }
        if not subject:
            return JsonResponse({'status': False, 'error': 'Subject cannot be empty'}, status=400)
        elif not email:
            return JsonResponse({'status': False, 'error': 'Email cannot be empty'}, status=400)

        send_email('send_email.html', subject, email, context)
        return JsonResponse({'status': True, 'message': 'Email sent successfully'}, status=200)
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new or self._state.db == 'default':
            self.send_mail()

