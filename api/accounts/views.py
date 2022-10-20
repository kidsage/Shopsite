# from rest_framework import status
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView

# Create your views here.

# update에 사용할 코드
# def update(self, request, *args, **kwargs):
#     serializer = self.serializer_class(request.user, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_200_OK)


""" 테스트용 코드
class ProfileViewSet(ViewSet):

    def partial_update(self, request, pk=None):    #partially update the profile

        try:
            user_detail = user_reg.objects.get(pk=pk)
           
            serializer = RegisterSerializer(user_detail,data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({'data':'internal server error','message':'error aa gyi'},500)

            serializer.save()

        except Exception as e:

            return Response('some exception occured' + str(e))

        return Response('record Updated successfully')

    def retrieve(self,request, pk=None):    #get or retrieve the profile from database

        queryset = user_reg.objects.get(pk=pk)
    
        serializer_class = RegisterSerializer(queryset)
    
        return Response(serializer_class.data)
"""