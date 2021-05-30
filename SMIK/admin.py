from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Gedung)
admin.site.register(models.Ruangan)
admin.site.register(models.Barang)
admin.site.register(models.FormPinjam)
admin.site.register(models.Peminjam)