# FindersKeepers API

This is the Final Project for the Course :-
" 23ZF03 : Developing And Deploying Scalable Applications "

## Tech Stack
- Flask
- PostgreSQL
- JWT Authentication
- Docker
- Jenkins / GitHub Actions

## Features
- User Authentication (JWT-based)
- Item Management (Lost & Found system)
- Claim System
- Role-Based Access Control (RBAC)
  - USER role
  - ADMIN role
  - Admin-protected endpoints

## How to Run

### Using Docker

docker compose up --build

### API Endpoints
POST /api/auth/register
POST /api/auth/login
GET /api/items
POST /api/items
POST /api/claims/<id>

## CI/CD Pipeline
- Clone
- Build
- Docker image creation
- Push to DockerHub

