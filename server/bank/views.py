from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from .models import Family, Member
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django.http import HttpResponse
from django.db import transaction

# Create your views here.

def index(request):
    context = Family.objects.all()
    return render(request, 'bank/index.html', {'contex': context})


def family(request, family_id):

    context = {'family': Family.objects.get(pk=family_id)}
    return render(request, 'bank/family.html', context)


def member(request, member_id):
    if request.method == 'POST':
        if request.POST:
            amount = request.POST.get("amount")
            member = Member.objects.get(pk=member_id)
            type = request.POST.get("type")
            print(amount)
            print(type)
            if amount:
                if type == "charge":
                    member.set_bank(( member.bank + int(amount)))
                    member.family.set_bank( member.family.bank - int(amount))
                else:
                    member.set_bank(member.bank - int(amount))
                    member.family.set_bank(member.family.bank + int(amount))
            member.save()
            member.family.save()

    context = {'member': Member.objects.get(pk=member_id)}
    return render(request, 'bank/member.html', context)


def handleRequestAndMoveMoney(request, member_id, type):
    amount = int(QueryDict(request.body).get('amount'))
    member = Member.objects.get(pk=member_id)

    if type == 'charge':
        member.bank += amount
        member.family -= amount
    else:
        member.bank -= amount
        member.family += amount


def charge(request, member_id):
    if request.method == 'GET':
        form = request.GET
        if form.is_valid():
            amount = int(form.get('amount'))
            member = Member.objects.get(pk=member_id)

            member.bank += amount
            member.family -= amount

            context = {'member': Member.objects.get(pk=member_id)}
    return render(request, 'bank/index.html', context)


def withdraw(request, member_id):
    if request.method == 'GET':
        form = request.GET
        if form.is_valid():
            amount = int(form.get('amount'))
            member = Member.objects.get(pk=member_id)

            member.bank -= amount
            member.family += amount

            context = {'member': Member.objects.get(pk=member_id)}
    return render(request, 'bank/index.html', context)

