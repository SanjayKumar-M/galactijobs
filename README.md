# Galactijobs API Documentation

Galactijobs is a powerful job portal application built using Django. This API documentation will guide you through the various endpoints available for users and companies to interact with the platform.


- [Authentication](#authentication)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Company Registration](#company-registration)
  - [Company Login](#company-login)
- [User Profile](#user-profile)
  - [Get User Profile](#get-user-profile)
  - [Update User Profile](#update-user-profile)
- [Job Posting](#job-posting)
  - [Create Job Post](#create-job-post)
  - [Get Job Post List](#get-job-post-list)
  - [Get Job Details](#get-job-details)
- [Job Application](#job-application)
  - [Apply for a Job](#apply-for-a-job)
  - [Get Applied Jobs List](#get-applied-jobs-list)
- [Company Profile](#company-profile)
  - [Get Company Profile](#get-company-profile)
  - [Update Company Profile](#update-company-profile)
  - [Get Applicants List](#get-applicants-list)

## Authentication

### User Registration

- **Endpoint**: /signup/
- **Method**: POST

**Request Body**:
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "password123"
}
```
### User Login

- **Endpoint**: `/login/`
- **Method**: POST

**Request Body**:
```json
{
  "username": "johndoe",
  "password": "password123"
}
```

### Company Registration

- **Endpoint**: `/company/`
- **Method**: POST

**Request Body**:
```json
{
  "company_name": "Acme Inc.",
  "email": "hr@acme.com",
  "password": "company123"
}
```

### Company Login

- **Endpoint**: `/company/login/`
- **Method**: POST

**Request Body**:
```json
{
  "email": "hr@acme.com",
  "password": "company123"
}
```

### User Profile

#### Get User Profile

- **Endpoint**: `/profile/int:pk/`
- **Method**: GET

**Response**:
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "johndoe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "1234567890",
  "resume": "https://example.com/resume.pdf"
}
```
### Update User Profile

- **Endpoint**: `/updateprofile/int:pk/`
- **Method**: PUT

**Request Body**:
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "phone_number": "1234567890",
  "resume": "https://example.com/resume.pdf"
}
```

### Job Posting

#### Create Job Post

- **Endpoint**: `/jobpost/`
- **Method**: POST

**Request Body**:
```json
{
  "job_title": "Software Engineer",
  "job_description": "We are looking for a talented software engineer to join our team.",
  "job_location": "San Francisco, CA",
  "job_type": "Full-time",
  "salary_range": "80,000 - 120,000 USD",
  "company": 1
}
```

### Get Job Post List

- **Endpoint**: `/jobpostlist/`
- **Method**: GET

### Get Job Details

- **Endpoint**: `/jobdetailpost/int:pk`
- **Method**: GET

### Job Application

#### Apply for a Job

- **Endpoint**: `/apply/int:pk`
- **Method**: POST

**Request Body**:
```json
{
  "cover_letter": "I am excited to apply for this position and would be a great fit for the team.",
  "resume": "https://example.com/resume.pdf"
}
```
