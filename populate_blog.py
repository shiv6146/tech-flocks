import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

import django
django.setup()

from blog.models import Tag, Post


def populate():
    tag_python = add_tag('#Python')

    add_post(tag=tag_python,
        title="Official Python Tutorial",
        content="http://docs.python.org/2/tutorial/")

    add_post(tag=tag_python,
        title="How to Think like a Computer Scientist",
        content="http://www.greenteapress.com/thinkpython/")

    add_post(tag=tag_python,
        title="Learn Python in 10 Minutes",
        content="http://www.korokithakis.net/tutorials/python/")

    tag_django = add_tag("#Django")

    add_post(tag=tag_django,
        title="Official Django Tutorial",
        content="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    tag_other = add_tag("#Others")

    add_post(tag=tag_other,
        title="Bottle",
        content="http://bottlepy.org/docs/dev/")

    add_post(tag=tag_other,
        title="Flask",
        content="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for t in Tag.objects.all():
        for p in Post.objects.filter(tag=t):
            print "- {0} - {1}".format(str(t), str(p))

def add_post(tag, title, content, likes=0):
    p = Post.objects.get_or_create(tag=tag, title=title, content=content, likes=likes)[0]
    return p

def add_tag(name):
    t = Tag.objects.get_or_create(name=name)[0]
    return t

# Start execution here!
if __name__ == '__main__':
    print "Starting Blog population script..."
    populate()