# To-Do Flask

## Table of Content

1. Build the image
2. Run the Container
3. Access via Browser

## Command Reference

1. Build the Image

```bash
docker build -t flask-image .
```

2. Run the Container

```bash
docker run -p 5001:5000 --rm --name flask-container flask-image
```

3. Access via Browser http://localhost:5001
