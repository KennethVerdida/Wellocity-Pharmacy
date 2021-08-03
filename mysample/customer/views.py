from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *

class LandingIndexView(View):
  def get(self, request):
    return render(request, 'customer/landing.html')
  
  def post(self, request):
    if request.method == 'POST':
      if 'btnSignin' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        if user is not None:
          login(request, user)
          return redirect('customer:dashboard_view')         
      else:
        return HttpResponse('not valid')
  
class CustomerRegistrationView(View):
  def get(self, request):
    return render(request, 'customer/customerRegistration.html')

  def post(self, request):
    form = CustomerForm(request.POST, request.FILES)
    
    if form.is_valid():
      profilePicture = request.FILES['profilePicture']
      fname = request.POST.get("firstName")
      mname = request.POST.get("middleName")
      lname = request.POST.get("lastName")
      street = request.POST.get("street")
      brgy = request.POST.get("barangay")
      city = request.POST.get("city")
      Zip = request.POST.get("Zip")
      prov = request.POST.get("province")
      country = request.POST.get("country")
      bday = request.POST.get("birthdate")
      height = request.POST.get("height")
      weight = request.POST.get("weight")
      religion = request.POST.get("religion")
      gender = request.POST.get("gender")
      status = request.POST.get("status")
      spouseName = request.POST.get("spouseName")
      spouseOccupation = request.POST.get("spouseOccupation")
      noChildren = request.POST.get("noChildren")
      motherName = request.POST.get("motherName")
      motherOccupation = request.POST.get("motherOccupation")
      fatherName = request.POST.get("fatherName")
      fatherOccupation = request.POST.get("fatherOccupation")
      email = request.POST.get("email")
      password = request.POST.get("password")
      
      form = Customer(profilePicture = profilePicture, dateRegistered_Customer  = timezone.now(), 
            firstName = fname, middleName = mname, lastName = lname, street = street, barangay = brgy,
            city = city, Zip = Zip, province = prov, country = country, birthdate = bday, height = height, weight = weight, religion = religion, gender = gender, status = status, 
            spouseName = spouseName, spouseOccupation = spouseOccupation, noChildren = noChildren,
            motherName = motherName, motherOccupation = motherOccupation,fatherName = fatherName,
            fatherOccupation = fatherOccupation, email = email, password = password)
      
      form.save()
      messages.success(request, 'CUSTOMER SAVED SUCCESSFULLY')
      return redirect('customer:dashboard_view')
    
