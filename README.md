# myecom
ecommerce website
## This is a step-by-step guide to create a basic website from scratch using django

Note: we have neither set up virtual environment. In the next project we'll do it. We'll also set up a testing folder.

### Step 1. 
Install these django plugins from VSCode marketplace: django-intellisense, django Template and django Snippets. They will make your life easier.

### Step 2. 
Create the folder in terminal:
```
mkdir myecom
```
### Step 3. 
Get inside the folder 
```
cd myecom
```
and run the following command:
```
django-admin startproject
```
### Step 4.
Create a github repository to link the local one. Use thse commands step by step (run one by one):
```
git init
gh repo create
git add .
git commit -m 'your comment'
git push origin master
```
After the first push, change the branch with the following command:
```
git checkout -b your_branchname
```
### Step 5.
Create a new app by running
```
python manage.py startapp appname
```
and then save the changes by running back-to back these lines:
```
python manage.py makemigrations
python manage.py migrate
```
### Step 6.
Include the catalog app in the 'settings.py' file in the main folder (in this case it's myecom)

### Step 7.
Hide secret key fro github. The key on local machine was on settings.py
It has to be put in the .env file and then transferred to settings.py in the following steps:

Create File => .env

Cut this from settings.py =>

SECRET_KEY = '-----your secret key-----'

Paste in .env

Write this in settings.py =>

from decouple import config

SECRET_KEY = config("SECRET_KEY")

Write this in terminal or cmd =>

pip install python-decouple

Then write this in terminal or cmd =>

pip freeze > requirements.txt

Go in cPanel and upload File .env

### Step 8.
create superuser:
```
python manage.py createsuperuser
```
### Step 9.
Edit the apps models in the file models.py in the app folder. Here we have a simple model with Item, Orderitem and Order field

### Step 10.
Import and register the models in the admin.py in the same folder (i.e. in the same app) 

### Step 11. 
Create urls.py in the catalog folder, and 
