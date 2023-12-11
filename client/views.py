from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .form import AddClientForm
from django.contrib import messages
from .models import Activity
from team.models import Team
def home(request):
    # Retrieve recent activities (you might have a more specific query)
    recent_activities = Activity.objects.order_by('-timestamp')[:5]  # Fetch 5 most recent activities

    return render(request, 'core/index.html', {'recent_activities': recent_activities})
# from teams.models import Team
@login_required
def client_list(request):
    clients=Client.objects.filter(created_by=request.user)
    return render(request,"client/client_list.html",{'clients':clients})
@login_required
def client_details(request,pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    return render(request,"client/client_details.html",{'client':client})
@login_required
def add_clients(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
                team=Team.objects.filter(created_by=request.user)[0]
                client = form.save(commit=False)  # Save the form data to a new client object without committing to the database yet
                client.created_by = request.user  # Assign the current user as the creator of this client (if necessary)
                client.team=team
                client.save()  # Save the new client to the database
                messages.success(request, "Client has been added")
                return redirect('/client/client-list/')
    else:
        form = AddClientForm()
    return render(request, 'client/add_client.html', {'form': form})
@login_required  
def clients_delete(request,pk):
    clients=Client.objects.filter(created_by=request.user).get(pk=pk)
    messages.success(request, "Client has been deleted")
    clients.delete()
    return redirect('/client/client-list')
@login_required
def clients_edit(request,pk):
    client=get_object_or_404(Client,created_by=request.user,pk=pk)
    if request.method=='POST':
        form = AddClientForm(request.POST,instance=client)
        if form.is_valid():  
            form.save()
            messages.success(request, "the changes was saved ")
            return redirect('/client/client-list')
    else:
        form = AddClientForm(instance=client)
    return render(request,'client/add_client.html',{'form':form})
