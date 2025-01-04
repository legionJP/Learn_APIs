#
## Consequences of a poorly designed API

```
Creating a high-quality API project can be challenging. Adherence to standards, implementing error handling, conducting security audits, and optimizing performance are crucial. Neglecting these steps can lead to inconsistencies, vulnerabilities, poor performance, and user dissatisfaction. Proper planning and execution are essential to ensure the effectiveness and reliability of your APIs.
```
# 1. Data breach   

| Reasons                                                              | Consequences                               |
|----------------------------------------------------------------------|--------------------------------------------|
| Poor security checks in the code                                     | Risk of data breach                        |
| No authentication or authorization checks                            | Exposure of sensitive data                 |
| Improper file permissions                                            | Potential data leakage                     |
| Not using SSL                                                        | Data interception by attackers             |
|                                                                      | Severe financial damage and erosion of trust |

# Fix: 
```
Add proper security checks in your code and create a solid authorization layer to prevent unauthorized access to your data. Always double-check these sensitive API endpoints before deploying them to production.   
```
# 2. Data corruption

| Reasons                                                               |      Consequences                           |
|-----------------------------------------------------------------------|---------------------------------------------|
| Poor security, no authentication or authorization checks              | Improper security checks and lack of a solid authorization layer can let any user with a valid authentication token access sensitive APIs and modify the data unexpectedly |
| Absence of data validation and sanitization of input data             | Creating resources without proper validation checks can create malformed data in the database |
|                                                                       | Severe data corruption and data loss beyond repair |

# Fix:
```
 Besides security checks and a solid authorization layer, an API developer must validate and sanitize user data before processing and saving it. 
 ```

# 3. Wastage of computing power and memory

| Reasons                                                                                | Implications                               |
|----------------------------------------------------------------------------------------|--------------------------------------------|
| Unoptimized code, improper business logic, lack of data validation                     | Inefficient code can consume excessive computing power and memory due to suboptimal algorithms and business logic |
| Unoptimized SQL queries or model relationships, lack of database indexes, no caching   | Inefficient SQL queries, lack of proper database indexing, and absence of caching can place a heavy load on the database server, causing system slowdowns |
|                                                                                        | Increased costs for API infrastructure due to inefficiencies |

# Fix 

```
To avoid this, always spend time optimizing the code and double-checking your database-related code before deploying your APIs to production
```

# 4. Wastage of bandwidth

| Reasons                                                                | Impact                                      |
|------------------------------------------------------------------------|---------------------------------------------|
| Absence of necessary caching header API code                           | Delivering unnecessary data multiple times without caching practices |
| Lack of caching policy on the reverse proxy and on the web server      | Increased bandwidth usage and additional costs |
| Lack of pagination and filtering                                       | Poor performance from API endpoints and additional resource usage by client applications to filter data |
|                                                                        | Increased monthly bills and slower client applications |

# Fix: 
```
To avoid this, always send proper caching headers with your API responses and implement filtering and pagination features so that the client application can request and receive only what they need.
```
# 5. Bad user experience

| Reasons | Consequences |
|---------|--------------|
| Not following the proper naming convention, not sending proper HTTP codes, not accepting Accept headers, absence of pagination, sorting, searching and filtering, and lack of proper error checking in code | This creates a poor user experience. Client application developers must perform additional processing of the API data, write extra code to generate the final output, and deal with a steeper learning curve to use your API, which could have been avoided if the API was designed following standard conventions and best practices. Not accepting the Accept headers means the API client does not receive the output in the required format, causing bad experiences because clients need more time and unnecessary code to process the data on their end. Also, sending incorrect HTTP status codes can cause unexpected errors in client applications, leading to a poor experience for the users who will use those applications. |

# Fix: 
```
To avoid this, always follow the proper naming convention and implement data filtering, searching, sorting, searching and pagination features for your API endpoints. Always keep proper error checking in the code and write tests so that it doesn’t create unexpected 5XX errors on the server side.

```

# 6. Breaking client applications

| Reasons | Consequences |
|---------|--------------|
| Not following the proper versioning system | If you don't maintain a proper versioning system for your API project, it can immediately break backward compatibility, and the client application can stop working instantaneously. The API can cause failure in the current client applications because your new API requires new request data and delivers new responses. So, their old code will not work anymore. They must refactor it and release a new version of their application as soon as possible. Such disruption can cause a bad reputation and financial damage for both the API and client application developers. |

# 7. Failure to manage the app

| Reasons | Consequences |
|---------|--------------|
| Keeping everything in one big Django app, adding all business logic in the views | Django apps can become big and unmanageable over time if you keep adding functionalities in one single app. Adding new features or debugging an error will be painful and take extra time and effort. Also, adding all business logic in the views file can lead to writing redundant code across multiple classes and function-based views. Failure to manage an app over time leads to bad coding, patching of errors without test coverage, and ultimately, poor performance from the APIs. |

# Fix:
```
Distribute the features and functionalities to multiple smaller Django apps in a decoupled way. Additionally, put some business logic in the models which can be reused by the other parts of your API project. 
```