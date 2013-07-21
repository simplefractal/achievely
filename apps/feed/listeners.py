from django.conf import settings

from emailer.notify import notify


def sync_media_s3(sender, instance, created, **kwargs):
    """
    Syncs media folder to S3 bucket.
    """
    if settings.PRODUCTION and created:
        call_command('sync_media_s3')


def send_email_notification(sender, instance, created, **kwargs):
    if created:
        notify(instance.id)
