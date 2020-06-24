
# Portfolio in Django 

 

A template to build your own portfolio in django. Add the details in Django admin panel and create your own portfolio. 

The project structure is as follows.

### Prerequisites

- Python 3.7

- Git

- pipenv

  
  

## Manual steps to get the app running in local environment.

  

1. Clone the repo using git - **`git clone https://github.com/anu37/Portfolio.git`**

2. Execute **`cd ./portfolio`**

3. Execute **`pipenv shell`**

4. Execute **`pipenv install`**

5. Migrate the models into SqlLite DB by using **`python manage.py migrate`**

6. Run the server using **`python manage.py runserver `**

  

To access the admin panel and the swagger UI you can create a super user using the command

 
    python manage.py createsuperuser


### Links

  

*  **Admin Dashboard** - http://localhost:8000/admin/

*  **Portfolio** - http://localhost:8000/
  

## Add details in Admin Panel Models

  

1.  **About Me** -  Basic information required for building the first few sections of the portfolio.
2. **Job** - Add your employment details with role, responsibilities and year in it.
3. **Education** - Add your education details. 
4. **Skill Catgeory** - Depends on how many category of skills you want to add. 
5. **Skill** - Skills can be addede for each category and the percenatge level of expertise. 
6. **Language** - Languages you know with expertise level within 5 stars.
7. **Blog** - Add the details of blog written. 