from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields = ('profilePicture', 'firstName', 'lastName', 'barangay', 'city', 'Zip', 
                  'province', 'country', 'birthdate', 'height', 'weight', 'religion', 'status', 'gender', 'motherName', 'motherOccupation', 'fatherName', 'fatherOccupation', 'email', 'password')
        
class MedicineForm(forms.ModelForm):
	
	class Meta:
		model = Medicine
		fields = ('category', 'genericName', 'commonBrand', 'manufacturedDate', 'expiryDate', 'size', 
				  'howTo_Use', 'sideEffects', 'price', 'noItems', 'img1')