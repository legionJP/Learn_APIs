# Examples of APIs calls

## GET 

``` diff
 A GET call doesn’t need a payload. However, GET calls can be accompanied by query string parameters and their values to filter the API output.

```

## POST
/api/menu-items
/api/orders

``` diff
Here’s a sample JSON payload for the /api/menu-items endpoint to create a new resource:
{
  "title":"Beef Steak",
  "price": 5.50,
  "category":"main",
}

```
## PUT

``` diff
 Here's a sample JSON payload for this endpoint /api/menu-items/1 to completely replace it. Note that you need to supply all data for a PUT request.
```

## PATCH

``` diff
Here’s a sample JSON payload for this endpoint /api/menu-items/1 to partially update this resource
{
   "price": 3.00
}

```
## DELETE

``` diff
When the DELETE call is sent to a collection endpoint, like /api/menu-items the API developer should delete the entire collection. When it is sent to a particular resource, like this, /api/menu-items/1, then the API developer should delete only that resource. 

```


| HTTP Method | Sample Endpoints                                | Query String / Payload                                                                                                                                                    |
|-------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **GET**     | /api/menu-items                                  | A GET call doesn’t need a payload. However, GET calls can be accompanied by query string parameters and their values to filter the API output.                             |
|             | /api/menu-items/1                                |                                                                                                                                                                           |
|             | /api/menu-items?category=appetizers              |                                                                                                                                                                           |
|             | /api/menu-items?perpage=3&page=2                 |                                                                                                                                                                           |
| **POST**    | /api/menu-items                                  | sample                                                                                                                                                                    |
|             |                                                  |     json payload                                                                                                                                                          |
|             |                                                  | {                                                                                                                                                                         |
|             | /api/orders                                      |   "title":"Beef Steak",                                                                                                                                                   |
|             |                                                  |   "price": 5.50,                                                                                                                                                          |
|             |                                                  |   "category":"main",                                                                                                                                                      |
|             |                                                  | }                                                                                                                                                                         |
| **PUT**     | /api/menu-items/1                                | ```json                                                                                                                                                                   |
|             |                                                  | {                                                                                                                                                                         |
|             | /api/orders/1                                    |   "title":"Chicken Steak",                                                                                                                                                |
|             |                                                  |   "price": 2.50,                                                                                                                                                          |
|             |                                                  |   "category":"main",                                                                                                                                                      |
|             |                                                  | }                                                                                                                                                                         |
| **PATCH**   | /api/menu-items/1                                | ```json                                                                                                                                                                   |
|             |                                                  | {                                                                                                                                                                         |
|             | /api/orders/1                                    |   "price": 3.00                                                                                                                                                           |
|             |                                                  | }                                                                                                                                                                         |
| **DELETE**  | /api/menu-items                                  | When the DELETE call is sent to a collection endpoint, like /api/menu-items, the API developer should delete the entire collection.                                       |
|             | /api/menu-items/1                                | When it is sent to a particular resource, like /api/menu-items/1, then the API developer should delete only that resource.                                                |
|             | /api/orders                                      |                                                                                                                                                                           |
|             | /api/orders/1                                    |                                                                                                                                                                           |



## Status Codes

Sending appropriate status codes with every API response is essential. Every status code has meaning, so you should choose the most appropriate one based on the situation. Here’s a list of the status code ranges and their purposes.

| Status Code Range | Purpose                                                                                                                                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 100-199           | This range is mainly used to pass on some information. For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. In such a case, the API developer can set it to keep returning 102 – Processing until the result is ready. This way, the client understands that the result isn’t ready and should be checked again.  |
| 200-299           | These are the success codes. If the client requests something and the API acts successfully, it should deliver the output with one of these status codes. For example, for a PUT, PATCH, or DELETE call, you can return 200 – Successful if the operation was successful. For a successful POST call, you can set it to return a 201 – Created status code when the resource has been created successfully. |
| 300-399           | These are the redirection codes. Suppose as an API developer, you changed the API endpoint from /api/items to /api/menu-items. If the client makes an API call to /api/items, then you can redirect the client to this new endpoint /api/menu-items with a 301 – Permanently moved status code so that the client can make new calls to that endpoint next time.                           |
| 400-499           | 4xx status codes are used in the following situations: if the client requests something that does not exist, sends an invalid payload with insufficient data, or wants to perform an action that the client is not authorized for. For the above scenarios, the appropriate status codes will be: - 404 - Not Found if the client requests something that doesn’t exist, - 400 - Bad Request if a client sends an invalid payload with insufficient data, - 401 - Unauthorized, - 403 - Forbidden if the client tries to perform an action it's not authorized for.|
| 500-599           | These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, and the API developer doesn't write code to deal with those errors. For example, a client requests a non-existing resource, and the API developer tries to display that resource without adequately checking if that resource exists in the database. Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. You, as an API developer, should always avoid 5xx errors.                                                                                                                                                                |


# Response types


 While making an API call, the client can specify its desired response format with the Accept HTTP header. And that header should be considered to deliver the result in that format using the render classes. Here’s a list of HTTP headers for different response types.  

| Response Type | Request Header                   |
|---------------|----------------------------------|
| HTML          | Accept: text/html                |
| JSON and JSONP| Accept: application/json         |
| XML           | Accept: application/xml          |
|               | Accept: text/xml                 |
| YAML          | Accept: application/yaml         |
|               | Accept: application/x-yaml       |
|               | Accept: text/yaml                |


































