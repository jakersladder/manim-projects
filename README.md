# Circuit Simulator

### Build Docker Container
```
docker build -t circuit-simulator .
```

### Run Docker Container
```
docker run -v $PWD/src:/app/src -v $PWD/media:/app/media --rm circuit-simulator
```
