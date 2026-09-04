from django import forms
from django.core.exceptions import ValidationError

from .models import Beneficiary


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = [
            "first_name",
            "last_name",
            "date_of_birth",
            "place_of_birth",
            "gender",
            "nationality",
            "marital_status",
            "settlement_camp",
            "registration_date",
            "date_of_joining",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter last name"}),
            "place_of_birth": forms.TextInput(attrs={"placeholder": "Enter place of birth"}),
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

    def clean(self):
        cleaned_data = super().clean()
        birth = cleaned_data.get("date_of_birth")
        registration = cleaned_data.get("registration_date")
        joining = cleaned_data.get("date_of_joining")

        if birth and registration and birth >= registration:
            self.add_error("date_of_birth", "Date of birth must be before registration date.")

        if joining and registration and joining <= registration:
            self.add_error("date_of_joining", "Joining date must be after registration date.")

        return cleaned_data

    def clean_first_name(self):
        value = (self.cleaned_data.get("first_name") or "").strip()
        if value and len(value) < 2:
            raise ValidationError("Please enter at least 2 characters.")
        return value

    def clean_last_name(self):
        value = (self.cleaned_data.get("last_name") or "").strip()
        if value and len(value) < 2:
            raise ValidationError("Please enter at least 2 characters.")
        return value

    def clean_place_of_birth(self):
        value = (self.cleaned_data.get("place_of_birth") or "").strip()
        if value and len(value) < 2:
            raise ValidationError("Please enter at least 2 characters.")
        return value