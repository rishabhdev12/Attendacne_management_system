import logging
from datetime import datetime

logging.basicConfig(filename='logs/django.log',level=logging.INFO)
class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the current datetime
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Datetime: {current_datetime}")
        
        # Log request data and URL path
        logging.info(f"Request Path: {request.path}")
        logging.info(f"Request Method: {request.method}")
        logging.info(f"Request Headers: {request.headers}")
        
        # Log GET or POST data
        if request.method == 'GET':
            logging.info(f"GET Data: {request.GET.dict()}")
        elif request.method == 'POST':
            logging.info(f"POST Data: {request.POST.dict()}")
            # If the request has a JSON body
            if request.content_type == 'application/json':
                try:
                    logging.info(f"JSON Body: {request.body.decode('utf-8')}")
                except Exception as e:
                    logging.warning(f"Failed to decode JSON body: {e}")

        # Call the next middleware or view
        response = self.get_response(request)

        # Log response data
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Content: {response.content.decode('utf-8')}")

        return response
