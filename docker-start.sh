#!/bin/bash

echo "Building and starting Champion Picker containers..."
docker compose up -d --build

echo ""
echo "Containers started successfully!"
echo "Frontend available at: http://localhost:80"
echo "Backend API available at: http://localhost:5001/randomize"
echo ""
echo "To view logs, run: docker compose logs -f"
echo "To stop containers, run: docker compose down" 