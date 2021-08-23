# Flask Task App 

With this application, you will be able to find the distance between a given address and the MKAD.
You will also know if the address is inside or not the MKAD.

## Heroku Link

``` https://flask-app-geocode.herokuapp.com/```

## Docker Project Setup
---

Build Image

``` docker build --tag flask-app .```

Run Container

``` docker run --publish 5000:5000 flask-app ```  

Access in your browser

``` http://localhost:5000/``` 


## Local Project Setup  
---

### Install Packages  
  
``` pip install -r requirements.txt```
  
### Running
  
```python webserver.py```

### Run Unit Tests

```python test.py```

