# Circuit Simulator

### Build Docker Container
```
docker build -t vbm-project .
```

### Run Docker Container
```
docker run -v $PWD/src:/app/src -v $PWD/media:/app/media --rm vbm-project manim -p -ql FILE_PATH CLASS_NAME
```
