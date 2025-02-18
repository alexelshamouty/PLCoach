import datetime
from time import sleep

# Re-defining the training data expansion after execution state reset

# Expanding the training data structure to 12 weeks
training_data = {}

# Define sample exercises for rotation
exercise_variations = [
    {"name": "Bench Press", "label": "chest", "sets": 4, "reps": 10, "comments": "Great work", "rpe": 8},
    {"name": "Pull-ups", "label": "pull-ups", "sets": 3, "reps": 12, "comments": "Great work", "rpe": 7},
    {"name": "Squats", "label": "squats", "sets": 4, "reps": 8, "comments": "Great work", "rpe": 9},
    {"name": "Lunges", "label": "legs", "sets": 3, "reps": 15, "comments": "Great work", "rpe": 7},
    {"name": "Deadlift", "label": "deadlift", "sets": 4, "reps": 6, "comments": "Great work", "rpe": 9},
    {"name": "Good Mornings", "label": "hamstrings", "sets": 3, "reps": 12, "comments": "Great work", "rpe": 8},
    {"name": "Hamstring Curls", "label": "hamstrings", "sets": 4, "reps": 15, "comments": "Great work", "rpe": 7},
    {"name": "Leg Press", "label": "legs", "sets": 4, "reps": 12, "comments": "Great work", "rpe": 9},
    {"name": "Incline Press", "label": "chest", "sets": 3, "reps": 10, "comments": "Great work", "rpe": 7},
    {"name": "Step-ups", "label": "legs", "sets": 3, "reps": 10, "comments": "Great work", "rpe": 7},
    {"name": "Triceps Dips", "label": "chest", "sets": 3, "reps": 12, "comments": "Great work", "rpe": 7},
    {"name": "Hack Squats", "label": "legs", "sets": 4, "reps": 10, "comments": "Great work", "rpe": 8},
]

# Define a list of days in a week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Generate 12 weeks of training data
for week in range(1, 13):
    training_data[str(week)] = []
    
    # Each week has 2-5 training days
    num_days = (week % 4) + 2  # Ensuring variety in days (2 to 5 days per week)
    
    for day_index in range(num_days):
        day_name = days_of_week[day_index % len(days_of_week)]
        
        # Select a subset of exercises for variation
        num_exercises = (week % 3) + 2  # Ensuring variety in exercises (2 to 4 per day)
        exercises = exercise_variations[day_index:num_exercises + day_index]

        # Append training day with selected exercises
        training_data[str(week)].append({
            "title": day_name,
            "content": exercises
        })


# Constants
user_id = 1

# Generate AWS CLI commands
aws_commands = []

for week, days in training_data.items():
    start_date = datetime.datetime.utcnow()
    sleep(1)
    block_number = (int(week) - 1) // 4 + 1  # Every 4 weeks create a new block
    block_id = f"BLOCK#block{block_number}"
    week_id = f"WEEK#{week}"
    week_date = start_date + datetime.timedelta(weeks=int(week))

    # Add the block (if not already added)
    if int(week) % 4 == 1:
        aws_commands.append(f"""
aws dynamodb put-item --table-name SweatyDuck --item '{{
    "PK": {{"S": "{block_id}"}}, 
    "SK": {{"S": "METADATA"}}, 
    "title": {{"S": "Block {block_number}"}}, 
    "created_at": {{"S": "{week_date.isoformat()}Z"}}, 
    "user_id": {{"N": "{user_id}"}}
}}' --endpoint-url http://localhost:8000
""")

    # Add the week
    aws_commands.append(f"""
aws dynamodb put-item --table-name SweatyDuck --item '{{
    "PK": {{"S": "{block_id}"}}, 
    "SK": {{"S": "{week_id}"}}, 
    "title": {{"S": "Week {week}"}}, 
    "created_at": {{"S": "{week_date.isoformat()}Z"}}
}}' --endpoint-url http://localhost:8000
""")

    # Add days and exercises
    for day_index, day in enumerate(days, start=1):
        day_id = f"{week_id}#DAY#{day_index}"
        day_date = week_date + datetime.timedelta(days=day_index)

        aws_commands.append(f"""
aws dynamodb put-item --table-name SweatyDuck --item '{{
    "PK": {{"S": "{block_id}"}}, 
    "SK": {{"S": "{day_id}"}}, 
    "title": {{"S": "{day['title']}"}}, 
    "created_at": {{"S": "{day_date.isoformat()}Z"}}
}}' --endpoint-url http://localhost:8000
""")

        # Add exercises
        for exercise_index, exercise in enumerate(day["content"], start=1):
            exercise_id = f"{day_id}#EXERCISE#{exercise_index}"
            aws_commands.append(f"""
aws dynamodb put-item --table-name SweatyDuck --item '{{
    "PK": {{"S": "{block_id}"}}, 
    "SK": {{"S": "{exercise_id}"}}, 
    "name": {{"S": "{exercise['name']}"}}, 
    "label": {{"S": "{exercise['label']}"}}, 
    "sets": {{"N": "{exercise['sets']}"}}, 
    "reps": {{"N": "{exercise['reps']}"}}, 
    "rpe": {{"N": "{exercise['rpe']}"}}, 
    "comments": {{"S": "{exercise['comments']}"}}
}}' --endpoint-url http://localhost:8000
""")

# Join all commands into a single string
aws_commands_str = "\n".join(aws_commands)

print(aws_commands_str)
