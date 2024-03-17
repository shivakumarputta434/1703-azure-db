from django.shortcuts import render, HttpResponse

from .models import SiteUsers



def users(request, user_id):
    msg = 'i am here'
    name = SiteUsers.objects.get(id=user_id).name
    return HttpResponse(name)




# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import SiteUsers


# class GetUsers(APIView):
#     def get(self, request, user_id):
#         msg = 'i am here'
#         name = SiteUsers.objects.get(id=user_id).name
#         if name=='shiv':
#             return Response(msg)
#         users = SiteUsers.objects.all().values()
#         return Response(users)
#     def post(self, request, user_id):
#         id = user_id
#         name=request.data.get('name')
#         age = request.data.get('age')
#         user = SiteUsers(name=name, age=age)
#         user.save()
#         print("name***************************",name)
#         return Response("success")
#     def put(self, request, user_id):
#         user = SiteUsers.objects.get(id=user_id)
#         user.name = 'srinivas'
#         user.save()
#         return Response("success")
#     def delete(self, request, user_id):
#         user = SiteUsers.objects.get(id=user_id)
        
#         user.delete()
#         return Response("success")
    
# class GetUsers1(APIView):
#     def get(self, request):
#         msg = 'i am here'
#         return Response(msg)



    