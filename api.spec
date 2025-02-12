openapi: 3.0.0
info:
  title: Coaching Platform API
  description: API specification for managing coaches, athletes, training programs, and tracking progress.
  version: 1.0.0
servers:
  - url: https://api.coachingplatform.com/v1
    description: Production server

paths:
  /auth/login:
    post:
      summary: Authenticate user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Successful login
        '401':
          description: Unauthorized

  /auth/register:
    post:
      summary: Register new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                password:
                  type: string
                role:
                  type: string
                  enum: [coach, athlete]
      responses:
        '201':
          description: User registered

  /users:
    get:
      summary: List all users
      responses:
        '200':
          description: A list of users
    post:
      summary: Add a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
                role:
                  type: string
                  enum: [coach, athlete]
      responses:
        '201':
          description: User created

  /users/{id}:
    get:
      summary: View user profile
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User details
    put:
      summary: Update user profile
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                email:
                  type: string
      responses:
        '200':
          description: Profile updated
    delete:
      summary: Delete user
      responses:
        '204':
          description: User deleted

  /training-programs:
    get:
      summary: List training programs
      responses:
        '200':
          description: A list of training programs
    post:
      summary: Create new training program
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                description:
                  type: string
      responses:
        '201':
          description: Training program created

  /workouts:
    get:
      summary: Get all workouts
      responses:
        '200':
          description: A list of workouts
    post:
      summary: Log workout
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                athlete_id:
                  type: string
                exercise:
                  type: string
                reps:
                  type: integer
                rpe:
                  type: integer
      responses:
        '201':
          description: Workout logged
