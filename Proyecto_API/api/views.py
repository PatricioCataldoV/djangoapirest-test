from typing import Any
from django import http
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Variables
import json

# Create your views here.

class VariablesView(View):

    @method_decorator(csrf_exempt)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            listvariables=(list(Variables.objects.filter(id=id).values()))
            if len(listvariables) > 0:
                variable=listvariables[0]
                datos={'mensaje' : "Exito", 'Variable': variable}
            else:
                datos={'mensaje': "Variable no encontrada..."}
            return JsonResponse(datos)
        else:
            listvariables= list(Variables.objects.values())
            if len(listvariables) > 0:
                datos={'mensaje' : "Exito", 'Variables': listvariables}
            else:
                datos={'mensaje' : "Lista de variables no encontrada..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Variables.objects.create(nombre=jd['nombre'], var1=jd['var1'], var2=jd['var2'], var3=jd['var3'], var4=jd['var4'], var5=jd['var5'], var6=jd['var6'], var7=jd['var7'], var8=jd['var8'], var9=jd['var9'], var10=jd['var10'], var11=jd['var11'], var12=jd['var12'], var13=jd['var13'], var14=jd['var14'], var15=jd['var15'], var16=jd['var16'], var17=jd['var17'], var18=jd['var18'], var19=jd['var19'], var20=jd['var20'], var21=jd['var21'], var22=jd['var22'], var23=jd['var23'], var24=jd['var24'], var25=jd['var25'], var26=jd['var26'], var27=jd['var27'], var28=jd['var28'], var29=jd['var29'], var30=jd['var30'])
        datos = {'mensaje' : "Exito"}
        return JsonResponse(datos)
    
    def put(self, request ,id):
        jd = json.loads(request.body)
        listvariables=(list(Variables.objects.filter(id=id).values()))
        if len(listvariables) > 0:
            variable=Variables.objects.get(id=id)
            variable.nombre = jd['nombre']
            variable.var1 = jd['var1']
            variable.var2 = jd['var2']
            variable.var3 = jd['var3']
            variable.var4 = jd['var4']
            variable.var5 = jd['var5']
            variable.var6 = jd['var6']
            variable.var7 = jd['var7']
            variable.var8 = jd['var8']
            variable.var9 = jd['var9']
            variable.var10 = jd['var10']
            variable.var11 = jd['var11']
            variable.var12 = jd['var12']
            variable.var13 = jd['var13']
            variable.var14 = jd['var14']
            variable.var15 = jd['var15']
            variable.var16 = jd['var16']
            variable.var17 = jd['var17']
            variable.var18 = jd['var18']
            variable.var19 = jd['var19']
            variable.var20 = jd['var20']
            variable.var21 = jd['var21']
            variable.var22 = jd['var22']
            variable.var23 = jd['var23']
            variable.var24 = jd['var24']
            variable.var25 = jd['var25']
            variable.var26 = jd['var26']
            variable.var27 = jd['var27']
            variable.var28 = jd['var28']
            variable.var29 = jd['var29']
            variable.var30 = jd['var30']
            variable.save()
            datos = {'mensaje' : "Exito"}
        else:
            datos={'mensaje': "Variable no encontrada..."}
        return JsonResponse(datos)
        
    
    def delete(self, request,id):
        listvariables=(list(Variables.objects.filter(id=id).values()))
        if len(listvariables) > 0:
            Variables.objects.filter(id=id).delete()
            datos = {'mensaje' : "Exito"}
        else:
            datos={'mensaje': "Variable no encontrada..."}
        return JsonResponse(datos)