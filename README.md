### Design Ideas
Build a website to buy food that you can buy after registering as a member

### Development Process
First install the build environment and framework and start creating the site using the django administration tool. 
Set the parameters, then migrate the data you want to display, edit the code in models.py and views.py, urls.py 
for registration, login, shopping cart, food, then build the pages and test files

### Built environment
        pyenv local 3.7.0 # this sets the local version of python to 3.7.0
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

### Install web framework
      pip install django


### Build the super account
You can create a super user to view all orders in the user's shopping cart and to delete


          python manage.py createsuperuser
          python manage.py createsuperuser
          

### Exisiting super account
admin account:
superuser
12345
### Start the Server
python3 manage.py runserver 0.0.0.0:8000 
### Web Uses
It shows the nutritional content and variety of a wide range of foods and their value, and you can buy them

### heroku url:
    https://shopfood.herokuapp.com

### github url:
    https://github.com/xiaoyangjiayounuli/individual-assesment.git
