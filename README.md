# installation


## build

```
docker build -t tag:version .
```

convert _tag_ and _version_ to any name, like this.

```
docker build -t captbot:0.0.1 .
```


## start 

```
docker run -d -v $(PWD)/script:/usr/src/app/script --name name tag:version --token token --command command --camid num
```
