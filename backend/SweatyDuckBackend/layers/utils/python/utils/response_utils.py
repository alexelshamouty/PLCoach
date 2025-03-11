import json
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CORS_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Type': 'application/json'
}

def check_authorization(context, required_groups=None):
    """Check if user has required group permissions"""
    if required_groups is None:
        required_groups = ['coaches']
        
    groups = context['authorizer'].get('claims', []).get('cognito:groups', [])
    is_authorized = any(group in groups for group in required_groups)
    logger.info(f"Authorization check - Required groups: {required_groups}, User groups: {groups}, Result: {is_authorized}")
    return is_authorized

def authorize(context, required_groups=None):
    """Authorization middleware that returns error response if unauthorized"""
    request_id = context.get('requestContext', {}).get('requestId', 'unknown')
    request_context = context.get('requestContext', {})
    logger.info(f"Authorization request - RequestId: {request_id}")
    
    if not check_authorization(request_context, required_groups):
        logger.warning(f"Authorization failed - RequestId: {request_id}")
        return error_response(403, 'Unauthorized')
    
    logger.info(f"Authorization successful - RequestId: {request_id}")
    return None

def create_response(status_code, body):
    """Create a standardized API response with CORS headers"""
    logger.debug(f"Creating response - Status: {status_code}, Body: {body}")
    return {
        'statusCode': status_code,
        'headers': CORS_HEADERS,
        'body': json.dumps(body)
    }

def error_response(status_code, message):
    """Create a standardized error response"""
    logger.error(f"Error response - Status: {status_code}, Message: {message}")
    return create_response(status_code, {'error': message})

def success_response(data):
    """Create a standardized success response"""
    logger.info(f"Success response - Data: {data}")
    return create_response(200, data)
