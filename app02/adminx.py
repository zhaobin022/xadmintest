import xadmin

from .models import *

class AlbumInline(object):
    model = Album
    extra = 0

class MusicianAdmin(object):
    inlines = [AlbumInline]

    exclude = ('instrument',)
    relfield_style = 'fk-ajax'

    pass
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # instrument = models.CharField(max_length=100)

class AlbumAdmin(object):
    list_display = ('artist', 'name', 'release_date', 'num_stars', )
    list_editable = ('artist',"name", "release_date",)

    list_filter = ['artist', ]


    pass
    # artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # release_date = models.DateField()
    # num_stars = models.IntegerField()


class AlbumAdmin2(object):
    exclude = ('artist',)
    def queryset(self):

        qs = super(AlbumAdmin2,self).queryset()
        qs =  qs.filter(name='11')
        return qs
    pass
    # artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # release_date = models.DateField()
    # num_stars = models.IntegerField()

class ToppingAdmin(object):
    pass
    # ...
    # name = models.CharField(max_length=100)


class PizzaAdmin(object):
    list_display = ('toppings', 'contents', 'name',  )
    list_editable = ('toppings', 'contents', 'name',  )


    style_fields = {
        'toppings': 'm2m_transfer',
        'contents':'ueditor',
    }

    # ...
    # toppings = models.ManyToManyField(Topping)

xadmin.site.register(Musician,MusicianAdmin)
xadmin.site.register(Album,AlbumAdmin)
xadmin.site.register(Album2,AlbumAdmin2)
xadmin.site.register(Topping,ToppingAdmin)
xadmin.site.register(Pizza,PizzaAdmin)
