# Fast API POC

## Running with docker

```shell
docker compose up
```

## Running with python virtualenv

1. Create virtualenv

2. Install requirements

```shell
pip install -r requirements
```

3. Execute

```shell
uvicorn main:app --reload
```

## View documentation 

Open any of these urls in a browser

- http://0.0.0.0:8000/docs
- http://0.0.0.0:8000/redoc

## Testing with postman

You can import and use the collection file included in this repo: [FastAPI POC.postman_collection.json](./FastAPI POC.postman_collection.json)

