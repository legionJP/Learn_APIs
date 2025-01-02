
REST APIs Uniform Resource Identifier or URI is one of the first things that users will notice when a page loads. 
It is also called an endpoint or URL path. 

A suitable API endpoint is forward slash orders spelled with a lowercase o and 
not orders spelled with an uppercase O.

https://little.web/orders ---- 
https://little.web/Orders ---- Wrong

 your API endpoint should always use 
 1. lowercase letters 
 2. and hyphens 
 to separate multiple words. 

 Using underscores or snake case, title case or camel case, two separate words is not optimal
because it makes the names difficult to read and understand


### Exception to camel case

There is an exception to the camel case rule though 
if you're API accepts a variable, for example,
 a userId or orderId you should 
always represent them in camel case and wrap them in curly braces. 

// For specific Order
/orders/{orderId}/menu-items
/orders/customers/{CustomerId}/orders

- always try to use clear, concise, and meaningful words in your API names
 to make them easy to read right away

### Use of the forward Slashes

 Hierarchical Relationship

 Customer ----> Orders ---> Order items
 Library---> Books---> author

 Autor of a Book 
/library/books/{bookID}/author
All books by the author 
/library/authors/{authorName}/books

So the relationship b/w authors and books all are the denoted by the /


### 
naming convention is that your API should always use a noun to 
indicate the resources it is dealing with. An API that returns a collection of books 
or a book should use the nouns books or books and bookId wrapped in curly braces. 

/books | /books/{booksId} | /books/{bookId}/price

API endpoints with verbs like getAllBooks or getUser userId are examples of bad API names.
That's because the resources and a REST API endpoint should be always represented with 
a noun and never with a verb.
 #### bad API -- 
 /getAllBooks
 /getUser/{userId}

### Bad Api is it have the http requests as verb to indicate action in it

/users/{userID}/delete

/oreder/{orderId}/save  

### Delete Request 
Delete ---->  users/{userID}    
- send the delete Request to user using the userId 

### PUT, PATCH  Request to update the order

----> /orders/{orderId}

Endpoints that use standard CRUD operation names such as create, read, update or delete should be avoided for two reasons

1.  resources these endpoints represent should be nouns, and the appropriate HTTP requests like GET, POST, PUT, or DELETE should be used 
with those endpoints to perform the necessary manipulations
2. omething else to consider is whether file names should be used in APIs,
can Api will have file name extension in the API  --> orders/{orderId}.json  ---> Wrong 

3. To solve it you should always : accept the expected data fromat as a query string parameter
output in json format 
orders/{orderId}?format=json
orders/{orderId}?format=xml

4. To deliver a minified version or source version of a JavaScript file, you use API endpoints like
/assets/Js/jquery/3.6.0/min
Or
/assets/js/moment/2.29 .4/original

5. To filter the results 
- Always accept The Query String parameter

- Remember the API endpoint menu items, returns all 

/menu-items

- but to only get the appetizers, you should pass 
the category name to the endpoint as question mark 

/menu-items?category=appetizer.

- Differnt query String parameter
/menu-items?category=main 
/menu-items?category=desserts

6. If your API can accept multiple user ids,
then they should be separated using a comma, as demonstrated below.

/users/12,23,23/address   ------>Good (Uses a comma for separation)

###  you should never add a trailing slash to the end of the API endpoint.
- /orders/{orderId}/    --- Wrong
- /orders/{orderId}  ------- right


#
# SUMMARY 

1. Use lowercase URI formatting.
2. Indicate hierarchical relationships with a forward slash. 
3. Use nouns for resource names. Avoid file name extensions. 
4. Furthermore, use query parameters for data types and don't use a trailing slash.
5. always follow a consistent naming strategy and standard API naming conventions.