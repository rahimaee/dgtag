from django.core.mail import send_mail
from django.db import models

# Create your models here.
from mytag import settings


class Newsletters(models.Model):
    Email = models.EmailField(verbose_name='ایمیل')

    class Meta:
        verbose_name = 'خبرنامه'
        verbose_name_plural = 'خبرنامه ها'

    def __str__(self):
        return self.Email


class NewslettersSend(models.Model):
    Message = models.TextField(verbose_name='متن پیام')

    def save(self, force_insert=False, force_update=True, using=None,
             update_fields=None):
        all_email = Newsletters.objects.all()
        if all_email is not None:
            subject = 'خبرنامه دی جی تگ'
            message = self.Message
            email_from = settings.EMAIL_HOST_USER
            list_email_user = []
            for email in all_email:
                list_email_user.append(email.Email)
            recipient_list = list_email_user
            send_mail(subject, message, email_from, recipient_list)
            super().save()

    class Meta:
        verbose_name = 'ارسال پیام'
        verbose_name_plural = 'پیام های ارسالی'
