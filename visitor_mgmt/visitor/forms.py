from django.shortcuts import render


def cookie_formView(request):
    if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
        username = request.COOKIES['username']
        last_connection = request.COOKIES['last_connection']
        last_connection_time = datetime.datetime.strptime(last_connection[:-7],
                                                          "%Y-%m-%d %H:%M:%S")
        if (datetime.datetime.now() - last_connection_time).seconds < 10:
            return render(request, 'loggedin.html', {"username": username})
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})
