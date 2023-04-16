from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    user_name = models.CharField(verbose_name='ユーザ名', max_length=32)
    member_since = models.DateField(verbose_name='入会日', default=timezone.now)
    membership_years = models.PositiveSmallIntegerField(verbose_name='会員年数', null=True, unique=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)