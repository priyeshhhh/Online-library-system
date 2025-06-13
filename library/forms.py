from django import forms
from .models import Author, Book, BorrowRecord

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only Gmail addresses allowed.")
        return email

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = '__all__'
