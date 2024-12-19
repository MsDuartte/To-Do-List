from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from tasks.models import Task



#@receiver(post_save, sender=Task)
#def taks_post_save(sender, instance, **kwargs):
#   ...