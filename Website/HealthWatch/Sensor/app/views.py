from django.shortcuts import render, HttpResponse, redirect
from app import urls
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
from pathlib import Path
import datetime
from .models import StoredData
import random
from twilio.rest import Client

# BASE_DIR = Path(__file__).resolve().parent.parent
# serviceKey = os.path.join(BASE_DIR, "serviceKey.json")
# cred = credentials.Certificate(serviceKey)
# firebase_admin.initialize_app(
#     cred, {"databaseURL": "https://fir-386c7-default-rtdb.firebaseio.com"}
# )
# data = db.reference("Data")

# Threshold values for different parameters in Fahrenheit
BODY_TEMP_HIGH_THRESHOLD_F = 100.4  # Fahrenheit
BODY_TEMP_LOW_THRESHOLD_F = 95.0  # Fahrenheit

ENV_TEMP_HIGH_THRESHOLD_F = 86.0  # Fahrenheit
ENV_TEMP_LOW_THRESHOLD_F = 65.0  # Fahrenheit

AIR_QUALITY_HIGH_THRESHOLD = 300  # ppm (adjusted range)
AIR_QUALITY_LOW_THRESHOLD = 100  # ppm

PULSE_RATE_HIGH_THRESHOLD = 100  # beats per minute
PULSE_RATE_LOW_THRESHOLD = 60  # beats per minute

SPO2_HIGH_THRESHOLD = 100  # percentage (assuming it can't exceed 100)
SPO2_LOW_THRESHOLD = 90  # percentage

account_sid = "ACfcb4ff679b2ffe82d4d74b2c922701e0"
auth_token = "d09b6bf5ba5d2047dc369623c96b760b"
client = Client(account_sid, auth_token)


def body_temp(request):
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")

    # Generate random real-world data for body temperature
    new_value = round(random.uniform(97.0, 99.0), 1)
    # new_value = 100
    if new_value >= BODY_TEMP_HIGH_THRESHOLD_F:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="High body temperature detected!",
            to="whatsapp:+916267247624",
        )
    elif new_value <= BODY_TEMP_LOW_THRESHOLD_F:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="Low body temperature detected!",
            to="whatsapp:+916267247624",
        )
    # Create or update HealthParameter instance with the new value
    obj = StoredData()
    obj.time = formatted_time
    obj.date = formatted_date
    obj.body_temp = new_value
    obj.save()

    # Get the previous 10 values
    SD = StoredData.objects.all()
    SD = list(SD)
    time = []
    previous_values = []
    date = []
    for S in SD:
        # ti = S.time.strftime("%H:%M:%S")
        # da = S.date.strftime("%Y-%m-%d")
        previous_values.append(S.body_temp)
        time.append(S.time)
        date.append(S.date)

    # Render the template with the data
    context = {
        "current_value": new_value,
        "previous_values": previous_values[-1:-21:-1],
        "time": time[-1:-21:-1],
        "date": date[-1:-21:-1],
    }
    return render(request, "body_temp.html", context)

def about_us(request):
    return render(request, "about_us.html")

def env_temp(request):
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")

    # Generate random real-world data for body temperature
    new_value = round(random.uniform(85.0, 90.0), 1)

    if new_value >= ENV_TEMP_HIGH_THRESHOLD_F:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="High environmental temperature detected!",
            to="whatsapp:+916267247624",
        )
    elif new_value <= ENV_TEMP_LOW_THRESHOLD_F:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="Low environmental temperature detected!",
            to="whatsapp:+916267247624",
        )

    # Create or update HealthParameter instance with the new value
    obj = StoredData()
    obj.time = formatted_time
    obj.date = formatted_date
    obj.env_temp = new_value
    obj.save()

    # Get the previous 10 values
    SD = StoredData.objects.all()
    SD = list(SD)
    time = []
    previous_values = []
    date = []
    for S in SD:
        # ti = S.time.strftime("%H:%M:%S")
        # da = S.date.strftime("%Y-%m-%d")
        previous_values.append(S.env_temp)
        time.append(S.time)
        date.append(S.date)

    # Render the template with the data
    context = {
        "current_value": new_value,
        "previous_values": previous_values[-1:-21:-1],
        "time": time[-1:-21:-1],
        "date": date[-1:-21:-1],
    }
    return render(request, "env_temp.html", context)

