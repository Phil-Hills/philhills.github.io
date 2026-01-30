import functions_framework
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

@functions_framework.http
def submit_lead(request):
    """HTTP Cloud Function to receive lead form submissions."""
    
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    try:
        # Parse content
        content_type = request.headers.get('content-type')
        if content_type == 'application/json':
            request_json = request.get_json(silent=True)
            if request_json:
                data = request_json
            else:
                return ('Invalid JSON', 400, headers)
        elif content_type == 'application/x-www-form-urlencoded':
             data = request.form.to_dict()
        else:
            return ('Unknown content type', 400, headers)

        # Log the lead (This effectively "saves" it to Cloud Logging)
        logging.info(f"New Lead Received: {json.dumps(data)}")

        # Professional Response ensuring the user feels handled
        response_data = {
            "success": True,
            "message": "Thank you. Your request has been routed to our enterprise team.",
            "next_steps": "A systems architect will review your infrastructure profile and contact you within 24 hours to schedule your audit."
        }

        return (json.dumps(response_data), 200, headers)

    except Exception as e:
        logging.error(f"Error processing lead: {e}")
        return (f"Internal Server Error: {e}", 500, headers)
