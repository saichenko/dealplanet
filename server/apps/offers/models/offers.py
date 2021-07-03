from django.db import models


class Offer(models.Model):
    category = models.ForeignKey(
        to='services.Category',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='название',
        max_length=128
    )
    base_price = models.PositiveIntegerField(
        verbose_name='цена без скидки'
    )
    discount_price = models.PositiveIntegerField(
        verbose_name='цена со скидкой'
    )
    discount = models.PositiveSmallIntegerField(
        verbose_name='скидка'
    )
    url = models.URLField(
        verbose_name='ссылка на товар'
    )
    description = models.TextField(
        verbose_name='описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
