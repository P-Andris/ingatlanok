from django.db import models

class Kategoria(models.Model):
    nev = models.CharField(max_length = 30, verbose_name = 'Név')

    def __str__(self):
        return self.nev
    
class Ingatlan(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete = models.CASCADE, verbose_name = 'Kategória')
    leiras = models.TextField(null = True, blank = True, verbose_name = 'Leírás')
    hirdetes_datuma = models.DateField(null = True, blank = True, verbose_name = 'Hirdetés ideje')
    tehermentes = models.BooleanField(verbose_name = 'Tehermentes')
    ar = models.IntegerField(verbose_name = 'Ár')
    kep_url = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Kép URL')