from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Forecast
from .serializers import ForecastSerializer

class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, pk):
        try:
            forecast = Forecast.objects.get(pk=pk)
            serializer = ForecastSerializer(forecast)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Forecast.DoesNotExist:
            return Response({"message": "Прогноз не найден."}, status=status.HTTP_404_NOT_FOUND)