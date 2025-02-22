from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
      return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director,
                                 on_delete=models.CASCADE,
                                 related_name='movies',)

    def __str__(self):
       return self.title



STARS = [(i, str(i)) for i in range(1, 6)]
class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='reviews',)
    stars = models.IntegerField(choices=STARS, null=True, blank=True, default=5)

    def __str__(self):
         return self.movie.title

    class Meta:
        verbose_name = 'Отзыв'