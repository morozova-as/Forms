from __future__ import unicode_literals

from django.db import models


class AnimalShelters(models.Model):
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    shelter_id = models.IntegerField(db_column='Shelter_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'animal_shelters'

    def __str__(self):
        return self.name


class AnimalSheltersHasPositions(models.Model):
    animal_shelters_shelter = models.ForeignKey(AnimalShelters, models.DO_NOTHING, db_column='Animal shelters_Shelter_id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    positions_name = models.ForeignKey('Positions', models.DO_NOTHING, db_column='Positions_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'animal_shelters_has_positions'
        unique_together = (('animal_shelters_shelter', 'positions_name'),)

    def __str__(self):
        return self.positions_name


class Animals(models.Model):
    breed = models.ForeignKey('Types', models.DO_NOTHING, db_column='Breed')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    animal_id = models.IntegerField(db_column='Animal_id', primary_key=True)  # Field name made lowercase.
    shelter = models.ForeignKey(AnimalShelters, models.DO_NOTHING, db_column='Shelter_id')  # Field name made lowercase.
    animal_employee = models.ForeignKey('Employees', models.DO_NOTHING, db_column='Animal_employee')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'animals'

    def __str__(self):
        return self.name

class AnimalsHasGrafts(models.Model):
    animals_animal = models.ForeignKey(Animals, models.DO_NOTHING, db_column='Animals_Animal_id', primary_key=True)  # Field name made lowercase.
    grafts = models.ForeignKey('Grafts', models.DO_NOTHING, db_column='Grafts_id')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'animals_has_grafts'
        unique_together = (('animals_animal', 'grafts'),)

    def __str__(self):
        return self.animals_animal

class Employees(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    employee_id = models.IntegerField(db_column='Employee_id', primary_key=True)  # Field name made lowercase.
    employee_position = models.ForeignKey('Positions', models.DO_NOTHING, db_column='Employee_position')  # Field name made lowercase.
    employee_shelter = models.ForeignKey(AnimalShelters, models.DO_NOTHING, db_column='Employee_shelter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'

    def __str__(self):
        return self.name

class Grafts(models.Model):
    graft_id = models.IntegerField(db_column='Graft_id', primary_key=True)  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=45)  # Field name made lowercase.
    periodicity = models.IntegerField(db_column='Periodicity')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grafts'

    def __str__(self):
        return self.disease

class Positions(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=50)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'positions'

    def __str__(self):
        return self.name

class Types(models.Model):
    breed = models.CharField(db_column='Breed', primary_key=True, max_length=45)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'types'

    def __str__(self):
        return self.breed