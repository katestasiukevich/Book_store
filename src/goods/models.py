from django.db import models

from refs.models import *


# Create your models here.
class Book(models.Model):
    title = models.CharField(
        verbose_name="Название книги", max_length=200, auto_created=False
    )
    cover = models.ImageField(verbose_name="Обложка", upload_to="book_covers/%Y/%m/%d/")
    # author_id = Author.objects.get(pk=1)
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name="author", verbose_name="Автор"
    )  # , default=author_id)
    series = models.ForeignKey(
        Series, on_delete=models.PROTECT, related_name="series", verbose_name="Серия"
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, related_name="genre", verbose_name="Жанр"
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        related_name="publisher",
        verbose_name="Издательство",
        null=True,
        blank=True
    )
    price = models.DecimalField(
        verbose_name="Цена",
        decimal_places=2,
        max_digits=7
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/book-detail/{self.pk}"
