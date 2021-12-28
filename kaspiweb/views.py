from decimal import Decimal

from uuid import uuid4
from django.http import HttpResponse
from django.shortcuts import render

from accounts.account import Account
from database.implementations.sqlite import AccountDatabaseSqlite

db = AccountDatabaseSqlite('db.sqlite3')
kzt_acc = Account.random_kzt()
usd_acc = Account.random_usd()
eur_acc = Account.random_eur()


def index(request):
    a = request.GET.get("your_balance")
    b = request.GET.get("accId")
    c = request.GET.get("toId")
    d = request.GET.get("fromId")
    e = request.GET.get("balance")
    return render(request, 'index.html', context={
        'accounts': db.get_accounts(),
        'max_kzt': db.max_balance_kzt(),
        'max_usd': db.max_balance_usd(),
        'max_eur': db.max_balance_eur(),
        'curr_eur': 'EUR',
        'curr_usd': 'USD',
        'curr_kzt': 'KZT',
        'add_ball': db.add_balance(b, a),
        'send_ball': db.send_balance(d, c, e)

    })


def add_kzt_acc(request):
    return render(request, 'add_acc.html', context={'kzt_new': db.new_acc(kzt_acc)})


def add_usd_acc(request):
    return render(request, 'add_acc.html', context={'usd_new': db.new_acc(usd_acc)})


def add_eur_acc(request):
    return render(request, 'add_acc.html', context={'eur_new': db.new_acc(eur_acc)})