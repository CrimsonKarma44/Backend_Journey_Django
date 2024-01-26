def visitor_cookie_handler(request, response):
    from datetime import datetime

    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, then the default value of 1 is used.
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
    
        #update the last visit cookie now that we have updated the count
        response.set_cookie('last_visit', str(datetime.now()))
    
    else:
        visits = 1
    
        # set the last visit cookie
        response.set_cookie('last_visit', last_visit_cookie)
    
    # Update/set the visits cookie
    response.set_cookie('visits', visits)