import logging
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from utils.db_utils import DBUtils
import os 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def finalize_upload_handler(
    s3Key: str,
    title: str,
    filetype: str,
    description: str,
    dayId: str,
    exerciseName: str,
    exerciseLabel: str,
    block: str,
    week: str,
    userID: str,
    type: str = "athlete",
):
    """
    Finalize the upload process by extracting metadata and updating the block table.
    """
    try:
        logger.info("Extracting metadata for S3 key: %s", s3Key)
        metadata = {
            "s3Key": s3Key,
            "title": title,
            "filetype": filetype,
            "type": type,
            "description": description,
            "dayId": dayId,
            "exerciseName": exerciseName,
            "exerciseLabel": exerciseLabel,
            "block": block,
            "week": week,
            "userID": userID,
        }
        logger.info(f"Extracted metadata: {metadata}")

        # Initialize the blocks table
        blocksTable = DBUtils(os.environ.get("BLOCK_TABLE", "blocks-dev"))

        # Fetch the block
        block, error = blocksTable.get_block_by_name(userID, block)
        if error:
            logger.error("Error retrieving block: %s", error)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Block not found",
            )

        # Access the week
        week_data = block.get("Block", {}).get("Weeks", {}).get(week)
        if not week_data:
            logger.error("Week %s not found in block %s", week, block)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Week not found",
            )

        # Access the day
        day_data = week_data.get("Days", {}).get(dayId)
        if not day_data:
            logger.error("Day %s not found in week %s", dayId, week)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Day not found",
            )

        # Access or initialize the exercises list
        exercises = day_data.get("Exercises", [])

        # Find the specific exercise
        exercise = next(
            (ex for ex in exercises if ex.get("name") == exerciseName and ex.get("label") == exerciseLabel),
            None
        )
        if not exercise:
            logger.error("Exercise %s not found in day %s", exerciseName, dayId)
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exercise not found",
            )

        # Add a Videos list if it doesn't exist
        if "Videos" not in exercise:
            exercise["Videos"] = []

        # Append the metadata to the Videos list
        exercise["Videos"].append({
            "s3Key": metadata["s3Key"],
            "title": metadata["title"],
            "filetype": metadata["filetype"],
            "description": metadata["description"],
            "type": metadata["type"],
        })

        # Update the block in the database
        blocksTable.table.update_item(
            Key={
                "Userid": userID,
                "Timestamp": block["Timestamp"]
            },
            UpdateExpression="SET #b.Weeks.#weekId.Days.#dayId.Exercises = :updated_exercises",
            ExpressionAttributeNames={
                "#b": "Block",
                "#weekId": week,
                "#dayId": dayId
            },
            ExpressionAttributeValues={
                ":updated_exercises": exercises
            }
        )

        logger.info("Successfully updated exercise with video metadata")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Video metadata added to exercise", "data": metadata},
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error("Error finalizing upload: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to finalize upload",
        )
