from django.db import models

class Beneficiary(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=120)
    gender = models.CharField(max_length=20, default="Female")
    nationality = models.CharField(max_length=40)
    marital_status = models.CharField(max_length=20)
    settlement_camp = models.CharField(max_length=100)
    registration_date = models.DateField()
    date_of_joining = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "dateOfBirth": self.date_of_birth.isoformat(),
            "placeOfBirth": self.place_of_birth,
            "gender": self.gender,
            "nationality": self.nationality,
            "maritalStatus": self.marital_status,
            "settlementCamp": self.settlement_camp,
            "registrationDate": self.registration_date.isoformat(),
            "dateOfJoining": self.date_of_joining.isoformat(),
        }
