from django.contrib import admin

from vencimientos.models import (
    Agency, CompaniesDueDate, Company, Criteria, DueDate,
    DueDateRule, Tax
)


admin.site.register(Agency)
admin.site.register(Company)
admin.site.register(Criteria)
admin.site.register(Tax)


@admin.register(DueDate)
class DueDateAdmin(admin.ModelAdmin):
    list_display = ("tax", "criteria", "period", "value", "due_date")
    list_filter = ("tax", )
    list_per_page = 30


@admin.register(DueDateRule)
class DueDateRuleAdmin(admin.ModelAdmin):
    list_display = ("tax", "criteria", "value", "day")
    list_filter = ("tax", )
    list_per_page = 30


@admin.register(CompaniesDueDate)
class CompaniesDueDateAdmin(admin.ModelAdmin):
    list_display = ("tax", "company", "period", "due_date")
    list_filter = ("tax", "company")
    list_per_page = 30
