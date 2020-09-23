# Dj_AirBnb_Simple_Project
Simple Django Project as Cope from "https://www.airbnb.com/"
Documentation :
1- Create Virtual env
    - From your PC & Where You want to Save Your Works Right Clic and Git Bash Here
	- Type -------------------> virtualenv -p python3.8 virtaul_name 
========================================================================================   
2- Activate your Virtual env
	- cd Virtual env name
	- On Windows Type --------> source Scripts/activate
	- On IOS     Type --------> source bin/activate
========================================================================================
3- Install Django
	- Type -------------------> pip install django
========================================================================================   
4- Create your REPO on GitHub
	- Public 
	- Add a README file
	- Add .gitignore (Python)
	- After Creation ---------> Edit the .gitignore 
								by remove db.sqlite3 & db.sqlite3-journal From it
								Save your Change
	- Copy Your Repo URL
========================================================================================	
5- Clone Your Repo from the GitHub
	- Type -------------------> python.exe -m pip install --upgrade pip
	- Type -------------------> git clone your Repo URL
========================================================================================
6- In Your PC Rename Your Repo Name in youe ENV Location
	- Rname it to ------------> src
   =================================   project   ===================================
7- Create Your Project
	- Go Inside src Folder ---> cd src
	- Type -------------------> django-admin startproject project .
	- Open VISCODE from This location
========================================================================================
8- Run The Server
	- Type -------------------> python manage.py migrate
	- Type -------------------> python manage.py runserver
========================================================================================
9- Create Your Super User
	- Type -------------------> python manage.py createsuperuser
========================================================================================
10- Save Your Works
	- Type -------------------> git add .
	- Type -------------------> git commit -m "Type Your Comment"
	- to send it to your GitHub 
	  Type -------------------> git push
    =================================   APPS   ====================================
11- Start to Create your Apps
	- Type -------------------> python manage.py startapp App1
	- Type -------------------> python manage.py startapp App2
	- Type -------------------> python manage.py startapp App3
	- Type -------------------> python manage.py startapp App4
========================================================================================
12- To Show your App on Django you need to Add on the so on :
	Project --> setting.py --> Last of the INSTALLED_APPS
	- Type -------------------> 'your app name',
   =================================   MODELS   ====================================
   ===================  all this Fields Name is only for example ===================
13- Create Database for your app in models of this app
	- App --> Models --> build you table of this app like this:
		a- after last import operation type ---> 
				from django.utils import timezone
		b- if you need select list use this example:
				UNIT_TYPE = (
					('CHALEH','CHALEH'),
					('ROOM' , 'ROOM'),
					('FLAT' , 'FLAT'),
					('STUDIO' , 'STUDIO'),
					('Lounge' , 'Lounge'),
				)

				UNIT_STATUS = (
					('AVAILABLE TO RENT','AVAILABLE TO RENT'),
					('RENTED' , 'RENTED'),
					('AVAILABLE TO SELL','AVAILABLE TO SELL'),
					('SOLD' , 'SOLD'),
					('SUSPENDED' , 'SUSPENDED'),

				)
		c- build you table as this example:
				
				# Area Table
				class Area(models.Model):
					title = models.CharField(max_length=60, verbose_name='Area', )

					def __str__(self):
						return self.title

				# City Table
				class City(models.Model):
					title = models.CharField(max_length=60, verbose_name='City', )
					#area = models.ManyToManyField(Area)

					def __str__(self):
						return self.title

				# Country Table
				class Country(models.Model):
					title = models.CharField(max_length=60, verbose_name='Country', )
					#city = models.ManyToManyField(City)

					def __str__(self):
						return self.title

				# Furniture Table
				class Furniture(models.Model):
					title = models.CharField(max_length=60, verbose_name='Furniture', )
					#city = models.ManyToManyField(Furniture)

					def __str__(self):
						return self.title

				# Rooms Table
				class Room(models.Model):
					title = models.CharField(max_length=60, verbose_name='Room', )
					
					def __str__(self):
						return self.title 
				
				# Main Unite Table
				class Unit(models.Model):

					title = models.CharField(max_length=60, verbose_name='Unit Title', unique=True ,) # Title
					description = models.TextField(max_length=500, verbose_name='Unit Description') # Description
					price = models.DecimalField(max_digits=10,decimal_places=2) # How much Price
					num_bedrooms = models.IntegerField( verbose_name='Number of Bed rooms') # Count of Closed Rooms
					hole_space = models.IntegerField( verbose_name='Hole Space') # Count of Closed Rooms
					image = models.ImageField(upload_to='units_images/' , blank=True , null=True, verbose_name='Unit Main Image') # Internal Images
					active = models.BooleanField(default=True) # Post Status
					owner_email = models.EmailField(default='m.medhat@dropsgroup.com') # Email
					type = models.CharField(choices=UNIT_TYPE , default='FLAT',max_length=20) # Unite Type
					status = models.CharField(choices=UNIT_STATUS , default='SUSPENDED',max_length=20) # Unite Status
					country = models.ForeignKey(Country, on_delete=models.CASCADE) # Country
					city = models.ForeignKey(City, on_delete=models.CASCADE) # City
					area = models.ForeignKey(Area, on_delete=models.CASCADE) # Area
					#furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE) 
					furniture = models.ManyToManyField(Furniture) # Room Type
					Room = models.ManyToManyField(Room) # Room Type
					remarks = models.TextField(max_length=500, blank=True , null=True, verbose_name='Remarks') # Remarks
					created_at = models.DateTimeField(default=timezone.now) # Post Creation Date
					
		d- To use the title to shown as the main field after the table builder type:
		
					def __str__(self):
						return self.title 
						
	- To Take a look for Django Fields go to:
	
		https://docs.djangoproject.com/en/3.1/ref/forms/fields/
		
