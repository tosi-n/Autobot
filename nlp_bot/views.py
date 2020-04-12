from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Bitron
from .serializers import BitronSerializer
from simpletransformers.classification import ClassificationModel
import pandas as pd
import json
import logging
import sklearn

# Create your views here.
class BitronView(viewsets.ModelViewSet):
	queryset = Bitron.objects.all()
	serializer_class = BitronSerializer

@api_view(["POST"])
def binatron(request):
    try:
        inport=request.data
        inport = [inport["eligible_text"]]
        # inport = list(inport.values())
        model=ClassificationModel("bert", "outputs", use_cuda=False)
        predictions, raw_outputs = model.predict(inport)
        df=pd.DataFrame(predictions, columns=['Criteria'])
        df=df.replace({1:'Eligible', 0:'Others'})
        df = df.to_dict()['Criteria'].get(0)
        return JsonResponse('Text Belongs to Class {}'.format(df), safe=False)
        # 
        # return df
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
