from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework import serializers
from .models import Match,Markets,Sport,Selections
import django_filters


#Serializers

class SelectionsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Selections

class MarketsSerializer(serializers.ModelSerializer):
    selections = SelectionsSerializer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = Markets

#Filters

class MatchFilter(django_filters.FilterSet):
    sport = django_filters.CharFilter(field_name='sport__name', lookup_expr='icontains')

    class Meta:
        model = Match
        fields=["sport"]
        order_by = ['start_time']


#Views


@api_view(['GET'])
def retriveMatch(request,id):
    match = Match.objects.get(id=id)

    context_dict = {
        "id":match.id,
        "url":match.url,
        "name":match.name,
        "startTime":match.start_time.strftime("%m/%d/%Y, %H:%M:%S"),

        "sport": {
            "id":match.sport_id,
            "name":match.sport.name
        },
        "markets":MarketsSerializer(match.markets,many=True).data

    }
    return Response(context_dict)

@api_view(['GET'])
def listMatch(request):
    f = MatchFilter(request.GET, queryset=Match.objects.all())
    values = f.qs.values("id","url","name","start_time")
    return  Response(values)



@api_view(['GET','POST'])
def Event(request):
    if request.data["message_type"] == "NewEvent":
        selection_ids = []
        selections = request.data["event"]["markets"]["selections"]
        for each in selections:
            s = Selections.objects.create(**each)
            s.save()
            selection_ids.append(s)

        market = Markets()
        market.id = request.data["event"]["markets"]["id"]
        market.name = request.data["event"]["markets"]["name"]
        market.selections.add(*selection_ids)
        market.save()

        match = Match()
        match.id = request.data["event"]["id"]
        match.url = "http://127.0.0.1:8000/api/match/"+str(match.id)
        match.name = request.data["event"]["name"]
        match.start_time = datetime.strptime(request.data["event"]["startTime"], "%Y-%m-%d %H:%M")

        sport, sport_created = Sport.objects.get_or_create(id=request.data["event"]["sport"]["id"])
        if sport_created:
            sport.name = request.data["event"]["sport"]["name"]
            sport.save()

        match.sport = sport
        match.markets.add(market)
        match.save()
        return  Response({"status":"success"})

    if request.data["message_type"] == "UpdateOdds":
        
        selections = request.data["event"]["markets"]["selections"]
        for each in selections:
            s = Selections.objects.get(id=each["id"])
            s.odds = each["odds"]
            s.save()


        return Response({"status": "success"})





