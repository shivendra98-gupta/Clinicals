from django.shortcuts import render,redirect
from .models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 
from .forms import ClinicalDataForm

class PatientListView(ListView):                                                                                     #ListView jisse data dikha sakeh
    model=Patient

class PatientCreateView(CreateView):                                                                                             #CreateView jisse data daal sakeh
    # class Meta:
            #model=Patient
            #success_url=reverse_lazy('index') 
            #fields="__all__"
    model=Patient
    success_url=reverse_lazy('index')                                                                                                        #esse index page pe pahuch jaaye ge after creating patient on google
    fields=("firstname","lastname","age")                                                                                                #kya kya fields likhe hue dikhe geh vo yaha likhe hai
class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')                                                                                              #esse index page pe pahuch jaaye ge after deleting patient on google

class PatientUpdateView(UpdateView):
        model=Patient
        success_url=reverse_lazy('index') 
        fields=("firstname","lastname","age")


def addData(request,**kwargs):                                                                                                                   # kwargs means keyword argument
     form=ClinicalDataForm()
     patient=Patient.objects.get(id=kwargs['pk'])
     if request.method=='POST':
          form=ClinicalDataForm(request.POST)
          if form.is_valid():
               form.save()
          return redirect("/")
     return render(request,'ClinicalApp/data_form.html',{'form':form,'patient':patient})

#21-08-23
def analyse(request,**kwargs):
      data=ClinicalData.objects.filter(patient_id=kwargs['pk'])
      responseData=[]
      for eachEntry in data:
           if eachEntry.componentname=="hw":
                heightAndWeight=eachEntry.componentvalue.split("/")
                if len(heightAndWeight)>1:
                     feetToMetres=float(heightAndWeight[0])*0.4356
                     BMI=(float(heightAndWeight[1]))/(feetToMetres*feetToMetres)
                     bmiEntry=ClinicalData()
                     bmiEntry.componentname="BMI"
                     bmiEntry.componentvalue=BMI
                     responseData.append(bmiEntry)
                responseData.append(eachEntry)
           return render(request,'ClinicalApp/generateReport.html',{'data':data})# yeh 'data' generateReport.html meh jaaye ga





        
