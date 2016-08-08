def decorator(func_to_decorate):
    def some():
        return 'decoration' + func_to_decorate() + 'decoration'
    return some

@decorator
def f():
    return 'marek'


print(f())
# # f = decorator(f)
# print(f())


{% extends 'rango/base.html' %}

{% load staticfiles %}

{% block title %}{% endblock %}

{% block body_block %}

{% endblock %}
