import json
from datetime import date

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import BeneficiaryForm
from .models import Beneficiary


def home(request):
    show_form = request.path.rstrip("/") == "/register"
    success = request.GET.get("success") == "1"

    if request.method == "POST":
        form_data = request.POST.copy()
        field_names = {
            "firstName": "first_name",
            "lastName": "last_name",
            "dateOfBirth": "date_of_birth",
            "placeOfBirth": "place_of_birth",
            "maritalStatus": "marital_status",
            "settlementCamp": "settlement_camp",
            "registrationDate": "registration_date",
            "dateOfJoining": "date_of_joining",
        }
        for submitted_name, form_name in field_names.items():
            form_data[form_name] = form_data.get(submitted_name, "")

        form = BeneficiaryForm(form_data)
        if form.is_valid():
            form.save()
            return redirect("register_list")
    else:
        form = BeneficiaryForm()

    template_name = "register.html" if show_form else "index.html"
    context = {"form": form, "show_form": show_form, "success": success}
    return render(request, template_name, context)


def register_list(request):
    records = Beneficiary.objects.order_by("-created_at")
    return render(request, "register_list.html", {"beneficiaries": records})


@csrf_exempt
def beneficiaries(request):
    if request.method == "GET":
        return JsonResponse([record.as_dict() for record in Beneficiary.objects.all()], safe=False)
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        payload = json.loads(request.body)
        required = [
            "firstName",
            "lastName",
            "dateOfBirth",
            "placeOfBirth",
            "nationality",
            "maritalStatus",
            "settlementCamp",
            "registrationDate",
            "dateOfJoining",
        ]

        if any(not payload.get(key) for key in required):
            return JsonResponse({"error": "All required fields must be provided"}, status=400)

        birth_date = date.fromisoformat(payload["dateOfBirth"])
        registration_date = date.fromisoformat(payload["registrationDate"])
        joining_date = date.fromisoformat(payload["dateOfJoining"])

        if (
            len(payload["firstName"].strip()) < 2
            or len(payload["lastName"].strip()) < 2
            or len(payload["placeOfBirth"].strip()) < 2
        ):
            return JsonResponse({"error": "Names and place of birth must be at least 2 characters"}, status=400)

        if birth_date >= registration_date or joining_date <= registration_date:
            return JsonResponse({"error": "Dates do not follow the required order"}, status=400)

        record = Beneficiary.objects.create(
            first_name=payload["firstName"].strip(),
            last_name=payload["lastName"].strip(),
            date_of_birth=birth_date,
            place_of_birth=payload["placeOfBirth"].strip(),
            gender=payload.get("gender", "Female"),
            nationality=payload["nationality"],
            marital_status=payload["maritalStatus"],
            settlement_camp=payload["settlementCamp"],
            registration_date=registration_date,
            date_of_joining=joining_date,
        )
        return JsonResponse(record.as_dict(), status=201)
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return JsonResponse({"error": "Invalid registration data"}, status=400)