========================================================================================
14- Make your Migrations
	- Type -------------------> python manage.py makemigrations
========================================================================================
15- Make your Migrate
	- Type -------------------> python manage.py migrate
========================================================================================
16- To show your app in the admin panel
	- go to your app location --> admin.py
	- Type -------------------> from .models import Class Name of this app
	- If You Have More than One Class in the same App go to your app location --> admin.py
	- Type -------------------> from .models import Class_Name_1, Class_Name_2, Class_Name_3
	- To Rigester your app in the admin
	- Type -------------------> admin.site.register(Class Name of this app)
	- To Rigester your app which Have more than one class in the same app go to your app location --> admin.py
	- Type -------------------> admin.site.register(Class_Name_1)
								admin.site.register(Class_Name_2)
								admin.site.register(Class_Name_3)
   =================================   IMAGES   ===================================
17- Adding Image to your App ( You need to install library first to allow you for that)
	- Type -------------------> python -m pip install Pillow
	* Add Setting for Media files:
	  go to https://docs.djangoproject.com/en/3.1/howto/static-files/
	- Go to Project --- > Setting ---> After : 
	    STATIC_URL = '/static/' ------> Add :
	
		STATICFILES_DIRS = [
			BASE_DIR / "static",
			'/var/www/static/',
		]
	- Go to main urls file in this location : Project --> urls.py and add this two line:
		from django.conf import settings
		from django.conf.urls.static import static
		
	- At the same place	Project --> urls.py After :
		urlpatterns = [
			path('admin/', admin.site.urls),
		]
		add :
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
		
	- Go to Project --- > Setting ---> After : 
		STATICFILES_DIRS = [
			BASE_DIR / "static",
			'/var/www/static/',
		] 
		------> Add :

		MEDIA_URL = '/media/'
		
		MEDIA_ROOT = "media"
	
	- Go to main urls file in this location : Project --> urls.py and update this :		
		urlpatterns = [
			path('admin/', admin.site.urls),
		]
	--------------> TO :
		urlpatterns = [
			path('admin/', admin.site.urls),
			path('app name/', include('app name.urls'))
		]
		
	- Go to main urls file in this location : Project --> urls.py and update this :		
		from django.contrib import admin
		from django.urls import path
		from django.conf import settings
		from django.conf.urls.static import static
	--------------> TO :
		from django.contrib import admin
		from django.urls import path , include
		from django.conf import settings
		from django.conf.urls.static import static

		
	* Add Image field to your class:
	- Type -------------------> 
		image = models.ImageField(upload_to='units_images/' , blank=True , null=True, verbose_name='Unit Main Image') # Internal Images
	* If you have records already in your class you get error because the default values in this field is'nt allowed
		so you need to choice number 1 and thin type '' as default value for the old records
	- Type -------------------> python manage.py makemigrations
	- Type -------------------> python manage.py migrate
   =================================   VIEWS   ===================================
