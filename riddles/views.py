import random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import Riddle, Category, Score


def home(request):
    return render(request, 'riddles/home.html')

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'riddles/category_list.html', {'categories': categories})

@login_required
def play_riddle(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    riddles = Riddle.objects.filter(category=category)
    played_riddles = request.session.get(f'played_riddles_{category_id}', [])
    current_riddle_id = request.session.get(f'current_riddle_{category_id}')

    if current_riddle_id:
        riddle = get_object_or_404(Riddle, id=current_riddle_id)
    else:
        available_riddles = riddles.exclude(id__in=played_riddles)
        if available_riddles.exists():
            riddle = random.choice(available_riddles)
            played_riddles.append(riddle.id)
            request.session[f'played_riddles_{category_id}'] = played_riddles
            request.session[f'current_riddle_{category_id}'] = riddle.id
            request.session[f'start_time_{riddle.id}'] = timezone.now().isoformat()
            request.session[f'hint_{riddle.id}'] = None
        else:
            riddle = None

    user_scores = Score.objects.filter(user=request.user).order_by('-date_played')
    hint = request.session.get(f'hint_{riddle.id}', None) if riddle else None
    return render(request, 'riddles/play_riddle.html', {
        'riddle': riddle,
        'category': category,
        'user_scores': user_scores,
        'hint': hint
    })

@login_required
def request_hint(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    request.session[f'hint_{riddle_id}'] = riddle.hint
    messages.info(request, f'Indice : {riddle.hint}')
    return redirect('play_riddle', category_id=riddle.category.id)

def scoreboard(request):
    scores = Score.objects.order_by('-date_played')
    return render(request, 'riddles/scoreboard.html', {'scores': scores})


@login_required
def validate_answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    user_answer = request.POST.get('answer')
    start_time_str = request.session.get(f'start_time_{riddle_id}')
    if start_time_str:
        start_time = timezone.datetime.fromisoformat(start_time_str)
        time_taken = (timezone.now() - start_time).total_seconds()
    else:
        time_taken = 0

    if user_answer.lower() == riddle.answer.lower():
        Score.objects.create(user=request.user, riddle=riddle, time_taken=time_taken)
        if time_taken < 10:
            messages.success(request, f'Excellent ! Temps : {time_taken:.2f} secondes')
        else:
            messages.success(request, f'Bonne réponse ! Temps : {time_taken:.2f} secondes')

        # Marquer la devinette comme jouée et passer à la suivante
        category_id = riddle.category.id
        played_riddles = request.session.get(f'played_riddles_{category_id}', [])
        played_riddles.append(riddle.id)
        request.session[f'played_riddles_{category_id}'] = played_riddles
        request.session[f'current_riddle_{category_id}'] = None
    else:
        messages.error(request, 'Mauvaise réponse. Essayez encore !')
        request.session[f'start_time_{riddle_id}'] = timezone.now().isoformat()

    return redirect('play_riddle', category_id=riddle.category.id)

@login_required
def reset_played_riddles(request, category_id):
    if f'played_riddles_{category_id}' in request.session:
        del request.session[f'played_riddles_{category_id}']
    return redirect('play_riddle', category_id=category_id)

@login_required
def skip_riddle(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    riddles = Riddle.objects.filter(category=category)
    played_riddles = request.session.get(f'played_riddles_{category_id}', [])
    available_riddles = riddles.exclude(id__in=played_riddles)

    if available_riddles.exists():
        riddle = random.choice(available_riddles)
        played_riddles.append(riddle.id)
        request.session[f'played_riddles_{category_id}'] = played_riddles
        request.session[f'current_riddle_{category_id}'] = riddle.id
        request.session[f'start_time_{riddle.id}'] = timezone.now().isoformat()
        request.session[f'hint_{riddle.id}'] = None
    else:
        riddle = None

    return redirect('play_riddle', category_id=category_id)
