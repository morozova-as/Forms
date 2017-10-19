from django.contrib import admin
from .models import *

class AnimalSheltersAdmin(admin.ModelAdmin):
    list_display = ('name', 'shelter_id')

class AnimalSheltersHasPositionsAdmin(admin.ModelAdmin):
    list_display = ('animal_shelters_shelter', 'positions_name')

class AnimalsAdmin(admin.ModelAdmin):
    list_display = ('breed','name','age','animal_id','shelter','animal_employee')

class AnimalsHasGraftsAdmin(admin.ModelAdmin):
    list_display = ('animals_animal','grafts','date')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name','employee_id','employee_position','employee_shelter')

class GraftsAdmin(admin.ModelAdmin):
    list_display = ('graft_id','disease','periodicity','type')

class PositionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary')

class TypesAdmin(admin.ModelAdmin):
    list_display = ('breed', 'type')


admin.site.register(AnimalShelters, AnimalSheltersAdmin)
admin.site.register(AnimalSheltersHasPositions, AnimalSheltersHasPositionsAdmin)
admin.site.register(Animals, AnimalsAdmin)
admin.site.register(AnimalsHasGrafts, AnimalsHasGraftsAdmin)
admin.site.register(Employees,EmployeesAdmin)
admin.site.register(Grafts, GraftsAdmin)
admin.site.register(Positions, PositionsAdmin)
admin.site.register(Types, TypesAdmin)
