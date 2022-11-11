from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import FCMManager as fcm

@api_view(['GET', 'POST'])
def n_sender(request):
    tokens=request.GET.get('tokenS',None)
    #tokens="fojmRGl-RcCsiy_MPWMebG:APA91bHR9PP-l6iVEsR4P2HK3TsiAlRPCq6C3JvF9Tef2ro9AHQ5fUWOQiOf5cp0V624Txa7b2D0IQVt8GeiPZcOxng66b0vbM3L5QSuB08psgPovnAfPImwrMT-3virqlbZGmfxQyj9"
    #tokens1="c4bDYJueQPqVsFURrNwNZz:APA91bFZESpXtF3nk4O632HkJ2fTMFqlllrj6Jri1_3zWmeUMvKJxhEE_Rnxft1TbAwdyf8fBZtgJeID_x32UY6pExbOEh79FpwPlLCCrEzbMduTDZO91fIuaaNd1l8Scd-zWMHPAFyR"
    titleS=request.GET.get('titleS',None)
    messageS=request.GET.get('messageS',None)
    response=fcm.sendPush(titleS, messageS, [str(tokens)])
    
    return JsonResponse({"Response":"Done"})