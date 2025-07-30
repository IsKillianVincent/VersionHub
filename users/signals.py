from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from users.models import User, UserSetting
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_user_setting(sender, instance, created, **kwargs):
    if created and not hasattr(instance, "settings"):
        UserSetting.objects.create(user=instance)
        logger.info(f"UserSetting created for {instance.email}")

@receiver(post_delete, sender=User)
def delete_user_setting(sender, instance, **kwargs):
    try:
        settings = instance.settings
        settings.delete()
        logger.info(f"UserSetting deleted for {instance.email}")
    except UserSetting.DoesNotExist:
        pass