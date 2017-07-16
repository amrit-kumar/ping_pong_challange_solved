from pygments.util import xrange
from rest_framework import viewsets
from rest_framework.decorators import detail_route,list_route
from rest_framework.response import Response

from game_app.serializers import *
from .models import *
import random
from django.apps import apps


MAX_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

PLAYER_LIST = []


SEMIFINAL_LIST=[]
FINAL_LIST=[]


def game(player1,player2):

    count1 = 0
    count2 = 0
    game_count=0
    player1.playing=True
    player2.playing=True
    player1.role='defencer'

    my_randoms=[]
    my_randoms2=[]
    guess=0
    guess2=0
    while (player1.point!=5 or player2.point!=5):
        if player1.role=='defencer':

            my_randoms = random.sample(xrange(1, 11), player1.array_length)
            player1.defense_array=my_randoms
            guess = random.choice(MAX_ARRAY)

        elif player2.role=='defencer':


            my_randoms2 = random.sample(xrange(1, 11), player2.array_length)
            player2.defense_array = my_randoms
            guess2 = random.choice(MAX_ARRAY)

        if guess in my_randoms:
            player2.role='defencer'
            count1+=1
            player1.point=count1

        else:
            player1.role='defencer'
            count2 += 1
            player2.point = count1


        if guess2 in my_randoms2:
            player1.role='defencer'
            count2 += 1
            player2.point = count1

        else:
            player2.role='defencer'
            count1+=1
            player1.point=count1


    if player1.point==5:
        return player1
    elif player2.point==5:
        return player2

class RefereeViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

class AddUserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class FirstRoundViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

    @list_route(methods=["GET"])
    def first_match(self,request):
        users = Users.objects.all()
        for i in users:
            PLAYER_LIST.append(i)
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)
        t_winner=game(first_player,second_player)
        SEMIFINAL_LIST.append(t_winner)

        return Response("First Match")

    @list_route(methods=["GET"])
    def second_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)


        t_winner=game(first_player,second_player)
        SEMIFINAL_LIST.append(t_winner)


        return Response("Second Match")

    @list_route(methods=["GET"])
    def third_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)
        SEMIFINAL_LIST.append(t_winner)
        print("2@@@@@@@@@@@@@@@@@@@@@@",PLAYER_LIST)



        return Response("Third Match")

    @list_route(methods=["GET"])
    def fourth_match(self,request):
        first_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(first_player)

        second_player=random.choice(PLAYER_LIST)
        PLAYER_LIST.remove(second_player)

        t_winner=game(first_player,second_player)
        SEMIFINAL_LIST.append(t_winner)


        return Response("Fourth Match")

class SecondRoundViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class = RefereeSerializer

    @list_route(methods=["GET"])
    def semifinal_match1(self,request):
        first_player=random.choice(SEMIFINAL_LIST)
        SEMIFINAL_LIST.remove(first_player)

        second_player=random.choice(SEMIFINAL_LIST)
        SEMIFINAL_LIST.remove(second_player)

        t_winner=game(first_player,second_player)
        FINAL_LIST.append(t_winner)


        return Response("First Match")

    @list_route(methods=["GET"])
    def semifinal_match2(self,request):
        first_player=random.choice(SEMIFINAL_LIST)
        SEMIFINAL_LIST.remove(first_player)

        second_player=random.choice(SEMIFINAL_LIST)
        SEMIFINAL_LIST.remove(second_player)

        t_winner=game(first_player,second_player)
        FINAL_LIST.append(t_winner)


        return Response("Second Match")

class ThirdRoundViewSet(viewsets.ModelViewSet):
    queryset = Referee.objects.all()
    serializer_class=RefereeSerializer

    @list_route(methods=["GET"])
    def last_match(self,request):
        first_player=random.choice(FINAL_LIST)
        FINAL_LIST.remove(first_player)

        second_player=random.choice(FINAL_LIST)
        FINAL_LIST.remove(second_player)

        t_winner=game(first_player,second_player)
        Referee.objects.create(player_won=t_winner)

        return Response("Last Match")
