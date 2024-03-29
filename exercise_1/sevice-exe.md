# Service Exercise

In this exercise you will create a kubernetes service.  
You will:  
- [Create a simple python web application](#Create-a-simple-python-web-application)
- [Dockerize your server application](#Dockerize-your-server-application)
- [Deploy your app to your local minikube kubernetes cluster](#Deploy-your-app-to-your-local-minikube-kubernetes-cluster)



## Create a simple python web application

Create a simple python web application:  
- Use Flask
- Your application should serve a single web page.
- The single web page should identify the replying server hostnme or IP address 
- Example:  
```
Greetings !!!
This is your server answering from pod:
 server-deployment-1-779cc696cf-54p77
```

- Make sure your code is saved in github

#Answer : view.py file

## Dockerize your server application

- Create a Dockerfile (also saved in github)
- You can store it in the same directory as the python file(s)
- build and tag your image
- Try to use your images locally
- Upload your images to dockerhub  
(you need a dockerhub account for that)

##Answer : aviadyarkoni/exercise:myflask

## Deploy your app to your local minikube kubernetes cluster

- Create the necessary yaml files
- Create a **deploy** directory in your project to store these files
- Deployment files should be part of your github project
- Deploy your code using **kubectl** commands

## kubectl apply -f  flask-deployment.yaml 

- Make sure deployment works even if image is locally deleted, so the image is downloaded from the registry


