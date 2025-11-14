from django.contrib import admin
from .models import LottoTicket, LottoDraw

@admin.register(LottoTicket)
class LottoTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'numbers', 'created_at')
    ordering = ('-created_at',)

@admin.register(LottoDraw)
class LottoDrawAdmin(admin.ModelAdmin):
    list_display = ('id', 'winning_numbers', 'draw_date')
    ordering = ('-draw_date',)
