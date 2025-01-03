
# 
# Security and Authentication for REST  APIs

### How to Keep API safe and Secure 

# 1. SSL (Secure Socket Layer)
```
1. Encryption: SSL encrypts the data exchanged between the client and the API server., SO it can't be read or manipulated.

2. Server Authentication : SSL encrypts the data exchanged between the client and the API server.

3. Data Integrity : SSL ensures that the data sent and received is not altered during transit
```
![alt text](<Images/Screenshot 2025-01-04 035927.png>)

# 2. Signed URLs
- Signed URLs give someone limited access to a specific resource for a brief period of time. 

![alt text](<Images/Screenshot 2025-01-04 035945.png>)

![alt text](<Images/Screenshot 2025-01-04 040018.png>)

```
A signed URL contains authentication information in its query string. This information is typically generated using a private key (Signature) associated with a service or third Parties account. 
```

# 3. HMAC (Hash-based Message Authentication Code.)
```
It is used  to verify both the data integrity and the authenticity of a message.
Hash Function: + Secret Key ====> Message Integrity and Message Authentication

- Hash Function: HMAC uses a cryptographic hash function (like SHA-256) along with a secret key.

- Secret Key: A secret key is shared between the sender and the receiver. This key is combined with the message data to create the HMAC.

- The receiver then uses the same hash function and the shared secret key to generate their own HMAC from the   received message. If the HMACs match, means the message has not been altered.

- Message Authentication: HMAC is generated using a secret key known only to the sender and receiver, it verifies that the message truly came from the sender.
```
![alt text](<Images/Screenshot 2025-01-04 040115.png>)

# 4. Token Based Authentication 
![alt text](<Images/Screenshot 2025-01-04 040132.png>)

![alt text](<Images/Screenshot 2025-01-04 040151.png>)

![alt text](<Images/Screenshot 2025-01-04 040223.png>)

```
Working of Token Based Authnatication

1. User Login 
2. Token Generation : 
The server verifies the credentials and, if valid, generates a token. it often contains encode info about user and permission
3. Token Sotrage: Sent back to client and Stored on client side in local storage or a cookie
4. Resource Access: When needs to access the protected resource , the client will send the token with Http request headers Authorization: Bearer <token>
5. Token Validation: : Check , Extract , Match , grant access if matched 
6. Token Expiry
```
# Types of Tokens:
~~~
JWT (JSON Web Tokens): A common token format that includes a header, payload, and signature. It's widely used in web applications.

OAuth Tokens: Used in OAuth 2.0 authorization framework to grant access to resources without sharing credentials.

API Keys: Simple tokens used to identify and authenticate an application making a request.
~~~

# 5.  CORS (Cross- Origin Resource Sharing)
![alt text](<Images/Screenshot 2025-01-04 040349.png>)
~~~
It is a security feature implemented in web browsers to allow or restrict web pages from making requests to other domains.

- enable interaction securely 
when a web application hosted on one domain needs to access resources or APIs hosted on another domain
1. Origin and Request : from origin the browser sends an HTTP request called a "preflight" request to the server
2. Server Response: The server responds with the appropriate CORS headers, whether request allowed or not
3. Access Control: If the CORS headers indicate permission, the browser sends the actual request. Otherwise, the request is blocked.

~~~

# 6. HTTP  Codes 

![alt text](<Images/Screenshot 2025-01-04 040257.png>)
![alt text](<Images/Screenshot 2025-01-04 040309.png>)

# 7. Firewall Application On Server 
```
Using the firewall we can use Authentication and Authorization: 
Verifies the identity of clients and ensures they have the necessary permissions to access specific resources within the API.

```