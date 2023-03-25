# Fast API POC

## Run with docker

```shell
docker compose up
```

## Run with python virtualenv

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

## Test with postman

you import the collection file includen in this repo: [FastAPI POC.postman_collection.json](./FastAPI POC.postman_collection.json)

