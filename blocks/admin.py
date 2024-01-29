from django.contrib import admin
from .models import *


@admin.register(HeaderBlock)
class HeaderBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(MainBlock)
class MainBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutBlock)
class AboutBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductionBlock)
class ProductionBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ServicesBlock)
class ServicesBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectsBlock)
class ProjectsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(StagesBlock)
class StagesBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamBlock)
class TeamBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionsBlock)
class QuestionsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ReviewsBlock)
class ReviewsBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactsBlock)
class ContactsBlockAdmin(admin.ModelAdmin):
    pass
