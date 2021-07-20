from PIL import Image
from django.db import models


class Offer(models.Model):
    category = models.ForeignKey(
        to='services.Category',
        on_delete=models.CASCADE,
        related_name='offers'
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
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='offers/images/'
    )

    def __str__(self):
        return self.name

    def resize_image(self):
        """Crop and resize image to 350x350."""
        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 350 and height > 350:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))
        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((350, 350))

        img.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
        ordering = ['discount']
