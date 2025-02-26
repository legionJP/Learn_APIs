# Exercise: User account management
In this exercise, use authentication and validation mechanisms inside DRF. You need to do this activity using VS code and Insomnia on your computer. 

# Objectives

- Add form validators to form data        

- Perform token and session authentication while using a DRF form      

- Use the Djoser and authtoken packages for default routes

- Use the Django admin panel for creating new users and tokens

# Introduction 
The Little Lemon website has grown in popularity since it was launched. While there are many benefits to the website, fake reviews are a cause for concern. The owners understand the need for better security for their review system. 

You are tasked with adding some measures to prevent the misuse of the review system on the Little Lemon website.

# Instructions 
This lab will require you to modify the following files:  

```markdown
views.py 

serializers.py 

settings.py

admin.py
```
You must start the development server on the local host and go to the URL to confirm the desired view on the webpage. 

When required, Open the Terminal by selecting New Terminal under Terminal on your VSCode.

For your convenience, the Django project called LittleLemon and Django app called LittleLemonDRF have already been created for you. Download the zip file and save the unzipped content inside a project directory on your local machine. Open the project folder inside VS Code and navigate to the directory containing 'Pipfile' inside your command line. If you are unsure how to set up a Django project reference the optional reading about 
Creating a Django project
 which includes all the necessary steps and code snippets.

 Follow the instructions below and ensure you check the output at every step.

 Note: The settings for project level and app level urls.py file have already been updated. 

Initial instructions
Now run a command on Terminal to initialize the pipenv environment such as:

pipenv shell

Open the Pipfile created and ensure the dependencies for the project are already added. 

Run a command on the Terminal to install the dependencies such as:

pipenv install

Note: You should be able to see the prompt inside the Terminal now has a suffix of round brackets. Follow the steps below to complete the exercise. 

Step 1:  
Open the models.py file and create a class called Rating inside it and pass models.Model to it as a parameter.

Create the two attributes in the model and assign the respective form fields to them.

Additionally, pass the following arguments to those form fields:

Attribute 

Form field type 

Arguments 

menuitem_id 

SmallIntegerField


rating 

SmallIntegerField


Now add a third attribute labelled user and assign it the value of models.ForeignKey() with the following arguments passed to it:

User

on_delete=models.CASCADE

1
user = models.ForeignKey(User, on_delete=models.CASCADE)
Step 2:  
Create a file called serializers.py inside the app level LittleLemonDRF directory. Add the code below inside the file: 


