# Student Management System — AWS Serverless

A full-stack serverless CRUD web application built with AWS Lambda, API Gateway, and DynamoDB.

## Architecture
Client (HTML/JS) → API Gateway → Lambda (Python) → DynamoDB

## AWS Services Used
- **AWS Lambda** — Serverless compute (Python 3.12)
- **AWS API Gateway** — REST API with 4 HTTP methods
- **AWS DynamoDB** — NoSQL database for student records

## Features
- Create a student record (POST)
- Read all student records (GET)
- Update a student record (PUT)
- Delete a student record (DELETE)

## Setup Instructions
1. Create DynamoDB table `Students` with PK `id` (String) and SK `timestamp` (String)
2. Create Lambda function `StudentsFunction` with the code in `/lambda`
3. Attach `AmazonDynamoDBFullAccess` policy to the Lambda IAM role
4. Create API Gateway REST API, resource `/student`, add all 4 methods
5. Enable CORS and deploy to stage `prod`
6. Update `API_URL` in `frontend/index.html` with your invoke URL
7. Open `index.html` in a browser to test
