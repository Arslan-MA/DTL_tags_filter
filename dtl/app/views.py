from django.shortcuts import render


def index_page(request):
    foods = [
        {'name': 'Apple', 'category': 'Fruit'},
        {'name': 'Banana', 'category': 'Fruit'},
        {'name': 'Corn', 'category': 'Vegetable'},
        {'name': 'Grape', 'category': 'Fruit'},
        {'name': 'Hamburger', 'category': 'Meat'},
        {'name': 'Pepper', 'category': 'Vegetable'},
    ]

    blurb = '<p>You are <em>pretty</em> smart!</p>'

    blurb_text = 'You are pretty smart!'

    context = {'value': 'Joel\nis a slug',
               'text': blurb_text,
               'foods': foods,
               'url': 'http://127.0.0.1:8000/urlize/',
               'value_default': '',
               'blurb': blurb,
               'var': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
               'value_num': 123456789,
               'list': ['a', 'b', 'c'],
               'number': 21,
               'object': {
                   'name': 'John',
                   'age': 25,
               }}
    return render(request, 'app/index.html', context)


def test_urlize(request):
    return render(request, "app/urlize.html")

