from django.db import models

# Create your models here.

class CursoManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

class Curso(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', blank=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    image = models.ImageField(
        upload_to='courses/images', verbose_name='imagem',
        null=True, blank=True
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated = models.DateTimeField('atualizado em', auto_now=True)

    objects = CursoManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('cursos:details', (), {'slug': self.slug})

class Meta:
    verbose_name = 'Cursos'
    verbose_name_plural = 'Cursos'
    ordering = ['name']