If client-side cookies are the right approach for you, then work through the following steps.

    1. You must first perform a check to see if the cookie you want exists. Checking the 
request parameter parameter will allow you to do this. The request.COOKIES.has_key 
('<cookie_- name>') function returns a boolean value indicating whether a cookie 
<cookie_name> exists on the client’s computer or not.

    2. If the cookie exists, you can then retrieve its value - again via the request 
parameter - with request.COOKIES[]. The COOKIES attribute is exposed as a dictionary, so pass the name of the cookie you wish to retrieve as a string between the square brackets. 
Remember, cookies are all returned as strings, regardless of what they contain. You must 
therefore be prepared to cast to the correct type (with int() or float(), for example).

    3. If the cookie doesn’t exist, or you wish to update the cookie, pass the value you wish 
to save to the response you generate. response.set_cookie('<cookie_name>', value) is the 
function you call, where two parameters are supplied: the name of the cookie, and the value 
you wish to set it to.


If you need more secure cookies, then use session based cookies.

    1. Firstly, ensure that the MIDDLEWARE_CLASSES list in your Django project’s settings.py 
module contains django.contrib.sessions.middleware.SessionMiddleware. If it doesn’t, add it 
to the list.

    2. Configure your session backend SESSION_ENGINE. See the official Django Documentation on
Sessions for the various backend configurations.

    3. Check to see if the cookie exists via requests.sessions.get().

    4. Update or set the cookie via the session dictionary, requests.session['<cookie_name>'].