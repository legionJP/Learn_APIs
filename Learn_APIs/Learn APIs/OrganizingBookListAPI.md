#
# Organizing the API Porject 

![alt text](Images_OrganizingBookListAPI/image.png)

```
Spliting the Big App into the multiple apps means Decoupling apps as much as possible and each app dealing with the particular set of relevent problems.

```
![alt text](Images_OrganizingBookListAPI/image-1.png)

### Disadvantes of the Adding the every feature in one App
![alt text](Images_OrganizingBookListAPI/image-2.png)

## Multiple Apps Management

1. Avoid the Global Environment use for project dependencies
2. Using the Global envs creates the Conflicts for packages and issues 
3. Always use the virtual environments to isolates the dependencies
  Example: Use Pipenv  
4. Use versioning Bcz the Upgrades might break the apps bcz result of the new api might be different 

![alt text](Images_OrganizingBookListAPI/image-3.png)

5. List your dependencies in the separate requirements.txt files 
![alt text](Images_OrganizingBookListAPI/image-4.png)
![alt text](Images_OrganizingBookListAPI/image-5.png)

- For the pipenv , no need the requirement file as it automatically creates and manages piplock file

![alt text](Images_OrganizingBookListAPI/image-6.png)

6. Must Have the Separate resource folder for the each APP:
    - to avoid conflicts 
    - Easily Manages 

7. Split the settings into multiple settings files
    - can use the Django Split Settings 
8. Plcae the Business Logic in models instead of views

    - Manages and Organize code in one place
    - Advantages  
    ![alt text](Images_OrganizingBookListAPI/image-7.png)


# Summary 
![alt text](Images_OrganizingBookListAPI/image-8.png)
![alt text](Images_OrganizingBookListAPI/image-9.png)
