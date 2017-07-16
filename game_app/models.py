from django.db import models


role_choices=  (
                            ('attacker', 'ATTACKER'),
                            ('defencer', 'DEFENCER'),
                        )

class Referee(models.Model):
    name=models.CharField(max_length=50)
    player_won=models.CharField(max_length=50)



# class PersonMixin(models.Model):
#     point=models.IntegerField(default=0)
#     role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
#     defense_array=models.TextField(null=True, blank=True)
#     attack_array=models.TextField(null=True, blank=True)

class CurrentPlayerList(models.Model):
    current_list=models.TextField(null=True, blank=True)

class Users(models.Model):
    name=models.CharField(max_length=50)
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    game_id=models.IntegerField()
    array_length=models.IntegerField()
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)



    def __str__(self):
        return self.name

