# LLMFlaskWebAppDockerDeployment
NLP Sentiment Analysis Flask App with Docker Deployment
This project is a Dockerized Flask web application that performs sentiment analysis using the DistilBERT NLP model. 
It demonstrates the end-to-end process of deploying a machine learning model in a web application with Docker.

Features:
Sentiment Analysis: Uses DistilBERT for analyzing the sentiment of input text.
Web Interface: Simple form for user input and result display.
Dockerized Deployment: Containerized with Docker for easy deployment and scalability.

Getting Started:
1- Clone the Repository:
git clone https://github.com/yourusername/repository.git

2- Build the Docker Image:
docker build -t flask_simple_app .

3- Run the Docker Container:
docker run -d -p 5000:5000 --name flask_app flask_simple_app

4- Access the App:
Open your browser and go to http://localhost:5000.
Technologies:
Flask for web framework
DistilBERT for NLP
Docker for containerization
