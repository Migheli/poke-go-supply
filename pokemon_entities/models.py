from django.db import models  # noqa F401


# your models here
class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField('название', max_length=200)
    title_en = models.CharField('название англ.', max_length=200, blank=True)
    title_jp = models.CharField('название яп.', max_length=200, blank=True)
    photo = models.ImageField('фото',
                              upload_to='images',
                              blank=True,
                              null=True,
                              default='default.png'
                              )
    description = models.TextField('описание', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='next_evolutions',
        verbose_name='предыдущая эволюция',
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('появляется', default=None)
    disappeared_at = models.DateTimeField('исчезает', default=None)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)
