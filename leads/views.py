from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from client.models import Client
# from teams.models import Team
from .models import *
# Create your views here.
@login_required
def leads_list(request):
    leads=Lead.objects.filter(created_by=request.user,converted_to_client=False)
    return render(request,"lead/lead_list.html",{'leads':leads})
@login_required
def leads_details(request,pk):
    leads=Lead.objects.filter(created_by=request.user).get(pk=pk)
    return render(request,"lead/lead_details.html",{'leads':leads})
def leads_delete(request,pk):
    leads=Lead.objects.filter(created_by=request.user).get(pk=pk)
    messages.success(request, "Lead has been deleted")
    leads.delete()
    return redirect('lead-list')
@login_required
def add_leads(request):
    if request.method=='POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead=form.save(commit=False)
            lead.created_by=request.user
            lead.save()
            messages.success(request, "Lead has been Added")
            return redirect('lead-list')
    else:
        form = AddLeadForm()
    return render(request,'lead/add_lead.html',{'form':form})
@login_required
def leads_edit(request,pk):
    lead=get_object_or_404(Lead,created_by=request.user,pk=pk)
    if request.method=='POST':
        form = AddLeadForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "the changes was saved ")
            return redirect('lead-list')
    else:
        form = AddLeadForm(instance=lead)
    return render(request,'lead/add_lead.html',{'form':form})

@login_required
def Convert_to_client(request,pk):
     lead=get_object_or_404(Lead,created_by=request.user,pk=pk)
    #  team=Team.objects.filter(created_by=request.user).first()

     client=Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=lead.created_by,
        # team=team
     )
     lead.converted_to_client=True
     lead.save()
     messages.success(request,"the lead was converted to a client")
     return redirect('lead-list')