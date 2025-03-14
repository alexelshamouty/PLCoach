
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handle_get_days_by_week(query_params, dbUtils, responseUtils):
        
        user_id = query_params.get('userId')
        week_id = query_params.get('weekId')
        block_id = query_params.get('blockId')

        logger.info(f"Processing getDaysByWeek request for userId: {user_id} blockId: {block_id} weekId: {week_id}")
        
        if not block_id:
            logger.error("Missing blockId parameter for getDaysByWeek")
            return responseUtils.error_response(400, "Missing blockId parameter")
            
        if not week_id:
            logger.error("Missing weekId parameter for getDaysByWeek")
            return responseUtils.error_response(400, "Missing weekId parameter")
            
        logger.info("Getting days for block: %s, week: %s", block_id, week_id)

        # Get block information
        block, error = dbUtils.get_block_by_name(user_id, block_id)
        if error:
            return error
        if not block:
            return responseUtils.error_response(404, f"Block not found: {block_id}")
        
        # Get week information
        week = block.get('Block', {}).get('Weeks', {}).get(week_id)
        if not week:
            return responseUtils.error_response(404, f"Week not found: {week_id}")
        
        # Get days array
        days = week.get('Days', [])
        logger.info(f"Found days: {days}")
        return responseUtils.success_response({
            'days': days
        })