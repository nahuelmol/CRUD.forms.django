from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from .models import Contact,Countries
from .forms import ContactForm,CountriesForm
=======
from .models import Contact
from .forms import ContactForm,Creater_User
>>>>>>> c3219e750c5c06f187097b7f923f5db793807721
from django.views.generic import ListView, DetailView

#########################################################################################
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        return Contact.objects.all()

class CountriesView(ListView):
    template_name = 'index_countries.html'
    context_object_name = 'countries_list'

    def get_queryset(self):
        return Countries.objects.all()

class CountryDetail(DetailView):
    model = Countries
    template_name = 'detail_country.html'
    context_object_name = 'country'

    def get_object(self,**kwargs):
        result = Countries.objects.get(id=self.kwargs['pk'])
        print(result.Name)
        return result

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'
    context_object_name = 'result'

    def __init__(self):
        self._template_name = 'contact-detail.html'

    def get_object(self,**kwargs):
        result = Contact.objects.get(id=self.kwargs['pk'])
        contact = get_object_or_404(Contact, pk=self.kwargs['pk'])

        print(result)
        print(contact.firstName)
        print(result.lastName)
        return result
#########################################################################################

def register_page(req):
   
    if req.method == 'POST':
        form = Creater_User(req.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
    form = Creater_User()
    context = {'form':form}

    return render(req,'register.html',context)

def create(req):
	
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/contacts/')
    form = ContactForm()

    context = {'form': form}

    return render(req,'create.html',context)

def edit(req, pk, template_name='edit.html'):
    
    ## pk/id specified to save, where we can refer at this contact from 
    contact = get_object_or_404(Contact, pk=pk) 
    
    form = ContactForm(req.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        model = form.instance
        return redirect('index')

    context = {'form':form}

    return render(req, template_name,context)

def delete(request, pk, template_name='confirm_delete.html'):

    contact = get_object_or_404(Contact, pk=pk)

    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})
<<<<<<< HEAD

def entering_countries(req):
    if req.method == 'POST':
        form = CountriesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/countries/')
    form = CountriesForm()

    context = {'form':form}
    return render(req,'create_countries.html',context)

=======
>>>>>>> c3219e750c5c06f187097b7f923f5db793807721
