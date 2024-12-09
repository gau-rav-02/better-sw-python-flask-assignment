# Library Management System

## How to Run
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python app.py`.
4. Use tools like Postman to interact with the API.

## Design Choices
1. In-memory storage for simplicity.
2. Clear separation of concerns: routes, models, authentication.

## Assumptions
1. Tokens are hardcoded.
2. No database integration (no third-party libraries).

## Limitations
1. Data is not persistent across restarts.
2. Basic error handling.
