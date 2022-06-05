"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&b54teu95g7^^d4u_$5eu$7o@z@$mqz^q9+bd#u*g+ku23^kh^'

# SECURITY WARNING: don't run with debug turned on in production!
#開発中はDEBUG=Trueにする。デプロイする時はDEBUG=Falseにする
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

#allauthの実装方法
#https://noauto-nolife.com/post/startup-django-allauth/

#django-allauth関係。django.contrib.sitesで使用するSITE_IDを指定する
SITE_ID = 1
#django-allauthログイン時とログアウト時のリダイレクトURL
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'


#djangoallauthでメールでユーザー認証する際に必要になる認証バックエンド
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

#ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD   = "email"

#ログイン時にユーザー名(ユーザーID)は使用しない
ACCOUNT_USERNAME_REQUIRED       = "False"

#ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VARIFICATION  = "mandatory"

#ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED= True


#Sendgridによるメール認証:https://noauto-nolife.com/post/django-sendgrid/
"""
EMAIL_BACKEND       = "sendgrid_backend.SendgridBackend"
DEFAULT_FROM_EMAIL  = "ここにデフォルトの送信元メールアドレスを指定"

SENDGRID_API_KEY    = "ここにsendgridのAPIkeyを記述する"
"""

#DEBUGがTrueのとき、メールの内容は全て端末に表示させる
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',  #
    'allauth',  #
    'allauth.account',  #
    'allauth.socialaccount',  #

    'map.apps.MapConfig',
    'users.apps.UsersConfig',

]
AUTH_USER_MODEL = 'users.CustomUser'
ACCOUNT_FORMS   = { "signup":"users.forms.SignupForm"}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/"templates",
                  BASE_DIR/"templates"/"allauth",
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

#Herokuにデプロイする時、STATICFILES_DIRSはDEBUGするときだけ有効にする
if DEBUG:
    STATICFILES_DIRS = [ BASE_DIR/"static"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL   = "/media/"
MEDIA_ROOT  = BASE_DIR / "media"



#以下choicesフィールドオプションの選択肢
SEX = [
    ("男性", "男性"),
    ("女性", "女性"),
    ("その他", "その他"),
]
PREFECTURES = [
    ("北海道"  ,"北海道"  ),
    ("青森県"  ,"青森県"  ),
    ("岩手県"  ,"岩手県"  ),
    ("宮城県"  ,"宮城県"  ),
    ("秋田県"  ,"秋田県"  ),
    ("山形県"  ,"山形県"  ),
    ("福島県"  ,"福島県"  ),
    ("茨城県"  ,"茨城県"  ),
    ("栃木県"  ,"栃木県"  ),
    ("群馬県"  ,"群馬県"  ),
    ("埼玉県"  ,"埼玉県"  ),
    ("千葉県"  ,"千葉県"  ),
    ("東京都"  ,"東京都"  ),
    ("神奈川県","神奈川県"),
    ("新潟県"  ,"新潟県"  ),
    ("富山県"  ,"富山県"  ),
    ("石川県"  ,"石川県"  ),
    ("福井県"  ,"福井県"  ),
    ("山梨県"  ,"山梨県"  ),
    ("長野県"  ,"長野県"  ),
    ("岐阜県"  ,"岐阜県"  ),
    ("静岡県"  ,"静岡県"  ),
    ("愛知県"  ,"愛知県"  ),
    ("三重県"  ,"三重県"  ),
    ("滋賀県"  ,"滋賀県"  ),
    ("京都府"  ,"京都府"  ),
    ("大阪府"  ,"大阪府"  ),
    ("兵庫県"  ,"兵庫県"  ),
    ("奈良県"  ,"奈良県"  ),
    ("和歌山県","和歌山県"),
    ("鳥取県"  ,"鳥取県"  ),
    ("島根県"  ,"島根県"  ),
    ("岡山県"  ,"岡山県"  ),
    ("広島県"  ,"広島県"  ),
    ("山口県"  ,"山口県"  ),
    ("徳島県"  ,"徳島県"  ),
    ("香川県"  ,"香川県"  ),
    ("愛媛県"  ,"愛媛県"  ),
    ("高知県"  ,"高知県"  ),
    ("福岡県"  ,"福岡県"  ),
    ("佐賀県"  ,"佐賀県"  ),
    ("長崎県"  ,"長崎県"  ),
    ("熊本県"  ,"熊本県"  ),
    ("大分県"  ,"大分県"  ),
    ("宮崎県"  ,"宮崎県"  ),
    ("鹿児島県","鹿児島県"),
    ("沖縄県"  ,"沖縄県"  ),
]








#Herokuデプロイ仕様の設定はDEBUG=Falseのときだけ有効にさせる
if not DEBUG:
    # INSTALLED_APPSにcloudinaryの追加
    INSTALLED_APPS.append('cloudinary')
    INSTALLED_APPS.append('cloudinary_storage')

    # ALLOWED_HOSTSにホスト名)を入力
    ALLOWED_HOSTS = ['.herokuapp.com']

    # 静的ファイル配信ミドルウェア、whitenoiseを使用。※ 順番不一致だと動かないため下記をそのままコピーする。
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # 静的ファイル(static)の存在場所を指定する。
    STATIC_ROOT = BASE_DIR / 'static'

    # DBの設定
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '5432',
        }
    }

    # DBのアクセス設定
    import dj_database_url

    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)

    # cloudinaryの設定
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': "",
        'API_KEY': "",
        'API_SECRET': "",
        "SECURE": True,
    }

    # これは画像だけ(上限20MB)
    # DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    # これは動画だけ(上限100MB)
    # DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.VideoMediaCloudinaryStorage'

    # これで全てのファイルがアップロード可能(上限20MB。ビュー側でアップロードファイル制限するなら基本これでいい)
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
