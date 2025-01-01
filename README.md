# Learn_APIs

## What is API
``` diff
- API (Application Programming Interface) is gateway to the backedn data.
- It allows different services to exchange informations and access functionality 


```

## Use of the APIs in the Real World

```
# consider  when designing the API who is your enduser and who is going to access the api
```


## HTTP:
~~~ diff
- HTTP : Hyper text transfer Protocol
 -Transmission
it requires the: Client <----Request----> Server


~~~
### HTTPS
~~~
- It is secured version of HTTP

+ in this the data is encrypted from the client  computer and then it transfer to server and then the server decrypt data. also the server computer encrypt the response. The browser decrypt it and shows the data. 
~~~

### HTTP methods:

```
These are also called the HTTP verbs. 
There is 5 common Types :

1. GET --------> Retrieve the resources , if not found returns 404
2. POST ------->  send data and Create the resource , request body contains the payload
4. PUT --------> Update the whole resource, (it deals with the single  resource )
5. Patch ------> Partially Update the resource, (update some parts of a resource)
6. DELETE ----->  Delete the resource
```
### HTTP Request:
~~~
The http request contains below 

1. Version Type
2. URL
3. Method
4. Request Headers : Extra information for the server that how to present the content 
-Examples: Cookies , User agents and referrersk
5. Body(optional) : Data is passed to server  in the Http body  in raw json or form URL encoded data

~~~

### HTTP Response:

~~~diff
-Http Response is information that helps the browser to display the content in respone body 
+ It contians the Below things:

!1.Requested resources 
!2. Content lenght 
!3. Content Type
!4. Headers
!5. Etags
!6. Time last modified (content)
!7. HTTP STATUS codes

~~~
### HTTP STATUS CODE:

~~~ diff
These are the Messages Provided to the borwser about the status of the resources
- Examples

! 100-199 ----> Inforamtional Code
+ 200 -299 ----> Successful response
! 300-399 ------> Redirection Messages
- 400-499 ------> Client Error  
(bad api request)
- 500-500 ------> Serevr Error codes
(config error)

! Different  status code Meaning for the Different Request

+ 200 (GET)
Content found

+ 200(PUT)
Updated and transmitted successfully

+ 200 (DELETE)
Deleted Successfully

~~~

### HTTP vs HTTPS


# REST APIs

# Building the API with the Django Rest Framework(DRF)


# Serializers
# Deserializers
