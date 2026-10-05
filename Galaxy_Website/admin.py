from django.contrib import admin
from .models import Slidebar
from .models import HomeServiceCards, About, Contact

#Register Models
admin.site.register(Slidebar)
admin.site.register(HomeServiceCards)
admin.site.register(About)
admin.site.register(Contact)


