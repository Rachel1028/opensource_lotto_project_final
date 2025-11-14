from django.db import models

class LottoTicket(models.Model):
    name = models.CharField(max_length=30)
    numbers = models.CharField(max_length=100)   # "1, 5, 10, 23, 30, 41"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} : {self.numbers}"


class LottoDraw(models.Model):
    winning_numbers = models.CharField(max_length=100)  # "3, 11, 23, 27, 33, 40"
    draw_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Draw on {self.draw_date} : {self.winning_numbers}"
