from django.conf import settings
from libthumbor import CryptoURL


def thumb(img, **kwargs):
    """
    Uses thumbor to prepare image served by S3.
    """
    image_url = img.url if hasattr(img, 'url') else img
    if settings.LOCAL:
        image_url = u"{}{}".format("http://localhost:8000", image_url)

    kwargs['image_url'] = image_url

    base = settings.THUMBOR_BASE_URL

    crypto = CryptoURL(key=settings.THUMBOR_KEY)
    path = crypto.generate(**kwargs)

    # With the unsafe option, path has no leading slash
    # so we add it ourselves
    if kwargs.get('unsafe'):
        path = "/{}".format(path)

    return u'{}{}'.format(base, path)
