from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalcheckoutsdk.core import SandboxEnvironment, PayPalHttpClient
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from .forms import ImageForm
from django.shortcuts import redirect
from .models import City


def home(request):
    return render(request, "index.html")

def aboutUs(request):
    pass

def contact(request):
    pass

def explore(request):
    cities = City.objects.all()
    return render(request, "explore.html", {"cities": cities})

def book(request):
    pass

def experience(request):
    pass

def help(request):
    pass


def create(request, id):
    if request.method =="POST":
        environment = SandboxEnvironment(client_id=settings.PAYPAL_CLIENT_ID, client_secret=settings.PAYPAL_SECRET_ID)
        client = PayPalHttpClient(environment)
        city = City.objects.get(pk=id)
        create_order = OrdersCreateRequest()

        #order            
        create_order.request_body (
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "USD",
                            "value": city.tourist_price,
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": city.tourist_price
                                }
                                },
                            },                               


                    }
                ]
            }
        )

        response = client.execute(create_order)
        data = response.result.__dict__['_dict']
        print(city.tourist_price)
        return JsonResponse(data)
    else:
        print("error2")
        return JsonResponse({'details': "invalide request"})

    

def capture(request, order_id, id):
    if request.method =="POST":
        capture_order = OrdersCaptureRequest(order_id)
        environment = SandboxEnvironment(client_id=settings.PAYPAL_CLIENT_ID, client_secret=settings.PAYPAL_SECRET_ID)
        client = PayPalHttpClient(environment)
        response = client.execute(capture_order)
        data = response.result.__dict__['_dict']
        return JsonResponse(data)
    else:
        return JsonResponse({'details': "invalide request"})

def getClientId(request):
    pass

def pay(request, pk):
    #line 10
    client_id = settings.PAYPAL_CLIENT_ID
    city = get_object_or_404(City, pk=pk)
    return render(request, 'payment.html', {'city':city, 'client_id':client_id })

@login_required(login_url="login/")
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if not form.is_valid():
            city = City.objects.create(
                name=request.POST["name"],
                description=request.POST["description"],
                tourist_price=request.POST["tourist_price"],
                city_poster=request.FILES,
                user=request.user
                )
            city.save()
            return render(request, "upload_succesful.html")
    return render(request, 'upload_image.html')