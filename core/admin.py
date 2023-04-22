from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import *


@admin.register(Stages)
class StagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionsAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ReviewText)
class ReviewTextAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(ReviewVideo)
class ReviewVideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
