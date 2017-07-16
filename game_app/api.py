from pygments.util import xrange
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response

from game_app.serializers import *
from .models import *
import random
from django.apps import apps





MAX_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
PLAYER_LIST = ['person1', 'person2', 'person3', 'person4', 'person5', 'person6', 'person7', 'person8']


def get_current_model(request):
    model_dict={'person1':'Person1','person2':'Person2','person3':'Person3','person4':'Person4','person5':'Person5'
    ,'person6':'Person6','person7':'Person7','person8':'Person8'}
    model_name=model_dict[request]
    model = apps.get_model('game_app', model_name)
    print(type(model),"!@#$%^&*()#$%^&*(#$%^&*($%^&*()")
    return model

def game(player1,player2):
    first_model = get_current_model(player1)
    second_model = get_current_model(player2)

    if first_model.name=='person1':
        qset=Person1.objects.get(id=1)
    elif first_model.name=='person2':
        qset=Person2.objects.get(id=1)
    elif first_model.name=='person3':
        qset=Person3.objects.get(id=1)
    elif first_model.name=='person4':
        qset=Person4.objects.get(id=1)
    elif first_model.name=='person5':
        qset=Person5.objects.get(id=1)
    elif first_model.name=='person6':
        qset=Person6.objects.get(id=1)
    elif first_model.name=='person7':
        qset=Person7.objects.get(id=1)
    else :
        qset=Person8.objects.get(id=1)

    if second_model.name == 'person1':
        qset2 = Person1.objects.get(id=1)
    elif second_model.name == 'person2':
        qset2 = Person2.objects.get(id=1)
    elif second_model.name == 'person3':
        qset2 = Person3.objects.get(id=1)
    elif second_model.name == 'person4':
        qset2 = Person4.objects.get(id=1)
    elif second_model.name == 'person5':
        qset2 = Person5.objects.get(id=1)
    elif second_model.name == 'person6':
        qset2 = Person6.objects.get(id=1)
    elif second_model.name == 'person7':
        qset2 = Person7.objects.get(id=1)
    elif second_model.name == 'person8':
        qset2 = Person8.objects.get(id=1)

    count = 0
    game_count=0
    qset.playing=True
    qset2.playing=True

    nu1=qset.game_number
    qset.game_number=nu1+1

    nu2=qset2.game_number
    qset2.game_number=nu2+1

    qset.role='defencer'
    qset2.role='attacker'

    while (qset.point!=5 or qset2.point!=5):
        if qset.role=='defencer':

            my_randoms = random.sample(xrange(1, 11), first_model.array_length)
            qset.defense_array=my_randoms
            guess = random.choice(MAX_ARRAY)

        elif qset2.role=='defencer':


            my_randoms2 = random.sample(xrange(1, 11), second_model.array_length)
            qset2.defense_array = my_randoms
            guess2 = random.choice(MAX_ARRAY)
        # if guess2 in my_randoms2:

        if guess in my_randoms:
            qset2.role='defencer'
            arr2=qset2.defense_array

        else:
            count+=1
            qset.point+=1

    if qset.point==5:
        return first_model.name
    elif qset2.point==5:
        return second_model.name



class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

    @list_route(methods=["GET"])
    def first_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)

        return Response("First Match")

    @list_route(methods=["GET"])
    def second_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)

        return Response("Second Match")

    @list_route(methods=["GET"])
    def third_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)

        return Response("Third Match")

    @list_route(methods=["GET"])
    def fourth_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)

        return Response("Fourth Match")

