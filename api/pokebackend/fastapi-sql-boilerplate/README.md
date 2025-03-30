# FastAPI Boilerplate with SQLite

## Project Description

This repository provides a comprehensive FastAPI boilerplate for building web applications with SQLite as the database. It includes:

* FastAPI framework for high-performance API development
* SQLite database for lightweight and portable data storage
* Basic project structure for seamless organization
* Dependencies management with requirements.txt
* Relationships between tables in SQL using FastAPI

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ridwanspace/fastapi-sql-boilerplate.git
```

2. Install dependencies:

```bash
cd fastapi-sql-boilerplate
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```


## Docker 

**To manually create Image and Uploaded to Cloud Run for Deployment**

### Docker (Create New Image)

1. Docker Build
``` bash
docker build -t name-your-app .
```

2. Run Docker
```bash
docker run -p 8080:8080 name-your-app
```

3. Access your App
Go to [http://localhost:8080/](http://localhost:8080/)

### Docker (Push Image to Docker Hub)
1. Create a Docker Hub Account: If you don't have one, sign up at Docker Hub.

2. Login to Docker Hub: 
```bash
docker login
```

3. Tag your Image: 
```bash
docker tag name-your-app username/name-your-app:name-your-tag
```

4. Push your Image to Docker Hub: 
```bash
docker push username/name-your-up:name-your-tag
```

### Docker (Update and Push Image)
1. Update your file

2. Login to Docker Hub: 
```bash
docker login
```

3. Check images
```bash
docker images
```

4. Rebuild docker image
```bash
docker build -t username/name-your-app:name-your-tag .
```

5. Run the Updated Docker Image
```bash
docker run -d -p 8080:8080 username/name-your-app:name-your-tag
```

6. Push the Updated Image to Docker Hub
```bash
docker push username/name-your-app:name-your-tag
```

### Remove Docker Images
1. Remove dangling images (images without a tag)
```bash
docker image prune
```

2. Remove specific images
```bash
docker rmi <image-id>
```

### Docker (Stop Running Container)
```bash
docker stop $(docker ps -a -q)
```

## Usage

Access the API documentation:

Open your browser and visit: http://127.0.0.1:8000/docs
Interact with endpoints:

Use tools like [Postman](https://www.postman.com/), [Thunder Client (VS Code Extension)](https://www.thunderclient.com/) or curl to send requests to the API endpoints.

## Additional Notes

* Customize the project structure and code as needed.
* Explore FastAPI's features for building robust APIs.
* Consider using Alembic for database migrations.
* Implement more relationships between tables.
* Implement authentication and authorization mechanisms for security.

