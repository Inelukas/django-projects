from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Eat no meat for the entire month!",
    "april": "Eat no meat for the entire month!",
    "may": "Eat no meat for the entire month!",
    "june": "Eat no meat for the entire month!",
    "july": "Eat no meat for the entire month!",
    "august": "Eat no meat for the entire month!",
    "september": "Eat no meat for the entire month!",
    "october": "Eat no meat for the entire month!",
    "november": "Eat no meat for the entire month!",
    "december": "Eat no meat for the entire month!",
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    return HttpResponse(f"<ul>{list_items}</ul>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month=months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")