class DashboardIndexView(View):
    def get(self, request):
      customers = Customer.objects.all()
      medicines = Medicine.objects.all()
      context = {
        'customers' : customers,
        'medicines' : medicines
      }
      return render(request, 'customer/dashboard.html', context)

    def post(self, request):
      if request.method == 'POST':
        if 'btnUpdate1' in request.POST:
          print('update profile button clicked')
          cid = request.POST.get("customer-id")
          fname = request.POST.get("customer-firstName")
          mname = request.POST.get("customer-middleName")
          lname = request.POST.get("customer-lastName")
          street = request.POST.get("customer-street")
          brgy = request.POST.get("customer-barangay")
          city = request.POST.get("customer-city")
          Zip = request.POST.get("customer-Zip")
          prov = request.POST.get("customer-province")
          country = request.POST.get("customer-country")
          bday = request.POST.get("customer-birthdate")
          height = request.POST.get("customer-height")
          weight = request.POST.get("customer-weight")
          religion = request.POST.get("customer-religion")
          gender = request.POST.get("customer-gender")
          status = request.POST.get("customer-status")
          spouseName = request.POST.get("customer-spouseName")
          spouseOccupation = request.POST.get("customer-spouseOccupation")
          noChildren = request.POST.get("customer-noChildren")
          motherName = request.POST.get("customer-motherName")
          motherOccupation = request.POST.get("customer-motherOccupation")
          fatherName = request.POST.get("customer-fatherName")
          fatherOccupation = request.POST.get("customer-fatherOccupation")
          email = request.POST.get("customer-email")
          password = request.POST.get("customer-password")
          update_customer = Customer.objects.filter(person_ptr_id = cid).update(firstName = fname, 
                            middleName = mname, lastName = lname, street = street, barangay = brgy,
                            city = city, Zip = Zip, province = prov, country = country, birthdate =
                            bday, height = height, weight = weight, religion = religion, gender = 
                            gender, status = status, spouseName = spouseName, spouseOccupation =
                            spouseOccupation, noChildren = noChildren, motherName = motherName, 
                            motherOccupation = motherOccupation,fatherName = fatherName, 
                            fatherOccupation = fatherOccupation, email = email, password = password)
          print('profile updated')

        elif 'btnDelete1' in request.POST:	
          print('delete button clicked')
          cid = request.POST.get("ccustomer-id")
          customer = Customer.objects.filter(person_ptr_id=cid).delete()
          person = Person.objects.filter(id = cid).delete()
          print('recorded deleted')

        elif 'btnUpdate' in request.POST:
          print('update profile button clicked')
          mid = request.POST.get("medicine-id")
          Category = request.POST.get("medicine-category")
          gName = request.POST.get("medicine-genericName")
          cBrand = request.POST.get("medicine-commonBrand")
          mDate = request.POST.get("medicine-manufacturedDate")
          eDate = request.POST.get("medicine-expiryDate")
          Size = request.POST.get("medicine-size")
          Order = request.POST.get("medicine-order")
          Total = request.POST.get("medicine-totalPrice")
          hTo_Use = request.POST.get("medicine-howTo_Use")
          sEffects = request.POST.get("medicine-sideEffects")
          Price = request.POST.get("medicine-price")
          nItems = request.POST.get("medicine-noItems")

          update_medicine = Medicine.objects.filter(id = mid).update(dateRegistered_Medicine = 
                            timezone.now(), category = Category, genericName = gName, commonBrand = cBrand, manufacturedDate = mDate, expiryDate = eDate, size = Size, order = Order, total = Total, howTo_Use = hTo_Use, sideEffects = sEffects,price = Price, noItems = nItems) 
          print(update_medicine)
          print('Medicine Updated')

        elif 'btnDelete' in request.POST:
          print('delete button clicked')
          mid = request.POST.get("mmedicine-id")
          medic = Medicine.objects.filter(id= mid).delete()
          print('recorded deleted')
        
        elif 'btnPurchase' in request.POST:
          mid = request.POST.get("medicine-id")  
          nItems = request.POST.get("medicine-noItems")
          Order = request.POST.get("medicine-ordering_Items")
          total_Purchase = request.POST.get("medicine-total_Items")
            
          items_Left = (int(nItems)-int(Order))
          Total = (float(Order) * float(total_Purchase)) 
             
          update_m = Medicine.objects.filter(id = mid).update(noItems = items_Left, order = Order, total = Total) 
          print(update_m)
          print('Medicine Updated')
    
        return redirect('customer:dashboard_view')

class MedicineRegistrationView(View):
    def get(self, request):
        return render(request, 'customer/medicineRegistration.html')

    def post(self, request):        
        form = MedicineForm(request.POST, request.FILES)    

        if form.is_valid():     
            Category = request.POST.get("category")
            gName = request.POST.get("genericName")
            cBrand = request.POST.get("commonBrand")
            mDate = request.POST.get("manufacturedDate")
            eDate = request.POST.get("expiryDate")
            Size = request.POST.get("size")
            Order = request.POST.get("order")
            Total = request.POST.get("total")
            hTo_Use = request.POST.get("howTo_Use")
            sEffects = request.POST.get("sideEffects")
            Price = request.POST.get("price")
            nItems = request.POST.get("noItems")
            image1 = request.FILES.get('img1')
            image2 = request.FILES.get('img2')
            image3 = request.FILES.get('img3')
            
            form = Medicine(dateRegistered_Medicine = timezone.now(), category = Category, 
                  genericName = gName, commonBrand = cBrand, manufacturedDate = mDate, expiryDate =
                  eDate, size = Size, order = Order, total = Total, howTo_Use = hTo_Use, sideEffects = sEffects, price = Price, noItems = nItems,  img1 = image1, img2 = image2, img3 = image3)
            form.save()

            return redirect('customer:dashboard_view')    
          
        else:
            print(form.errors)
            return HttpResponse('not valid')
      