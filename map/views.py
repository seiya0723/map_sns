from django.shortcuts import render,redirect
from django.views import View



#from django.contrib.auth.models import User
from users.models import CustomUser as User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


from .models import Category,Place,Reply
from .forms import PlaceForm,ReplyForm,UserForm,UserProfileForm


from django.conf import settings

from django.contrib import messages


#未認証ユーザーはこのビューを実行せず、ログインページへリダイレクトする。
#class IndexView(LoginRequiredMixin,View):

class IndexView(View):
    def get(self,request,*args,**kwargs):

        context = {}
        query = Q()

        #リクエストボディを参照する時、存在しないキーを指定するとエラーになる。そのため、予めキーが存在するかチェックする
        if "search" in request.GET:
            print(request.GET["search"])
            # TODO:ここで検索実行

            #comment=request.GET["search"]では完全一致のみ
            #context["places"] = Place.objects.filter(comment=request.GET["search"])

            #comment__icontains=request.GET["search"]では、request.GET["search"]を含むcommentを
            #これだと、スペースも文字列の一部として考えられるので、スペース区切りの検索ができない
            #context["places"] = Place.objects.filter(comment__icontains=request.GET["search"])

            #.split()は引数に指定した文字列で区切ってリストにする。"Django 道場"なら["Django","道場"]となる
            #.replace("A","B")は文字列のAをBに置き換える。全角スペースを半角スペースに統一
            raw_words   = request.GET["search"].replace("　"," ").split(" ")
            print(raw_words)

            words = []
            # 1つずつ取り出す
            for w in raw_words:
                #空文字列ではない文字列であれば、wordsに追加する
                if w != "":
                    words.append(w)

            print(words)

            #Q()の引数内にfilterに記述する条件式を書く

            for w in words:
                # &= とすることで、追加の条件を指定(AND検索)できる。 |= とすることでOR検索ができる
                query &= Q(comment__icontains=w)

        """
        else:
            print("検索の指定なし")
            #検索の指定のない場合は全件表示
            context["places"] = Place.objects.all()
        """

        #TODO:ここに追加の絞り込みを追記(画像の有無、カテゴリ検索、リプライ数、星の数など)



        # できあがった条件式で絞り込む(検索していない時は、query=Q()なので、全部出てくる)
        context["places"] = Place.objects.filter(query)
        context["categories"]   = Category.objects.all()


        return render(request,"map/index.html",context)

    def post(self,request,*args,**kwargs):

        if not request.user.is_authenticated:
            print("未認証につき投稿は拒否されました")
            return redirect("account_login")

        form = PlaceForm(request.POST,request.FILES)

        if form.is_valid():
            messages.info(request, "投稿受け付けました")
            form.save()
        else:
            messages.error(request, form.errors)

        return redirect("map:index")

index=IndexView.as_view()


class ReplyView(View):
    def get(self, request, pk, *args, **kwargs):
        #print(pk)
        context = {}
        context["places"]   = Place.objects.filter(id=pk)
        context["replies"]  = Reply.objects.filter(place=pk)

        return render(request, "map/reply.html",context)

    def post(self, request, pk, *args, **kwargs):

        # { "comment":"aaaa","place":pk }

        #requestオブジェクトは書き換え不可能なため、placeを追加する処理はエラーになる
        #request.POST["place"] = pk

        copied          = request.POST.copy()  # 書き換えを可能にするためコピーオブジェクトを作る { "comment":"aaaa" }
        copied["place"] = pk                   # placeを追加する { "comment":"aaaa","place":pk }

        form = ReplyForm(copied)

        #ここでバリデーションをする(commentとplace)
        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

        return redirect("map:reply", pk)

reply   = ReplyView.as_view()


class MyPageView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):

        #TODO:フォームの性別と都道府県の選択肢を提供

        context = {}

        context["sex"]          = [ s[0] for s in User.sex.field.choices ]
        context["prefectures"]  = [ p[0] for p in User.prefecture.field.choices ]

        return render(request,"map/mypage.html")

    def post(self, request, *args, **kwargs):
        #TODO:ここで、ユーザー情報の記録をする。

        #ユーザーモデルの編集を行うため、まずは対象のモデルオブジェクトを特定する
        user    = User.objects.filter(id=request.user.id).first()

        form    = UserForm(request.POST,instance=user)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)


        #プロフィール関係のバリデーション
        form    = UserProfileForm(request.POST, instance=user)
            
        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print(form.errors)



        return redirect("map:mypage")

mypage  = MyPageView.as_view()


