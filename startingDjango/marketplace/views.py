from django.shortcuts import render
from models import Item
# Create your views here.
class Items:
    def getAll(self):
        Item.objects.all()

# Круд для каждой модели, проверки на существование(наличие) в бд,
# Проверка на авторизован или нет, какие права, принцип AAA
# GET - getOne: TABLE(CLASS).objects.all().order_by('id')