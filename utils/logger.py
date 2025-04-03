import json
import logging

# Configure Logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_request_response(response, request_body=None,params=None):
    """
    Logs the API request (if available) and response in a readable JSON format.

    :param url: API endpoint URL
    :param response: API response object
    :param request_body: (Optional) Request payload (dictionary)
    """
    # Pretty-print request body if provided
    request_log = ""
    if request_body is not None:
        request_log = f"\nBody:\n{json.dumps(request_body, indent=4)}"

    if params is not None:
        request_log += f"\nParams:\n{json.dumps(params, indent=4)}"

    # Handle response body formatting
    try:
        response_body_pretty = json.dumps(response.json(), indent=4)
    except ValueError:
        response_body_pretty = response.text  # In case response is not JSON

    # Log the details
    logger.info(f"===== REQUEST =====\nURL:{request_log}")
    logger.info(f"===== RESPONSE =====\nStatus Code: {response.status_code}\nBody:\n{response_body_pretty}")

    # Print for pytest reports
    print("\n===== REQUEST =====")
    # print(f"URL: {url}")
    if params is not None:
        print(f"Params:\n{json.dumps(params, indent=4)}")

    if request_body is not None:
        print(f"Body:\n{json.dumps(request_body, indent=4)}")

    print("\n===== RESPONSE =====")
    print(f"Status Code: {response.status_code}")
    print(f"Body:\n{response_body_pretty}")
