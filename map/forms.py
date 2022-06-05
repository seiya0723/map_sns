from django import forms

#TODO:Djangoのユーザーモデルではなく、カスタムユーザーモデルを用意する。
#from django.contrib.auth.models import User
from users.models import CustomUser


from .models import Place,Reply


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["comment","category","lat","lon","photo"]

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["comment","place","star"]


#ユーザーモデルを元にバリデーション用のフォームクラスを作る
class UserForm(forms.ModelForm):

    class Meta:
        model   = CustomUser
        fields  = [ "first_name","last_name" ]


#ユーザーモデルのプロフィールに関する項目
class UserProfileForm(forms.ModelForm):
    class Meta:
        model   = CustomUser
        fields  = [ "icon","birthday","introduction","nickname","sex","prefecture" ]



