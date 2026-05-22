# Ex.04 Design a Website for Server Side Processing
## Date:22-05-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<!DOCTYPE html>
<html>
<head>
    <title>GST Bill Calculator</title>

    <style>
        body{
            background-color:lightblue;
            text-align:center;
            margin-top:80px;
            font-family:Arial;
        }

        input{
            width:150px;
            height:25px;
        }

        button{
            margin-top:15px;
        }
    </style>

</head>

<body>

<h1>GST Bill Calculator</h1>

<form method="POST">
    {% csrf_token %}

    <label>Enter Price:</label>
    <br><br>

    <input type="text" name="price">
    <br><br>

    <label>Enter GST %:</label>
    <br><br>

    <input type="text" name="gst">
    <br><br>

    <button type="submit">Calculate</button>
</form>

{% if total %}
    <h2>Price : {{price}}</h2>
    <h2>GST : {{gst}}%</h2>
    <h2>Total Bill Amount : {{total}}</h2>
{% endif %}

</body>
</html>

from django.shortcuts import render

def gst_bill(request):
    context = {}

    if request.method == 'POST':
        price = request.POST.get('price')
        gst = request.POST.get('gst')

        if price and gst:
            price = float(price)
            gst = float(gst)

            total = price + (price * gst / 100)

            context['price'] = price
            context['gst'] = gst
            context['total'] = round(total, 2)

    return render(request, 'app4/math.html', context)

from django.contrib import admin
from django.urls import path
from app4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gst_bill, name='gst'),
]
```

## OUTPUT - SERVER SIDE:

![alt text](<Screenshot 2026-05-22 132746.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot 2026-05-22 132846.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
