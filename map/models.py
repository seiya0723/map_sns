from django.db import models

from django.core.validators import MinValueValidator,MaxValueValidator


class Category(models.Model):

    name = models.CharField(verbose_name="カテゴリ名",max_length=20)

class Place(models.Model):

    comment = models.CharField(verbose_name="コメント",max_length=500)
    #category = models.CharField(verbose_name="カテゴリ名",max_length=20)

    category = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE)

    lat = models.DecimalField(verbose_name="緯度",max_digits=9, decimal_places=6)
    lon = models.DecimalField(verbose_name="経度",max_digits=9, decimal_places=6)
    photo = models.ImageField(verbose_name="写真", upload_to="map/place/photo",null=True,blank=True)

    #TODO:ここにユーザーを記録するフィールドを追加する。


    #モデルのメソッド( テンプレートで{{ place.hello }}と呼び出すことで実行できる )
    def hello(self):
        print("Hello!!")
        return "HelloWorld"

    #リプライ数をカウントして表示するメソッド。 {{ place.reply_amount }}で呼び出せる
    #selfを使い、Replyモデルから絞り込んで検索、.count()で数をカウントする
    def reply_amount(self):
        return Reply.objects.filter(place=self.id).count()


class Reply(models.Model):

    star = models.IntegerField(verbose_name="星",validators=[MinValueValidator(1),MaxValueValidator(5)])

    comment = models.CharField(verbose_name="コメント",max_length=500)
    place   = models.ForeignKey(Place,verbose_name="プレイス",on_delete=models.CASCADE)

    #TODO:ここにユーザーを記録するフィールドを追加する。




