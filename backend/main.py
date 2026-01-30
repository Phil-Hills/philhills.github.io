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
        # In a real production scenario, you might write this to Firestore or Google Sheets.
        logging.info(f"New Lead Received: {json.dumps(data)}")

        # Redirect back to the website with a success parameter (optional, if using form post)
        # For this implementation, we'll return a JSON success response for AJAX or simple success text for form POST
        return ('Success! Lead received.', 200, headers)

    except Exception as e:
        logging.error(f"Error processing lead: {e}")
        return (f"Internal Server Error: {e}", 500, headers)
