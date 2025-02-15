from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from .models import Job
import re
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    search_fields = ['positionName', 'company', 'location']
    list_display = ('position_name', 'company', 'location', 'salary_in_dollar')
    change_list_template = "admin/job_changelist.html"  # Use a custom template

    def position_name(self, obj):
        return obj.positionName if obj.positionName else "No Title"

    def salary_in_dollar(self, obj):
        return self.convert_salary(obj.salary) if obj.salary else 0

    def convert_salary(self, salary_string):
        if not salary_string:
            return 0
        salary_string = salary_string.strip().lower()

        match_annual = re.match(r"\$?\s*([\d\s,]+)\s*-\s*\$?\$?\s*([\d\s,]+)\s*(?:annually|per annum)?", salary_string)
        if match_annual:
            try:
                min_salary = float(match_annual.group(1).replace(",", "").replace(" ", ""))
                max_salary = float(match_annual.group(2).replace(",", "").replace(" ", ""))
                return (min_salary + max_salary) / 2
            except ValueError:
                return 0

        match_hourly = re.match(r"\$?\s*([\d\s,]+)\s*-\s*\$?\$?\s*([\d\s,]+)\s*(?:per hour|an hour)?", salary_string)
        if match_hourly:
            try:
                min_salary = float(match_hourly.group(1).replace(",", "").replace(" ", ""))
                max_salary = float(match_hourly.group(2).replace(",", "").replace(" ", ""))
                return ((min_salary + max_salary) / 2) * 40 * 52
            except ValueError:
                return 0

        return 0

    def calculate_average_salary(self, request):
        location = request.GET.get("location")

        if not location:
            return JsonResponse({"error": "Location is required"}, status=400)

        jobs = Job.objects.filter(location__icontains=location)

        if not jobs.exists():
            return JsonResponse({"error": f"No jobs found for location: {location}"}, status=404)

        total_salary = sum(self.convert_salary(job.salary) for job in jobs)
        average_salary = total_salary / jobs.count() if jobs.count() > 0 else 0

        return JsonResponse({"average_salary": round(average_salary, 2)})


    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path('calculate_average/', self.admin_site.admin_view(self.calculate_average_salary, cacheable=True), name='calculate_average'),
    ]
        return custom_urls + urls  # Ensure custom URLs are added first
