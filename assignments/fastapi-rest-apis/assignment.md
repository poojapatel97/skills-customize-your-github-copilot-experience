# Building REST APIs with FastAPI

- Learning objectives:
  - Set up a FastAPI project and run a development server
  - Design RESTful endpoints (GET, POST, PUT, DELETE) with proper status codes
  - Use Pydantic models for request validation and response models
  - Handle errors and return meaningful HTTP responses
  - Write basic integration tests using FastAPI's TestClient
  - Expose interactive API docs (OpenAPI/Swagger)

- Difficulty: Intermediate
- Estimated time: 3–5 hours
- Files provided:
  - starter/main.py
  - starter/models.py
  - starter/data_store.py
  - tests/test_api.py
  - requirements.txt
- Instructions:
  1. Create a virtual environment and install dependencies:
     - python3 -m venv .venv
     - source .venv/bin/activate
     - pip install -r requirements.txt
  2. Implement the API in `starter/main.py` so it provides:
     - GET /items — list items (support optional query params: limit, skip)
     - GET /items/{item_id} — get one item or 404
     - POST /items — create item (validate input)
     - PUT /items/{item_id} — update item (partial or full)
     - DELETE /items/{item_id} — delete item (return 204)
     - Use Pydantic models from `starter/models.py`
     - Use the in-memory datastore in `starter/data_store.py`
     - Provide clear error messages and appropriate status codes
  3. Ensure the interactive docs are available at /docs and /redoc.
  4. Add or update tests in `tests/test_api.py` so they pass.
  5. Add examples of curl or httpie requests to the README portion in this file.
- Submission format:
  - Push to a Git branch or provide a zip with the assignment folder containing your implementation and README with run instructions.
- Rubric (100 pts):
  - Correctness & endpoints implemented: 40
  - Validation & error handling: 20
  - Tests implemented & passing: 20
  - Documentation & examples: 10
  - Code clarity & style: 10
