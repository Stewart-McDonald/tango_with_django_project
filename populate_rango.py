import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "https://docs.python.org/2/tutorial/",
         "views": 21},
        {"title": "How to Think like a Computer Scientist",
         "url": "https://www.greenteapress.com/thinkpython/",
         "views": 20},
        {"title": "Learn Python in 10 Minutes",
         "url": "https://www.korokithakis.net/tutorials/python/",
         "views": 45}
    ]

    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views": 7},
        {"title": "Django Rocks",
         "url": "https://www.djangorocks.com/",
         "views": 3},
        {"title": "How to Tango with Django",
         "url": "https://www.tangowithdjango.com/",
         "views": 0}
    ]

    other_pages = [
        {"title": "Bottle",
         "url": "https://bottlepy.org/docs/dev/",
         "views": 1},
        {"title": "Flask",
         "url": "https://flask.pocoo.org",
         "views": 0}
    ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    for cat, cat_data in cats.items():
        curCat = add_cat(cat, views=cat_data["views"], likes=cat_data["likes"])
        for page in cat_data["pages"]:
            add_page(curCat, page["title"], page["url"], page["views"])

    for curCat in Category.objects.all():
        for page in Page.objects.filter(category=curCat):
            print("- {0} - {1}".format(str(curCat), str(page)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
    p.views = views
    p.url = url
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
