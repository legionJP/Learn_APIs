
# REST APIs
~~~
- Rest is Architectural style for designing the API for the Project. easy to implement and develop
- Provide easy way to communicate to the servera and access the the data 
-
~~~

# RESTful APIs

``` diff
- Api is Only Restful if it complies with 

+ 1. Must Have Client Server Architecture
+ 2. It is always Stateless and should be cacheable
+ 3. It should be layerd 
+ 4.it should have Uniform interface 
+ 5. (Optioonal) code on demand 

```

#### 1. Client Server Model: 
- There should be serevr who serves the resources and client who consumes the resources

#### 2. Stateless
- It doesn't contain any state of the client who is making the call , So can't identify who is making the request and what was the previously requested data without the user information 
- and the status is stored on the client machine not on the server and this influences include in the endpoint of the api or url path 

#### 3. Cacheable 

- This means the response can be saved by a web browser or server or an system , this help to reduce the server load by using the api result from the cache. 

### 4. Layerd

- This means that the entire system architecture can be be split or decoupled into multiple layers and should be able to add or remove the multiple layer at any time.


Layers: 1. client |----firewall---| Load Balancer|---- Web Server---|--Database Server | 


### 5. Uniform Interface : 

- the system shoulf offer a uniform communication system to access the resources , 
Example:  1.Unique URLs for each resources 

- Uinified way (Procedures) to modify or proceed further with a resources from the API result or represntation in a standard XML or Json format


### 6. Code on Demand 

- Means apiu may deliver the some business logic that the API may deliver some business logic ort code that the client can run further improve the result 


example: 
<script
src = 'https://../'>

</script>


# Resources : 

- It is core part of every REST API
- a mobile app can use for user and admin to support this app will use the diff api 
- Resource Type will be differnet for each : 
1. https://myrestro/orders/16 ---> resource type---> order object
2. https://myrestro/orders/16/cutomer ----> resource type is ----> Customer object 
3. to browse the menu api will use another api and resource  type will menu-object 

API4. https//myrestor/menu-items?Category=appetizers 
- here resrouce type is same menu-item object 


## Statelessness Of REST API

- The server can't reconginize clients automatically api call must include the more info about the user 
- bcz it doesn't store the previous query/request  or data 
