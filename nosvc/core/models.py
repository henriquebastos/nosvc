# coding: utf-8
from django.db import models
from model_utils.models import TimeStampedModel


CITIES = (
    (1, u'Porto Alegre'),
    (2, u'Florianópolis'),
    (3, u'Rio de Janeiro'),
    (4, u'São Paulo'),
    (5, u'Curitiba'),
    (6, u'Belo Horizonte'),
    (7, u'Novo Hamburgo'),
    (8, u'Balneário Camboriú'),
    (9, u'Brasília'),
    (10, u'Niterói'),
    (11, u'Santos'),
    (12, u'Sta. Cruz do Sul'),
    (13, u'Manaus'),
    (14, u'Ji-Paraná'),
    (15, u'Canoas'),
    (16, u'Cuiabá'),
    (17, u'Joinville'),
    (18, u'Caxias do Sul'),
    (19, u'Juiz de Fora'),
    (20, u'Viçosa'),
    (21, u'Londrina'),
    (22, u'Salvador'),
    #(23, u'Aaah! Minha cidade não tá aqui!'),
    (24, u'Campo Grande'),
    (25, u'Piracaia SP'),
    (26, u'São Leopoldo'),
    (27, u'Presidente Lucena - RS'),
    (28, u'Goiânia'),
    (29, u'Esteio'),
    (30, u'Alto Paraíso'),
    (31, u'Rio Grande'),
)


class Meeting(TimeStampedModel):
    # user
    # backers
    # rewards
    # updates
    # dynamic fields
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    about = models.TextField()
    headline = models.TextField(max_length=140)
    period = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    city = models.IntegerField(choices=CITIES)
    location = models.TextField()

    video = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    visible = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    # host
    about_host = models.TextField(blank=True, null=True)

    min_attendees = models.PositiveIntegerField(blank=True, null=True)
    max_attendees = models.PositiveIntegerField(blank=True, null=True)
    deadline = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    questions = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('meeting_detail', (), {'slug': self.slug})
