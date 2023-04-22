from django.db import models
from django.utils import timezone

class UserInfo(models.Model):
    user_name = models.CharField(help_text='ユーザ名', verbose_name='ユーザ名', max_length=32)
    member_since = models.DateField(help_text='入会日', verbose_name='入会日', default=timezone.now)
    membership_years = models.PositiveSmallIntegerField(help_text='会員年数',verbose_name='会員年数', null=True, unique=False)
    created_at = models.DateTimeField(help_text='作成日時', verbose_name='作成日時', auto_now_add=True)