# 🛍️ Puddle — Online Marketplace

**Puddle** is a full-stack online marketplace web application built using **Django**, **SQLite**, **HTML/CSS**, and **Docker**, designed to help users list and browse products. The application is containerized and deployed using **AWS ECS** and **Elastic Load Balancing (ELB)**.

---

## 📦 Tech Stack

-  **Backend**: Django (Python)
-  **Database**: SQLite (for development)
-  **Frontend**: HTML, CSS
-  **Containerization**: Docker
-  **Cloud Deployment**: AWS ECR, ECS, ELB

---


## 🚀 Features

- 🏠 Home page to browse all products
- 🔍 Search and filter products by category
- 📬 Inbox for messaging sellers
- 🛠️ Dashboard to manage listed items
- 🐳 Docker containerization for environment portability
- ☁️ Fully deployed on AWS using scalable ECS architecture

---

## 🧑‍💻 Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/puddle.git
   cd puddle
   ```
2. **Build the Docker image**
    ```bash
    docker build -t onlinemarketplace .
    ```
3. **Run the container locally**
    ```bash
    docker run -d -p 8000:8000 onlinemarketplace
    ```
4. **Visit: http://localhost:8000**

---

## ☁️ AWS Deployment Steps

**Step 1: Configure AWS CLI**
```bash
aws configure
```
 Provide your Access Key, Secret, Region, and Output format.

**Step 2: Push Image to Amazon ECR**

1. Create an ECR Repository in AWS Console.
![alt text](<Screenshot 2025-06-23 161726.png>)

2. Copy the push commands from ECR, then run:

    ```bash
    # Example docker push commands 
    docker tag onlinemarketplace 8979399146726.dkr.ecr.us-east-1.amazonaws.com/puddle

    aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 897729146726.dkr.ecr.us-east-1.amazonaws.com

    docker push 897729146726.dkr.ecr.us-east-1.amazonaws.com/puddle
    ```
    ![alt text](<Screenshot 2025-06-23 162517.png>)

**Step 3: Create ECS Cluster and Service**
1. Create a new ECS cluster using the AWS Console (EC2 or Fargate).

2. Create a Task Definition

   -  Use the pushed ECR image
   ![alt text](<Screenshot 2025-06-23 144548.png>)

   - Define resource limits and networking mode

3. Create a Service

   - Attach the task

   - Configure:

        - Security Group (open port 80/443)

        - Load Balancer (ELB + listener)

        - Health checks
        ![alt text](<Screenshot 2025-06-23 161654.png>)
        ![alt text](<Screenshot 2025-06-23 161632.png>)

        - Auto Scaling

        - IAM Roles / Policies

        - Rollback settings
    ![alt text](<Screenshot 2025-06-23 144530.png>)

4. Deploy the Service and verify the application.

## 🌐 Access the App
 - Once deployed, visit the DNS name of the Load Balancer (ELB) to view the live application.
 ![alt text](<Screenshot 2025-06-23 161520.png>)

## 📋 Future Improvements
- Enable email/SMS notifications
- Integrate AI-based recommendations