# Champion Picker - Docker Hub Deployment

This document explains how to run the Champion Picker application using Docker images from Docker Hub.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Quick Start

1. Create a new directory for the application:
   ```
   mkdir champion-picker
   cd champion-picker
   ```

2. Create a `docker-compose.yml` file with the following content:
   ```yaml
   version: '3.8'

   services:
     # Backend API service
     api:
       image: poweraade/lol-champion-picker:api
       ports:
         - "5001:5000"
       container_name: champion-picker-api
       restart: unless-stopped
       networks:
         - app-network

     # Frontend service
     frontend:
       image: poweraade/lol-champion-picker:frontend
       ports:
         - "80:80"
       container_name: champion-picker-frontend
       restart: unless-stopped
       depends_on:
         - api
       networks:
         - app-network

   # Define a network for the services
   networks:
     app-network:
       driver: bridge
   ```

3. Start the application:
   ```
   docker compose up -d
   ```

4. Access the application:
   - Frontend: http://localhost:80
   - Backend API: http://localhost:5001/randomize

5. Stop the application:
   ```
   docker compose down
   ```

## Troubleshooting

- If port 5001 is already in use, you can change it in the docker-compose.yml file.
- If port 80 is already in use, you can change it in the docker-compose.yml file.

## About Champion Picker

Champion Picker is a League of Legends champion randomizer application with a React frontend and Flask backend. 