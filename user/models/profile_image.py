import os
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from utils.general_model import GeneralModel

User = get_user_model()


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/profile_image/', filename)


class ProfileImage(GeneralModel):
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='profile_images'
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to=get_file_path,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('ProfileImage')
        verbose_name_plural = _('ProfileImages')

    def __str__(self):
        return f'{self.user}'
