import json

CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Type': 'application/json'
}

def check_authorization(event, required_groups=None):
    """Check if user has required group permissions"""
    if required_groups is None:
        required_groups = ['coaches']
        
    groups = event['cognitoPoolClaims'].get('groups', [])
    return any(group in groups for group in required_groups)

def authorize(event, required_groups=None):
    """Authorization middleware that returns error response if unauthorized"""
    if not check_authorization(event, required_groups):
        return error_response(403, 'Unauthorized')
    return None

def create_response(status_code, body):
    """Create a standardized API response with CORS headers"""
    return {
        'statusCode': status_code,
        'headers': CORS_HEADERS,
        'body': json.dumps(body)
    }

def error_response(status_code, message):
    """Create a standardized error response"""
    return create_response(status_code, {'error': message})

def success_response(data):
    """Create a standardized success response"""
    return create_response(200, data)
