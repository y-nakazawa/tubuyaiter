from django.db import models


class Mutter(models.Model):
    content = models.CharField('内容', max_length=256)
    created_at = models.DateTimeField('作成日', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('更新日', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Mutter'

    def __str__(self):
        return self.content
