# Online Library - ALX Foundation Portfolio Project

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://git@github.com:MikiyasA/Online_Library-ALX_Foundation_Portfolio_Project.git
```

Then make sure your machine is capable to run the code. The below command is for Linux OS

```sh
sudo apt-get install python3.*
sudo apt install python3-django
pip install django-crispy-forms
```
Change your directory to the folder that holds manage.py file. After that, create super user to have admin write and access admin page.
```sh
python3 manage.py createsuperuser
"""Then follow the stapes and provide the information needed."""
```

Then, it is time to run the program. Just enter the below command without changing your directory.

```sh
python3 manage.py runserver
"If you want to run it with different port, use the below"
python3 manage.py runserver <port_no_you_want>
```
And navigate to `http://127.0.0.1:8000/`. or `http://127.0.0.1:<port_no_you_enter>/`

## Setting 

You can deploy this system with two different database system, MySql or sqlite. Just open setting.py file located in `../onlinelibrary` directory make adjustment as be below.

`To run with sqlite database, make sure to uncomment the below code and comment any code line start with "DATABASES = {"`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
`To run with MySql database, make sure to uncomment the below code and comment any code line start with "DATABASES = {"`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<name_of_your_schema>',
        'USER': '<user_name_with_write_privilege>',
        'PASSWORD': '<password>',
    }
}
```

## Bird view of the system

This system is web based online library system developed using once of best python web framework called Django. Books are a light for life of human being, and this kind of system will give huge benefit to society. That’s why it inspires me to develop this system of foundation portfolio project. 
The first thing you see when you open the system is, home page which will list the post made by the user who have access. Then, when open book page, it will show you available shelves created to hold the books as per shelf category. `When you create shelves, please make sure to be specific. It will help you when you on categorizing the books.` For example, `it is best creating python book shelf than programming book shelf. ` Then when you click the shelf, it will direct you to the list of books added in that shelf. Then the site has about and contact page for general information. There is also navigation to direct you to standard admin page. It will prevent you to write on address bar every time you want to access the admin page. 

## DEVELOPER

Mikiyas Adere 
[Github](https://github.com/MikiyasA) - https://github.com/MikiyasA
[Gmail](mailto:Mikiyasad86@gmail.com) -  Mikiyasad86@gmail.com
[Phone](+251921162566) - +251921162566
