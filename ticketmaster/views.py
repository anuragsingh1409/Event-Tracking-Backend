from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event
from .services import get_events

    
class EventAPIview(APIView):
    def post(self, request):
        print(request.data)
        api_key = 'V3Yjd5F8oKpJCar0lf1ZJAAzj4qBZNVD'
        keyword = request.data['keyword']
        distance = request.data['distance']
        category = request.data['category']
        location = request.data['location']
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
          print(distance,location,category,keyword)
          events = get_events(api_key, keyword, distance, category,location)
        #   print(type(events))
          if events is not None:
            return Response(events)
          else:
            return Response({'error': 'Unable to retrieve events'})
    # def get(self, request):
    #     objs = Event.objects.all()
    #     #location = request.data.get("location")
    #     serializer = EventSerializer(objs,many=True)
    #     return Response({"message": "Got some data!","data":serializer.data})

    #     # print(e)
    #     # return Response({"message": "Got error data!", "error": serializer.error})

    # # return Response({"message": "Got some data!"})
