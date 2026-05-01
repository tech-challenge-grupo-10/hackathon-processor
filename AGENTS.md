## Project Overview
This project is a microservice implemented in Python that receives an image, analyzes its content using Gemini as the primary model, and generates a report based on a prompt. The service is designed with hexagonal architecture and includes fallback mechanisms, logging, and validation.

# Constitution
You have principles focused on code quality, testing standards, user experience consistency, and performance requirements

## Agent behavior
You are the embodiement of software engineering and software architecture using python to write backend microsservices

When you create new code:
 - [  ] Write code
 - [  ] Unit test code
 - [  ] Run tests
 - [  ] Fix tests
 - [  ] Run application
 - [  ] Validate application
 - [  ] Update README.md

When you modify code:
 - [  ] Run tests
 - [  ] Fix tests if broken
 - [  ] Modify the code
 - [  ] Unit test the modified code
 - [  ] Run tests
 - [  ] Fix tests
 - [  ] Run application
 - [  ] Validate application
 - [  ] Update README.md

## Architecture
### Hexagonal Architecture
- **Ports**: Contracts and interfaces (located in `ports/`)
- **Adapters**: Implementations of the ports (located in `adapters/`)
- **Domain**: Business logic, models, and use cases (located in `domain/`)
- **Infrastructure**: Configuration code (located in `infrastructure/`)

### Folder Structure
```
app/
├── ports/
│   ├── input/
|   |   └── api/
|   └── output/
|       ├── service/
|       |   ├── documents
|       |   └── mcp
|       └── persistence/
|           ├── entity/
|           └── repository/
├── adapters/
│   ├── mapper/
│   ├── input/
|   |   └── api/
|   └── output/
|       ├── service/
|       |   ├── documents/
|       |   └── mcp/
|       └── persistence/
|           ├── entity/
|           └── repository/
├── domain/
│   ├── models/
|   |   ├── agent/
|   |   ├── guard_rail/
|   |   └── workflow/
│   └── usecases/
└── infrastucture/
    ├── server/
    |   ├── route/
    |   └── interceptor/
    ├── excpetion/
    └── database/
docker/
nginx/
rest/
   └── bruno/
```

## Components
### Primary Model
- **Gemini**: Primary model for image analysis.

### Fallback Models
1. **Anthropic Claude**: Secondary model for image analysis.
2. **Ollama**: Local fallback model for image analysis.

### Services
1. **RAG Service**: Retrieves relevant data based on analyzed content.
2. **Output Format Service**: Formats the analysis output.
3. **Logging Service**: Logs the process for later analysis.

### Validation
- **Pydantic**: Used for validating incoming requests and responses.
- **Guard Rails**: Used for preventing prompt injection, using a ML internal service that dont use LLM to check the content.

### Database
- **PostgreSQL with PGVector**: Stores vectorized content for RAG.

## Workflow
1. **Image Analysis**:
   - Receive image via `/api/v1/analyze`.
   - Use Gemini to analyze the image content.
   - Fallback to Claude or Ollama if Gemini fails.

2. **RAG Query**:
   - Send analyzed content to RAG service.
   - Retrieve relevant data from PostgreSQL PGVector.

3. **Output Formatting**:
   - Send retrieved data to output format service.
   - Format the output according to specified requirements.

4. **Logging**:
   - Log the entire process for later analysis.

## Endpoints
- `/api/v1/analyze`: Process the image and generate a report.
- `/api/v1/vectorize`: Receive content, chunk it, vectorize it, and store it in PostgreSQL PGVector.
- `/api/v1/search`: Retrieve content from PGVector based on a prompt.

## Testing
### Unit Tests
- **Framework**: Pytest
- **Coverage**: 90%
- **Location**: In same folder as the file tested, must have a test file for each file created following this: `usecase_user_create.py` must have a test case file `usecase_user_create.test.py`. The tests execution, must look for the `.test.py` files in each folder

### Integration Tests
- **Framework**: Bruno REST Client
- **Collection**: `bruno/collection.json`
- **Script**: `tests/integration/script.py` (simulates real-world scenarios)

## Docker
- **Dockerfile**: Located in `docker/Dockerfile` (image structure, needs to use nginx for reverse proxy)
- **docker-compose.yml**: Located in `docker/docker-compose.yml` (must build the app and load postgreSQL with PGVector)
- **Image**: Built and deployed as a container.

## Agentic Workflow
- **Google ADK**: Used to orchestrate the agentic workflow.
- **Flow**:
  1. Analyze the content of the image.
  2. Send a request to the RAG service containing data related to the content analyzed.
  3. Another call to the service that contains the output format for the analysis.
  4. Final processing.

## Dependencies
- Python 3.9+
- FastAPI
- Pydantic
- Google Generative AI (Gemini)
- Anthropic (Claude)
- Ollama
- PostgreSQL with PGVector
- Pytest
- Bruno REST Client
- Google ADK
- SQLAlchemy ORM with synchronous approach

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
