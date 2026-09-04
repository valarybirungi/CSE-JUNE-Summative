from django import forms
from django.core.exceptions import ValidationError

from .models import Beneficiary


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = [
            "first_name", "last_name", "date_of_birth", "place_of_birth", "gender",
            "nationality", "marital_status", "settlement_camp", "registration_date",
            "date_of_joining",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "registration_date": forms.DateInput(attrs={"type": "date"}),
            "date_of_joining": forms.DateInput(attrs={"type": "date"}),
            "gender": forms.RadioSelect(choices=[("Male", "Male"), ("Female", "Female")]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["gender"].initial = "Female"
        self.fields["first_name"].label = "First name"
        self.fields["last_name"].label = "Last name"
        self.fields["place_of_birth"].label = "Place of birth"
        self.fields["date_of_joining"].label = "Date of joining settlement camp"
        self.fields["registration_date"].label = "Date of registration"
        self.fields["first_name"].widget.attrs.update({"placeholder": "Enter first name"})
        self.fields["last_name"].widget.attrs.update({"placeholder": "Enter last name"})
        self.fields["place_of_birth"].widget.attrs.update({"placeholder": "Enter place of birth"})

    def clean(self):
        cleaned_data = super().clean()
        birth = cleaned_data.get("date_of_birth")
        registration = cleaned_data.get("registration_date")
        joining = cleaned_data.get("date_of_joining")
        if birth and registration and birth >= registration:
            self.add_error("date_of_birth", "Date of birth must be before registration.")
        if joining and registration and joining <= registration:
            self.add_error("date_of_joining", "Joining date must be after registration.")
        return cleaned_data

    def clean_first_name(self):
        value = self.cleaned_data["first_name"].strip()
        if len(value) < 2:
            raise ValidationError("Please enter at least 2 characters.")
        return value

    clean_last_name = clean_first_name

    def clean_place_of_birth(self):
        value = self.cleaned_data["place_of_birth"].strip()
        if len(value) < 2:
            raise ValidationError("Please enter at least 2 characters.")
        return value
