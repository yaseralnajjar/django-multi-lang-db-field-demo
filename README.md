# What is this?

A simple demo to show the usage of django-i18nfield to have multiple language fields.

# How does it work?

Getting and settings the data is in `articles/views.py`.

```
def index(request):

    translation.activate('ar')
    article = Article.objects.all()[0]

    return HttpResponse(article.title)

def change(request):

    translation.activate('ar')
    article = Article.objects.all()[0]

    article.title.data['ar'] = 'مرحباً'
    article.save()

    return HttpResponse(article.title)
```

# Used packages

`django-i18nfield` is the main package here.

You can get more info here about the package: https://github.com/raphaelm/django-i18nfield/

# Running the project (Windows specific)

```
virtualenv venv
call venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```