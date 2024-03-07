from django.contrib import admin
from .models import PasswordChoice, PasswordGuess, ShoulferSurferGuess
from django.http import HttpResponse
import csv


class PasswordChoiceAdmin(admin.ModelAdmin):
    list_display = ['password', 'identifier']  # Adjust fields as per your model
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="your_model_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['password','identifier'])  # Adjust headers as per your model

        for obj in queryset:
            writer.writerow([getattr(obj, 'password'), getattr(obj, 'identifier')])  # Adjust fields as per your model

        return response

    export_to_csv.short_description = "Export selected objects to CSV"

admin.site.register(PasswordChoice, PasswordChoiceAdmin)

class PasswordGuessAdmin(admin.ModelAdmin):
    list_display = ['password_guess', 'identifier']  # Adjust fields as per your model
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="your_model_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['password_guess','identifier'])  # Adjust headers as per your model

        for obj in queryset:
            writer.writerow([getattr(obj, 'password_guess'), getattr(obj, 'identifier')])  # Adjust fields as per your model

        return response

    export_to_csv.short_description = "Export selected objects to CSV"

admin.site.register(PasswordGuess, PasswordGuessAdmin)

class ShoulferSurferGuessAdmin(admin.ModelAdmin):
    list_display = ['identifier','password_guess','question_number']  # Adjust fields as per your model
    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="your_model_data.csv"'

        writer = csv.writer(response)
        writer.writerow(['identifier','password_guess','question_number'])  # Adjust headers as per your model

        for obj in queryset:
            writer.writerow([getattr(obj, 'identifier'), getattr(obj, 'password_guess'), getattr(obj,'question_number')])  # Adjust fields as per your model

        return response

    export_to_csv.short_description = "Export selected objects to CSV"

admin.site.register(ShoulferSurferGuess, ShoulferSurferGuessAdmin)