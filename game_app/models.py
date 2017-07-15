from django.db import models


role_choices=  (
                            ('attacker', 'ATTACKER'),
                            ('defencer', 'DEFENCER'),
                        )

class Referee(models.Model):
    player_won=models.CharField(max_length=50)



class PersonMixin(models.Model):
    score=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)

class CurrentPlayerList(models.Model):
    current_list=models.TextField(null=True, blank=True)

class Person1(PersonMixin,models.Model):
    name="person1"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=8

    def __str__(self):
        return self.name


class Person2(PersonMixin,models.Model):
    name="person2"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=8



class Person3(PersonMixin,models.Model):
    name="person3"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=7



class Person4(PersonMixin,models.Model):
    name="person4"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=7



class Person5(PersonMixin,models.Model):
    name="person5"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=6



class Person6(PersonMixin,models.Model):
    name="person6"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=6


class Person7(PersonMixin,models.Model):
    name="person7"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=5



class Person8(PersonMixin,models.Model):
    name="person8"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length = 5








#
# class Players(models.Model):
#     uid = models.ForeignKey('auth.User', related_name='player')
#     name = models.CharField(max_length=50)
#     defence_len = models.IntegerField()
#     joined = models.IntegerField(default=0)
#     tour_status = models.IntegerField(default=0)
#     round1_gameid = models.IntegerField(null=True)
#     round1_qualified = models.IntegerField(null=True)
#     round2_gameid = models.IntegerField(null=True)
#     round2_qualified = models.IntegerField(null=True)
#     round3_gameid = models.IntegerField(null=True)
#     round3_winner = models.IntegerField(null=True)


# class Game(models.Model):
#     player1_id = models.IntegerField(null=True)
#     player2_id = models.IntegerField(null=True)
#     player1_responses = models.CharField(max_length=200)
#     player2_responses = models.CharField(max_length=200)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField(null=True)
#     player1_score = models.IntegerField(default=0)
#     player2_score = models.IntegerField(default=0)
#     order = models.IntegerField()
#     round_no = models.IntegerField()
#
#
# class Variables(models.Model):
#     count = models.IntegerField(default=1)
#     x = models.CharField(max_length=50, default="[1,2,3,4,5,6,7,8]")
