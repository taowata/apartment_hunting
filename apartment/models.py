from django.db import models


# Create your models here.

class Apartment(models.Model):
    """アパートモデル"""
    class Meta:
        db_table = "apartment"

    name = models.CharField(verbose_name='アパート名', max_length=255)
    goodNumber = models.IntegerField(verbose_name='いいね数')


class Room(models.Model):
    """部屋モデル"""
    class Meta:
        db_table = 'room'

    apartment = models.ForeignKey(Apartment, verbose_name='アパート',
                                  on_delete=models.PROTECT)
    number = models.IntegerField(verbose_name='部屋番号')
    isRentable = models.BooleanField(verbose_name='空部屋かどうか')
    rent = models.IntegerField(verbose_name='家賃')
    floorPlan = models.CharField(verbose_name='間取り', max_length=255)
    areBathAndToiletSeparated = models.BooleanField(verbose_name='バストイレ')
    age = models.IntegerField(verbose_name='築年数')
    buildingStructure = models.CharField(verbose_name='建物構造', max_length=255)
