# Fast API


## Docker deployment of Fast API

Build the container image in the root dir
```
docker build -t fastapi .
```

Run Fast api instance
```
docker run -d --network=host --name fast_api_server -p 80:80 fastapi 
```
Use -d to run in detached mode

To stop instance
```
docker stop fast_api_server
```


## Using fast API server

To run the instance now simple use
```
docker start fast_api_server
```

To stop instance
```
docker stop fast_api_server
```

### See API Docs at: http://0.0.0.0/docs


## Normal run

```
/Documents/cek-cs-cookbook/fastapi/app$ uvicorn main:app --reload
```