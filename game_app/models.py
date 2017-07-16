from django.db import models


role_choices=  (
                            ('attacker', 'ATTACKER'),
                            ('defencer', 'DEFENCER'),
                        )

class Referee(models.Model):
    player_won=models.CharField(max_length=50)



# class PersonMixin(models.Model):
#     point=models.IntegerField(default=0)
#     role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
#     defense_array=models.TextField(null=True, blank=True)
#     attack_array=models.TextField(null=True, blank=True)

class CurrentPlayerList(models.Model):
    current_list=models.TextField(null=True, blank=True)

class Person1(models.Model):
    name="person1"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=8
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class Person2(models.Model):
    name="person2"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=8
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)




class Person3(models.Model):
    name="person3"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=7
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)




class Person4(models.Model):
    name="person4"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=7
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)




class Person5(models.Model):
    name="person5"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=6
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)




class Person6(models.Model):
    name="person6"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=6
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)



class Person7(models.Model):
    name="person7"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length=5
    point=models.IntegerField(default=0)
    role=models.CharField(choices=role_choices,max_length=10, null=True, blank=True)
    defense_array=models.TextField(null=True, blank=True)
    attack_array=models.TextField(null=True, blank=True)




class Person8(models.Model):
    name="person8"
    playing=models.BooleanField(default=False)
    game_number=models.IntegerField(default=0)
    array_length = 5
    point = models.IntegerField(default=0)
    role = models.CharField(choices=role_choices, max_length=10, null=True, blank=True)
    defense_array = models.TextField(null=True, blank=True)
    attack_array = models.TextField(null=True, blank=True)

