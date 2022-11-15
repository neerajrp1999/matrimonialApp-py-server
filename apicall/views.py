from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import FCMManager as fcm

@api_view(['GET', 'POST'])
def n_sender(request):
    tokens=request.GET.get('tokenS',None)
    titleS=request.GET.get('titleS',None)
    messageS=request.GET.get('messageS',None)
    #tokens1="c4bDYJueQPqVsFURrNwNZz:APA91bFZESpXtF3nk4O632HkJ2fTMFqlllrj6Jri1_3zWmeUMvKJxhEE_Rnxft1TbAwdyf8fBZtgJeID_x32UY6pExbOEh79FpwPlLCCrEzbMduTDZO91fIuaaNd1l8Scd-zWMHPAFyR"
    response=fcm.sendPush(titleS, messageS, [str(tokens)])
    
    return JsonResponse({"Response":"Done"})