def gases(request):
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")

    # Generate random real-world data for body temperature
    new_value = round(random.uniform(50, 300), 1)

    if new_value >= AIR_QUALITY_HIGH_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="High air quality detected!",
            to="whatsapp:+916267247624",
        )
    elif new_value <= AIR_QUALITY_LOW_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="Low air quality detected!",
            to="whatsapp:+916267247624",
        )

    # Create or update HealthParameter instance with the new value
    obj = StoredData()
    obj.time = formatted_time
    obj.date = formatted_date
    obj.air_quality = new_value
    obj.save()

    # Get the previous 10 values
    SD = StoredData.objects.all()
    SD = list(SD)
    time = []
    previous_values = []
    date = []
    for S in SD:
        # ti = S.time.strftime("%H:%M:%S")
        # da = S.date.strftime("%Y-%m-%d")
        previous_values.append(S.air_quality)
        time.append(S.time)
        date.append(S.date)

    # Render the template with the data
    context = {
        "current_value": new_value,
        "previous_values": previous_values[-1:-21:-1],
        "time": time[-1:-21:-1],
        "date": date[-1:-21:-1],
    }
    return render(request, "gases.html", context)

def pulse_rate(request):
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")

    # Generate random real-world data for body temperature
    new_value = round(random.uniform(60, 100), 1)

    if new_value >= PULSE_RATE_HIGH_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="High pulse rate detected!",
            to="whatsapp:+916267247624",
        )
    elif new_value <= PULSE_RATE_LOW_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="Low pulse rate detected!",
            to="whatsapp:+916267247624",
        )

    # Create or update HealthParameter instance with the new value
    obj = StoredData()
    obj.time = formatted_time
    obj.date = formatted_date
    obj.pulse_rate = new_value
    obj.save()

    # Get the previous 10 values
    SD = StoredData.objects.all()
    SD = list(SD)
    time = []
    previous_values = []
    date = []
    for S in SD:
        # ti = S.time.strftime("%H:%M:%S")
        # da = S.date.strftime("%Y-%m-%d")
        previous_values.append(S.pulse_rate)
        time.append(S.time)
        date.append(S.date)

    # Render the template with the data
    context = {
        "current_value": new_value,
        "previous_values": previous_values[-1:-21:-1],
        "time": time[-1:-21:-1],
        "date": date[-1:-21:-1],
    }
    return render(request, "pulse_rate.html", context)

def spO2(request):
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")

    # Generate random real-world data for body temperature
    new_value = round(random.uniform(60, 100), 1)

    if new_value >= SPO2_HIGH_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="High oxygen saturation detected!",
            to="whatsapp:+916267247624",
        )
    elif new_value <= SPO2_LOW_THRESHOLD:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="Low oxygen saturation detected!",
            to="whatsapp:+916267247624",
        )

    # Create or update HealthParameter instance with the new value
    obj = StoredData()
    obj.time = formatted_time
    obj.date = formatted_date
    obj.spo2_level = new_value
    obj.save()

    # Get the previous 10 values
    SD = StoredData.objects.all()
    SD = list(SD)
    time = []
    previous_values = []
    date = []
    for S in SD:
        # ti = S.time.strftime("%H:%M:%S")
        # da = S.date.strftime("%Y-%m-%d")
        previous_values.append(S.spo2_level)
        time.append(S.time)
        date.append(S.date)

    # Render the template with the data
    context = {
        "current_value": new_value,
        "previous_values": previous_values[-1:-21:-1],
        "time": time[-1:-21:-1],
        "date": date[-1:-21:-1],
    }
    return render(request, "spO2.html", context)

def location(request):
    return render(request, "location.html")
