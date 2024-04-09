from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed # m2m_changed # , post_save
from django.dispatch import receiver

# from django.conf import settings

from .models import PostCategory # PostCategory # Subscriber  # Post  # Category


# @receiver(post_save, sender=Post)
# def test_signal(sender, instance, **kwargs):
#     print(f'I am signal!!!')


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        print(f'I am signal!!!')
        # categories = instance.category.all()
        # print(f'I am signal!!!')
#
#         emails = User.objects.filter(
#                 subscriptions__category=instance.category.all()
#             ).values_list('email', flat=True)
#
#         subject = f'Новая публикация в категории {instance.category}'
#
#         text_content = (
#                 f'Заголовок: {instance.title}\n'
#                 f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
#             )
#         html_content = (
#                 f'Заголовок: {instance.title}<br>'
#                 f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#                 f'Ссылка на публикацию</a>'
#             )
#         for email in emails:
#                 msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()


# @receiver(m2m_changed, sender=Post)
# def notify_about_new_post(sender, instance, **kwargs):
#     if not kwargs['action'] == 'post_add':
#         return
#
#     emails = User.objects.filter(
#         subscriptions__category__in=instance.Category.all()
#     ).values_list('email', flat=True)
#
#     subject = f'Новая публикация в категории {instance.category}'
#
#     text_content = (
#         f'Заголовок: {instance.title}\n'
#         f'Ссылка на публикацию: http://127.0.0.1:8000{instance.get_absolute_url()}'
#     )
#     html_content = (
#         f'Заголовок: {instance.name}<br>'
#         f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
#         f'Ссылка на публикацию</a>'
#     )
#     for email in emails:
#         msg = EmailMultiAlternatives(subject, text_content, from_email=settings.DEFAULT_FROM_EMAIL, to=[email])
#         msg.attach_alternative(html_content, mimetype="text/html")
#         msg.send()