from rest_framework import serializers 
from .models import Rating 
from rest_framework.validators import UniqueTogetherValidator 
from django.contrib.auth.models import User 
 
 
class RatingSerializer (serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField( 
    queryset=User.objects.all(), 

 Note: The import statements required have already been added. Additionally, the class RatingSerializer is already declared and updated with the relevant code. Take note of the user variable created and the contents of the code because you will be using it. 

Step 3:
Create another class called Meta inside RatingSerializer and add the following code inside the class:

Assign the Rating model to a variable called model

Create a fields variable and assign a list to it that contains the following three string elements: user, menuitem_id and rating

Note: The order of list elements must be maintained.

Create a variable called validators and assign to it a list that contains:

A UniqueTogetherValidator class that has the following arguments passed to it:

a queryset variable that is assigned the value of Rating.objects.all()

a fields variable that contains three list elements that are strings like: user, menuitem_id and rating     

Create a variable called extra_kwargs that has a dictionary assigned to it containing one item that has the following key-value  pair:

Key: rating      

Value: A dictionary containing the following two items:       

max_value as key and 5 as value

min_value as key and 0 as value

Note: Make sure you add a comma after the inner dictionary.

Step 4:
Open the settings.py file inside the project-level directory LittleLemon. 

Locate the code in the screenshot and follow the instructions provided below to update the code:

Add code to assign default renderer classes in the REST_FRAMEWORK section in the settings.py file.
You will be adding three configurations inside the REST_FRAMEWORK this time:

Create a string called DEFAULT_AUTHENTICATION_CLASSES and assign a list to it containing the following items:

rest_framework.authentication.TokenAuthentication

rest_framework.authentication.SessionAuthentication

Note: Make sure you add a comma after every list item. 

Step 5:
Now look for the configuration settings for INSTALLED_APPS namespace inside the settings.py file and update the list with the following string elements:

rest_framework.authtoken

djoser

Note: Make sure you add a comma after every new element added to the list. 

Step 6:
Open the views.py file.

Note: All the import statements required are already added. Additionally, the class RatingsView is already declared and updated with the relevant code. 

Create a function inside the class RatingsView called get_permissions() and pass a single argument inside it called self. 

 Inside the get_permissions() function, add the following code:

12345
if(self.request.method=='GET'):
    return []
        
return [IsAuthenticated()]

Make sure you save all the files that have been updated. 

Step 7:  
Run a command to create a superuser in Django.

Tip: The command to create a superuser in Django is:  python3 manage.py createsuperuser

 Enter the following details inside the prompts that appear:

Username: admin

Email: admin@littlelemon.com

Password: lemon@789!

Step 8: 
Open the file urls.py and remove the commenting for the line below:

1
# path('ratings', views.RatingsView.as_view()),
Step 9:
Open the Terminal in VS Code and run both the commands to perform the migrations.

Step 10: 
Once the migrations are performed successfully, run the command to start the server on the localhost and go to the URL: http://127.0.0.1:8000/admin

Enter the details of the credentials for the superuser you have created in step 8 and log into the Django admin panel. The Django Admin home page should appear as below:

Django admin panel with the superuser login details.
Step 11:  
Click on Users and click on Add User again. Enter the following details for the new user:

Username: Adrian

Email: adrian@littlelemon.com

Password: lemon@adr!

 Press the Save button and add another user and enter the following details for the second user:

Username: Mario

Email: mario@littlelemon.com

Password: lemon@mar!

 Press the Save button once again and add a third user with the following details:

Username: Sana

Email: sana@littlelemon.com

Password: lemon@san!

 Press the Save button. Ignore the information on the user details screen that appears and press the Home button in the left-hand corner of the page.

Django admin panel for user changing 
Step 12:  
Now press the Tokens option listed under Auth Tokens and press Add Token. 

Step 13:  
Select Adrian from the dropdown menu and press the Save button. 

 

The user called Adrian appears in the user dropdown menu in the Add token section
A screen will appear that contains Adrian's details along with a unique key generated for him. Follow the same process to generate tokens for the users Mario and Sana. Copy and save these tokens because you will use them later on in Insomnia.

Tokens for Mario and Adrian appears
Step 14:  
Now open the API request client, Insomnia and perform the following actions:

Create a POST request to the URL: http://127.0.0.1:8000/api/ratings

A POST request in the API client Insomnia.
Click on Body and select FORM URL Encoded as the data structure.

FORM URL Encoded is an option in the dropdown menu that appears when you click on Body.
Add the following details inside it:

menuitem_id: 3

rating: 4

Details for data structure added
 Under the Bearer section add the token value. For example,  for Adrian ad the token 4c7cbdf14c6e5b7cd481bb5bd681c89baba49f9d 

Also select the checkbox next to Enabled and update the Prefix with the value Token. 

Token for Adrian added in the Bearer section.
Press the Send button to generate the POST request. It will generate JSON output like in the screenshot below.

JSON object created by a POST request.
Step 15:
Now keep the value of menuitem_id unchanged but change the rating to 5. It should generate JSON output that is different to before, such as in the screenshot below. The error denotes the throttling limits you have placed on the number of reviews a user can add in a certain amount of time.  It means that any given user can add at most one rating for a specific menu item and a unique set must be created for a combination of a user and a menu item.

JSON output that displaces an error when a user try to give a menu item another rating.
Step 16:
Update the token id with the user Sana and use the same values with which you encountered an error, such as menuitem_id with value 3 and a rating value of  5. This should update the user review without any issue because it is now a new rating given by another user.

 

JSON output of user 6 for menu item id 3 with a rating of 5.
Step 17:
Switch the screen and go back to the webpage on your browser with the URL: 

http://127.0.0.1:8000/api/ratings

 Refresh the page to see if the entries for the reviews are updated.

 Concluding Thoughts 
In this exercise, you learned how to create default routes using Djoser and basic authentication and security mechanisms by implementing throttling functionalities in DRF. 

 

 