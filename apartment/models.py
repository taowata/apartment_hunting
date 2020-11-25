from django.db import models


# Create your models here.

class Apartment(models.Model):
    """アパートモデル"""
    class Meta:
        db_table = "apartment"

    name = models.CharField(verbose_name='アパート名', max_length=255)
    goodNumber = models.IntegerField(verbose_name='いいね数')
    age = models.IntegerField(verbose_name='築年数', default=12)
    address = models.CharField(verbose_name='所在地', default='京都市左京区吉田本町', max_length=255)
    appearance = models.CharField(verbose_name='外観画像URL',
                                  default='https://image2.homes.jp/smallimg/image.php?file'
                                                                  '=http%3A%2F%2Fimage.homes.renters.jp%2F51bc6a50'
                                                                  '-5ad1-411e-b30e'
                                                                  '-b4643a59643c_property_picture_2347_large.jpg',
                                  max_length=2048)


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
