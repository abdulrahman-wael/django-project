
what was built step-by-step?

# Setting up & First app

1. django start
2. create app (core)

   1. link inside settings: INSTALLED APPS
   2. create HTML inside templates/core: base, index, contact
   3. create views: linked to it
   4. add to urls.py
3. startapp items

   1. settings: INSTALL APPS
   2. models: class Category: name = CharField + max_length, Meta: verbose_name_plural, ordering, __ str __(self)
      1. admin.py: import Category, admin.site.register
      2. makemigrations, migrate
   3. createsuperuser, login in admin interface
      1. add data inside admin
   4. models: Item (name CharField, description TextField, price FloatField, is_sold BooleanField, create_at DateTimeField auto_now_add, created_by ForienKey related_name on_delete, category ForienKey related_name on_delete, image ImageField upload_to)
      1. from django.contrib.auth.models import Users
      2. for images: pip install pillow
         1. settings.py: MEDIA_URL, MEDIA_ROOT
      3. startmigrations, migrate
      4. admin.py import Items, admin.site.register()
         1. login + add items
   5. views.py: import item.models.Category, Item
      1. def index: Item.objects.filter(is_sold=True)[:6], Category.objects.all, return(,,{'categories': categories, })
   6. update index.html with the required code view both items, categories then [add settings.MEDIA_ROOT, settings.MEDIA_URL to the urls.py file (DEV-ONLY TRICK)]
      1. 2 div with class = mt-6 px-6 py-12 bg-gray-100 round-xl
      2. 2 h2 with class = mb-12 text-2xl text-center
      3. 2 div with class = grid grid-cols-3 gap-3
      4. {% for item or category in categories or items %} {% endfor %}
      5. < div >
         1. < a >
            1. < div >
               1. < img source class >
            2. < div class >
               1. h2 class (item.name)
               2. p class (price)
      6. create detail.html page
         1. connect it to views.py file (inside the items folder)
         2. create a urls.py and connect it to the main urls.py
         3. connect to index.html page
4. after finishing the basic browsing now comes handling users

   1. inside the core app: create a urls.py for consistency + connect to the main urls.py
      1. create a form.py inside the core and connect it to the views.py file
      2. create a signup.html page and connect it to the views.py
   2. modify signup.html to create a login.html and connect with urls.py and views.py
