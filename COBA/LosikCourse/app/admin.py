from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.siswa)
admin.site.register(models.CustomerService)
admin.site.register(models.Transaksi)
admin.site.register(models.Kelas_Mata_Kursus)
admin.site.register(models.Registrasi)