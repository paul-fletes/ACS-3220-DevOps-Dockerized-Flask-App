# To-Do Flask

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Website](https://img.shields.io/website?url=http%3A%2F%2Flocalhost%3A5050)

## 📚 Table of Contents

1. Build and Run with Docker Compose
2. Access the App
3. Command Reference

---

## 🚀 Build and Run

Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

Then, from the root of the project:

```bash
docker-compose up --build
```

This will build the Flask app and start both MongoDB and Flask containers.

---

## 🌐 Access the App

Once everything is up and running, open your browser and go to:

```
http://localhost:5050
```

---

## ⚙️ Command Reference

### Build the Image Manually (Optional)

```bash
docker build -t flask-image .
```

### Run Without Compose (Optional)

```bash
docker run -p 5050:5000 --rm --name flask-container flask-image
```
