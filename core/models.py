from django.db import models




class ParagraphMissionOfKinderGarden(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name_plural = "Параграфи - МИСИЯ НА ЗАВЕДЕНИЕТО"


class TextVisionGarden(models.Model):
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name_plural = "Текст - ВИЗИЯ НА ЗАВЕДЕНИЕТО"


class TextValueGarden(models.Model):
    text = models.TextField(max_length=700)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name_plural = "Текст - ЦЕННОСТ НА ЗАВЕДЕНИЕТО"
