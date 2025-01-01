# Example calls



# GET
```
- A GET call doesn’t need a payload. However, GET calls can be accompanied by query string parameters and their values to filter the API output.
```

#POST
/api/menu-items
/api/orders
```diff
Here’s a sample JSON payload for the /api/menu-items endpoint to create a new resource:
{
  "title":"Beef Steak",
  "price": 5.50,
  "category":"main",
}
```
# PUT
```
- Here's a sample JSON payload for this endpoint /api/menu-items/1 to completely replace it. Note that you need to supply all data for a PUT request.
```

# PATCH
```
Here’s a sample JSON payload for this endpoint /api/menu-items/1 to partially update this resource
{
   "price": 3.00
}
```
# DELETE
```
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






































