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
    print(model.name,"!@#$%^&*()#$%^&*(#$%^&*($%^&*()")
    return model

def game(player1,player2):
    first_model = get_current_model(player1)
    second_model = get_current_model(player2)

    my_randoms = random.sample(xrange(1, 11), first_model.array_length)
    print("random list-------------", my_randoms)
    guess=random.choice(MAX_ARRAY)
    print("random guess---------------",guess)
    count=0
    while (first_model.score==5 or second_model.score==5):
        if guess in my_randoms:
            my_randoms2 = random.sample(xrange(1, 11), second_model.array_length)
            guess2=random.choice(MAX_ARRAY)
        else:
            first_model.score+=1

    my_randoms2 = random.sample(xrange(1, 11), second_model.array_length)
    print("22222222222222222222222", my_randoms)


class RefereeViewSet(viewsets.ModelViewSet):
    print("@@@@@@@@@@@@@@@@@@@")
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

    @list_route(methods=["GET"])
    def first_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)
        # print("%%%%%%%%%%%%%%%%%%%%%",first_player)
        # print("111111111111111111111111",PLAYER_LIST)


        seacond_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(seacond_player)
        # print("%%%%%%%%%%%%%%%%%%%%%",seacond_player)
        # print("2222222222222222222222",PLAYER_LIST)

        t_winner=game(first_player,seacond_player)
        print("(((((((((((((((((((((((((((((99999999999999999999999999999999999999999",t_winner)
        qsets=Referee.objects.all()
        serialized=RefereeSerializer(qsets,many=True)
        return Response(serialized.data)