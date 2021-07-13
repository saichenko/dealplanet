from django.db import models


class Category(models.Model):
    """A class represents Yandex.Market category.

    Fields:
        id: ID of category on Yandex.Market;
        name: name of category on Yandex.Market;
    """

    id = models.PositiveIntegerField(
        primary_key=True
    )
    name = models.CharField(
        verbose_name='название',
        max_length=32
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
