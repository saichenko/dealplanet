from django.db import models


class OfferImage(models.Model):
    offer = models.ForeignKey(
        to='offers.Offer',
        verbose_name='предложение',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='offers/images/',
    )

    def __str__(self):
        return self.offer.name

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
