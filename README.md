# GalactiJobs API Documentation

GalactiJobs is a powerful job portal application built using Django. This API documentation will guide you through the various endpoints available for users and companies to interact with the platform.

## Table of Contents
- [Authentication](#authentication)
- [User Registration](#user-registration)
- [User Login](#user-login)
- [Company Registration](#company-registration)
- [Company Login](#company-login)
- [User Profile](#user-profile)
- [Job Posting](#job-posting)
- [Job Application](#job-application)
- [Company Profile](#company-profile)

## Authentication
### User Registration
**Endpoint:** `/signup/`  
**Method:** `POST`  
**Request Body:**
```json
{
  "username": "johndoe",
  "email": "johndoe@example.com",
  "password": "password123"
}
