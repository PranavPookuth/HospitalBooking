from django.contrib import admin
from .models import Department,Doctors,Booking
from .views import department

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
     list_display = ('id','p_name','p_phone','p_email','dr_name','booking_date','booked_on')


admin.site.register(Booking,BookingAdmin)