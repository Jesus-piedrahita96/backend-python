# importaciones de django

from django.views import View
from django.http.response import JsonResponse

# simula el trabajo con csrf

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Company

# importacion propia de python

import json

# Create your views here.


class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            companies = list(Company.objects.filter(pk=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {
                    'message': 'seccess',
                    'company': company
                }
            else:
                datos = {'message': 'companies not found...'}

            return JsonResponse(datos)

        else:
            companies = list(Company.objects.values())

            if len(companies) > 0:
                datos = {
                    'message': 'seccess',
                    'companies': companies
                }
            else:
                datos = {'message': 'companies not found...'}

            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(
            name=jd['name'],
            web_site=jd['web_site'],
            foundation=jd['foundation']
        )
        datos = {'message': 'success'}

        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(pk=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.web_site = jd['web_site']
            company.foundation = jd['foundation']
            company.save()
            datos = {'message': 'seccess'}

        else:
            datos = {'message': 'companies not found...'}

        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(pk=id).values())
        if len(companies) > 0:
            Company.objects.get(pk=id).delete()
            datos = {'message': 'seccess'}

        else:
            datos = {'message': 'companies not found...'}

        return JsonResponse(datos)
