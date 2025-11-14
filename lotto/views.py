from django.shortcuts import render, redirect
from .models import LottoTicket, LottoDraw
import random

def home(request):
    tickets = LottoTicket.objects.all().order_by('-created_at')
    return render(request, "home.html", {"tickets": tickets})


def buy_ticket(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mode = request.POST.get("mode")

        if mode == "auto":
            nums = random.sample(range(1, 46), 6)
            nums.sort()
            numbers = ", ".join(map(str, nums))
        else:
            numbers = request.POST.get("numbers")

        LottoTicket.objects.create(name=name, numbers=numbers)
        return redirect("/")

    return render(request, "buy.html")


def result(request):
    last_draw = LottoDraw.objects.order_by('-draw_date').first()
    tickets = LottoTicket.objects.order_by('-created_at')

    if not last_draw:
        return render(request, "result.html", {"error": "관리자가 아직 당첨 번호를 생성하지 않았습니다."})

    win_nums = list(map(int, last_draw.winning_numbers.split(",")))

    results = []
    for t in tickets:
        user_nums = list(map(int, t.numbers.split(",")))
        matched = len(set(win_nums) & set(user_nums))

        # 등수 판정
        if matched == 6:
            rank = "1등"
            color = "red"
        elif matched == 5:
            rank = "2등"
            color = "blue"
        elif matched == 4:
            rank = "3등"
            color = "gray"
        else:
            rank = "꽝"
            color = ""

        results.append({
            "name": t.name,
            "numbers": t.numbers,
            "matched": matched,
            "rank": rank,
            "color": color,
        })

    return render(request, "result.html", {
        "winning": last_draw.winning_numbers,
        "results": results,
    })
