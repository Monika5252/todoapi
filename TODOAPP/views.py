from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail,EmailMessage




from . serializers import *

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.



def sendmail(request):
    subject="Thank you for registering for this site"
    message="welcome"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['zendeshubham11@gmail.com']
    send_mail=EmailMessage (subject,message,email_from,recipient_list)
    send_mail.attach_file('emp2.jpg')
    send_mail.send()
    return HttpResponse('Email send successfully')
class TodoAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return  Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise
    def get(self,request,pk=None,format=None):
        if pk:
            data=self.get_object(pk)
            serializer=TodoSerializer(data)
            return Response(serializer.data)

        else:
            data=Todo.objects.all()
            serializer=TodoSerializer(data,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        data=request.data
        serializer=TodoSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        response=Response()
        response.data={
            'message':'Todo Created Successfully',
            'data':serializer.data
        }
        return response

    def put(self, request,pk=None, format=None):
        todo_to_update=Todo.objects.get(pk=pk)
        serializer = TodoSerializer(instance=todo_to_update,data=request.data,partial=True)

        serializer.is_valid()
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }
        return response
    def delete(self, request,pk,format=None):
        todo_to_delete=Todo.objects.get(pk=pk)
        todo_to_delete.delete()
        return Response({
            'message':'Todo deleted successfully'
        })
    # def get(self,request,pk,format=None):
    #     if pk:
    #         data=self.get_object(pk)
    #         serializer=TodoSerializer(data)
    #         return Response(serializer.data)
    #
    #     else:
    #         data=Todo.objects.all()
    #         serializer=TodoSerializer(data,many=True)
    #         return Response(serializer.data)



class Register(APIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer=userSerializers(data=request.data)

        if not serializer.is_valid():
            return Response({'status':404 ,'errors':serializer.errors,'message':'Something wrong '})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        #create token
        # token_user ,_=Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user=user)

        return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),'message':'your data saved'})

    # def get(self,request,pk=None,format=None):
    #     if pk:
    #         data=self.get_object(pk)
    #         serializer=TodoSerializer(data)
    #         return Response(serializer.data)
    #
    #     else:
    #         data=Todo.objects.all()
    #         serializer=TodoSerializer(data,many=True)
    #         return Response(serializer.data)
        # if not serializer.is_valid():
        #     return Response({'status':404 ,'errors':serializer.errors,'message':'Something wrong '})
        # serializer.save()
        # user=Modules.objects.get(username=serializer.data['username'])
        # #create token
        # # token_user ,_=Token.objects.get_or_create(user=user)
        # refresh = RefreshToken.for_user(user=user)
        #
        # return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        # 'access': str(refresh.access_token),'message':'your data saved'})

