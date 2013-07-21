from emailer.notify import notify


def send_email_notification(sender, instance, created, **kwargs):
    if created:
        notify(instance.id)
