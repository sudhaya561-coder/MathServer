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