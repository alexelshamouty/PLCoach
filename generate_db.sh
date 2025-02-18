
aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "METADATA"}, 
    "title": {"S": "Block 1"}, 
    "created_at": {"S": "2025-02-24T17:42:24.910698Z"}, 
    "user_id": {"N": "1"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1"}, 
    "title": {"S": "Week 1"}, 
    "created_at": {"S": "2025-02-24T17:42:24.910698Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-02-25T17:42:24.910698Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-02-26T17:42:24.910698Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-02-27T17:42:24.910698Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#1#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2"}, 
    "title": {"S": "Week 2"}, 
    "created_at": {"S": "2025-03-03T17:42:25.916180Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-03-04T17:42:25.916180Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#1#EXERCISE#4"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-03-05T17:42:25.916180Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#2#EXERCISE#4"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-03-06T17:42:25.916180Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#3#EXERCISE#4"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-03-07T17:42:25.916180Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#4#EXERCISE#3"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#2#DAY#4#EXERCISE#4"}, 
    "name": {"S": "Hamstring Curls"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3"}, 
    "title": {"S": "Week 3"}, 
    "created_at": {"S": "2025-03-10T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-03-11T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-03-12T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-03-13T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-03-14T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#5"}, 
    "title": {"S": "Friday"}, 
    "created_at": {"S": "2025-03-15T17:42:26.921581Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#5#EXERCISE#1"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#3#DAY#5#EXERCISE#2"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4"}, 
    "title": {"S": "Week 4"}, 
    "created_at": {"S": "2025-03-17T17:42:27.926397Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-03-18T17:42:27.926397Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-03-19T17:42:27.926397Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block1"}, 
    "SK": {"S": "WEEK#4#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "METADATA"}, 
    "title": {"S": "Block 2"}, 
    "created_at": {"S": "2025-03-24T17:42:28.931971Z"}, 
    "user_id": {"N": "1"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5"}, 
    "title": {"S": "Week 5"}, 
    "created_at": {"S": "2025-03-24T17:42:28.931971Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-03-25T17:42:28.931971Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#1#EXERCISE#4"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-03-26T17:42:28.931971Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#2#EXERCISE#4"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-03-27T17:42:28.931971Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#5#DAY#3#EXERCISE#4"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6"}, 
    "title": {"S": "Week 6"}, 
    "created_at": {"S": "2025-03-31T17:42:29.936562Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-04-01T17:42:29.936562Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-04-02T17:42:29.936562Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-04-03T17:42:29.936562Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-04-04T17:42:29.936562Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#6#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7"}, 
    "title": {"S": "Week 7"}, 
    "created_at": {"S": "2025-04-07T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-04-08T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-04-09T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-04-10T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-04-11T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#4#EXERCISE#3"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#5"}, 
    "title": {"S": "Friday"}, 
    "created_at": {"S": "2025-04-12T17:42:30.941219Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#5#EXERCISE#1"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#5#EXERCISE#2"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#7#DAY#5#EXERCISE#3"}, 
    "name": {"S": "Hamstring Curls"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8"}, 
    "title": {"S": "Week 8"}, 
    "created_at": {"S": "2025-04-14T17:42:31.941771Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-04-15T17:42:31.941771Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#1#EXERCISE#4"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-04-16T17:42:31.941771Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block2"}, 
    "SK": {"S": "WEEK#8#DAY#2#EXERCISE#4"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "METADATA"}, 
    "title": {"S": "Block 3"}, 
    "created_at": {"S": "2025-04-21T17:42:32.945390Z"}, 
    "user_id": {"N": "1"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9"}, 
    "title": {"S": "Week 9"}, 
    "created_at": {"S": "2025-04-21T17:42:32.945390Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-04-22T17:42:32.945390Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-04-23T17:42:32.945390Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-04-24T17:42:32.945390Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#9#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10"}, 
    "title": {"S": "Week 10"}, 
    "created_at": {"S": "2025-04-28T17:42:33.947345Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-04-29T17:42:33.947345Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-04-30T17:42:33.947345Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-05-01T17:42:33.947345Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-05-02T17:42:33.947345Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#10#DAY#4#EXERCISE#3"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11"}, 
    "title": {"S": "Week 11"}, 
    "created_at": {"S": "2025-05-05T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-05-06T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#1#EXERCISE#3"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#1#EXERCISE#4"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-05-07T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#2#EXERCISE#3"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#2#EXERCISE#4"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#3"}, 
    "title": {"S": "Wednesday"}, 
    "created_at": {"S": "2025-05-08T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#3#EXERCISE#1"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#3#EXERCISE#2"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#3#EXERCISE#3"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#3#EXERCISE#4"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#4"}, 
    "title": {"S": "Thursday"}, 
    "created_at": {"S": "2025-05-09T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#4#EXERCISE#1"}, 
    "name": {"S": "Lunges"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#4#EXERCISE#2"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#4#EXERCISE#3"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#4#EXERCISE#4"}, 
    "name": {"S": "Hamstring Curls"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#5"}, 
    "title": {"S": "Friday"}, 
    "created_at": {"S": "2025-05-10T17:42:34.952791Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#5#EXERCISE#1"}, 
    "name": {"S": "Deadlift"}, 
    "label": {"S": "deadlift"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "6"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#5#EXERCISE#2"}, 
    "name": {"S": "Good Mornings"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#5#EXERCISE#3"}, 
    "name": {"S": "Hamstring Curls"}, 
    "label": {"S": "hamstrings"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "15"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#11#DAY#5#EXERCISE#4"}, 
    "name": {"S": "Leg Press"}, 
    "label": {"S": "legs"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12"}, 
    "title": {"S": "Week 12"}, 
    "created_at": {"S": "2025-05-12T17:42:35.954815Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#1"}, 
    "title": {"S": "Monday"}, 
    "created_at": {"S": "2025-05-13T17:42:35.954815Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#1#EXERCISE#1"}, 
    "name": {"S": "Bench Press"}, 
    "label": {"S": "chest"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "10"}, 
    "rpe": {"N": "8"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#1#EXERCISE#2"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#2"}, 
    "title": {"S": "Tuesday"}, 
    "created_at": {"S": "2025-05-14T17:42:35.954815Z"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#2#EXERCISE#1"}, 
    "name": {"S": "Pull-ups"}, 
    "label": {"S": "pull-ups"}, 
    "sets": {"N": "3"}, 
    "reps": {"N": "12"}, 
    "rpe": {"N": "7"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000


aws dynamodb put-item --table-name SweatyDuck --item '{
    "PK": {"S": "BLOCK#block3"}, 
    "SK": {"S": "WEEK#12#DAY#2#EXERCISE#2"}, 
    "name": {"S": "Squats"}, 
    "label": {"S": "squats"}, 
    "sets": {"N": "4"}, 
    "reps": {"N": "8"}, 
    "rpe": {"N": "9"}, 
    "comments": {"S": "Great work"}
}' --endpoint-url http://localhost:8000

