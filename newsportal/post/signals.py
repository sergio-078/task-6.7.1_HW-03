from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Post, Category


@receiver(m2m_changed, sender=Post)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()

        emails = User.objects.filter(
                subscriptions__category=instance.category
            ).values_list('email', flat=True)

        subject = f'Новая публикация в категории {instance.category}'

        text_content = (
                f'Заголовок: {instance.title}\n'
                f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
            )
        html_content = (
                f'Заголовок: {instance.title}<br>'
                f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
                f'Ссылка на публикацию</a>'
            )
        for email in emails:
                msg = EmailMultiAlternatives(subject, text_content, None, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

    # if kwargs['action'] == 'post_add':
    #     categories= instance.categories.all()



# @receiver(post_save, sender=Post)
# def post_created(instance, created, **kwargs):
#     if not created:
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category=instance.category
#     ).values_list('email', flat=True)
#
#     subject = f'Новая публикация в категории {instance.category}'
#
#     text_content = (
#         f'Заголовок: {instance.title}\n'
#         f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Заголовок: {instance.title}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на публикацию</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, None, [email])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
