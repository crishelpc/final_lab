from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Category, Product, Customer, MealType

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border '


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('first_name', 'last_name', 'phone', 'email', 'password',)
		labels = {
			'first_name': '',
			'last_name': '',
			'phone': '',
			'email': '',
			'password': '',
		}
		widgets = {
			'first_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last_Name'}),
			'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone_Number'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeolder': 'Email'}),
			'password': forms.HiddenInput(),
		}	


class MealTypeForm(ModelForm):
	class Meta: 
		fields = ('name',)
		labels = {
			'name',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meal Type'}),
		}




class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'price', 'category', 'description', 'image', 'meal_type', 'is_sale', 'sale_price',)
		labels = {
			'name': '',
			'price': 'Product Price',
			'category': '',
			'description': '',
			'image': '',
			'meal_type': '',
			'is_sale': '',
			'sale_price': 'Sale Price',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
			'price': forms.NumberInput(attrs={'class': 'form-control'}),
			'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product Category'}),
			'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
			'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'meal_type': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Product Meal Type'}),
			'is_sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'sale_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sale Price'}),
		} 
	is_sale = forms.BooleanField(
    	required=False,  
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Product Is on Sale',
        initial=False,  
    )

class CategoryForm(ModelForm):
	class Meta:
		model = Category 
		fields = ('name',)
		labels = {
		'name': '',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category_Name'}),
		}

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'