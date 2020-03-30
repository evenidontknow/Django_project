from django.http import HttpResponse
from .models import Notes
from .models import Items
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def home(request):
    if request.method == 'GET':    
        notes = Notes.objects.all()
        items = Items.objects.all()
        return render(request,
            'notes.html',
            {'Notes':notes,'Items':items})
    elif request.method == 'POST': 
        item_name=request.POST['item_name']
        note_id=int(request.POST['note_id'])
        notes = Notes.objects.all()
        for note in notes:
            if note.id == note_id:
                Items.objects.create(
                    item_name=item_name,
                    note_id=note)
        items = Items.objects.all()
        return render(request,
            'notes.html',
            {'Notes':notes,'Items':items})   
        

