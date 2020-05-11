from django.contrib import admin
from .forms import RecruitmentForm
from .models import Recruiter


def make_akceptacja(modeladmin, request, queryset):
    queryset.update(status='a')
    make_akceptacja.short_description = "zaznacz, by zaakceptowac"


def make_niezaakceptowany(modeladmin, request, queryset):
    queryset.update(status='n')
    make_niezaakceptowany.short_description = "zaznacz, by niezaakceptowac"


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "timestamp", "updated", "status"]
    form = RecruitmentForm
    actions = [make_akceptacja, make_niezaakceptowany]


admin.site.register(Recruiter, RecruitmentAdmin)
