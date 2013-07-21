from django.core.mail import send_mail

from feed.models import Post


def notify(post_id):
    post = Post.objects.get(id=post_id)
    goal_title = None
    if "#" in post.note:
        goal_title_components = post.note.split()
        for el in goal_title_components:
            if "#" in el:
                goal_title = el.split("#")[1]
                break

    if goal_title:
        subject = "{} just made progress on {}!".format(
            post.user.first_name, goal_title)
    else:
        subject = "{} just made progress on a goal!".format(
            post.user.first_name)
    body = "Check it out here: {}".format(post.detail_url)
    from_address = "Achieve.ly <e@achievely.com>"
    recipients = ["xie1989@gmail.com", "suneel0101@gmail.com"]
    send_mail(
        subject,
        body,
        from_address,
        recipients,
        fail_silently=False)
