# FindersKeepers API

FindersKeepers is a secure RESTful Lost and Found Management System built using Flask.  
The system enables users to register, authenticate using JWT, post lost or found items, submit claims, and manage claim approval workflows.

The application follows a modular backend architecture and is fully containerized using Docker. It supports CI/CD integration for automated builds and Docker image creation, and is deployment-ready for cloud environments such as AWS EC2.

---

## 1. Problem Statement

In institutions such as colleges or campuses, lost and found item tracking is often handled manually. This results in:

- Lack of structured verification  
- Security issues  
- No centralized tracking  
- No digital claim approval workflow  
- Poor accountability  

FindersKeepers provides a secure backend solution that manages item reporting and claim validation using authentication and authorization mechanisms.

---

## 2. Features

### Authentication & Security

- User registration  
- Secure login using JWT tokens  
- Protected API endpoints  
- Role-based authorization  
- Ownership validation  
- Prevention of unauthorized access  
- Duplicate claim prevention  

### Item Management

- Post lost items  
- Post found items  
- Retrieve all items  
- Automatic item status tracking  
- Owner-linked items  

### Claim Workflow

- Submit claim for an item  
- Prevent users from claiming their own items  
- Owner can approve or reject claims  
- Item status updates after approval  
- Claim state tracking (pending, approved, rejected)  

### DevOps & Deployment

- Dockerized backend  
- CI/CD pipeline support (Jenkins or GitHub Actions)  
- Docker image pushed to DockerHub  
- Cloud deployment ready (AWS EC2 compatible)  

---

## 3. Tech Stack

### Backend

- Python 3  
- Flask  
- Flask-SQLAlchemy  
- Flask-JWT-Extended  

### Database

- PostgreSQL (Dockerized)  

### DevOps

- Docker  
- Docker Compose  
- Jenkins or GitHub Actions  

### Server

- Gunicorn  

---

## 4. Project Architecture

### Folder Structure
finders-keepers/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   ├── user.py
│   │   ├── item.py
│   │   └── claim.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── item_routes.py
│   │   └── claim_routes.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── README.md
└── USER_STORIES.md


### Architecture Explanation

- `main.py` initializes the Flask application using the factory pattern.  
- `extensions.py` initializes shared services like database and JWT.  
- `models/` defines the database schema.  
- `routes/` defines REST API endpoints.  
- `Dockerfile` defines container configuration.  
- `Jenkinsfile` defines CI/CD pipeline stages.  

This modular structure ensures clean separation of concerns, scalability, and maintainability.

---

## 5. Application Workflow

1. User registers an account.  
2. User logs in and receives a JWT access token.  
3. Authenticated user posts a lost or found item.  
4. Another user submits a claim for the item.  
5. Item owner reviews pending claims.  
6. Owner approves or rejects the claim.  
7. Item status updates accordingly.  

This workflow enforces ownership validation and prevents unauthorized claim approvals.

---

## 6. API Endpoints

### Authentication

- `POST /api/auth/register`
- `POST /api/auth/login`

### Items

- `GET /api/items`
- `POST /api/items` (Protected)

### Claims

- `POST /api/claims/<item_id>` (Protected)
- `PUT /api/claims/review/<claim_id>` (Owner Only)

### Health Check

- `GET /health`

All protected routes require:
Authorization: Bearer <JWT_TOKEN>


---

## 7. Running the Application

### Using Docker

Build image:

docker compose up --build

### Run Container

docker run -p 5001:5000 finderskeepers

### Access Health

http://localhost:5001/health

---

## 8. CI/CD Pipeline 

The CI/CD pipeline includes:

  - Clone repository
  - Build application
  - Create Docker image
  - Push image to DockerHub
  - Optional deployment to AWS EC2

This ensures automated image creation and deployment consistency.

---

## 9. Dockerhub Image

### Pull Image 

docker pull <your-dockerhub-username>/finderskeepers:latest

### Run Image

docker run -p 5001:5000 <your-dockerhub-username>/finderskeepers:latest

---

## 10. Security Considerations

1. Password hashing implemented
2. JWT-based stateless authentication
3. Authorization checks for ownership
4. Prevention of self-claiming
5. Duplicate claim prevention
6. Protected routes with token validation

---

## 11. Testing Strategy

The system was tested using:

  1. Functional endpoint testing
  2. Authentication validation tests
  3. Authorization validation tests
  4. Negative test cases
  5. Edge case testing
  6. Docker runtime validation

Testing was performed using curl commands and container log verification.

---


## 12. Future Enhancements

  1. Frontend UI integration
  2. Email notifications
  3. Admin dashboard
  4. Search and pagination
  5. Audit logging
  6. Activity monitoring
  7. Rate limiting and API throttling

---

## 14. Team Members : 

  1. 23N203 - Aakash Balaa
  2. 23N230 - Muralikarthik
  3. 23N232 - Nikileshh
  4. 23N240 - Rohish Raj

---

## 14. Conclusion

FindersKeepers demonstrates backend engineering best practices including:

  1. Secure REST API design
  2. Modular Flask architecture
  3. JWT authentication
  4. Role-based authorization
  5. Docker containerization
  6. CI/CD automation
  7. Cloud deployment readiness

The system is scalable, maintainable, and production-ready.

---
