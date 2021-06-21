# photo-sphere-viewr
photo sphere viewer django bootstrap5

This is a simple django and photo-sphereviwer and Bootstrap5 web app project that has the fullowing features
1. you can upload the title and a panaromic image using add room, and it will give a sphere view.
2. Using add component on each items that have been added using 'Add Room' you can add marker on an specific 
   Longitude and Latitude which by double clicking on it, the current image will change to the image which is linked to the marker.


This is how you can run the project:
      
      - virtualenv environment_name
      - .\environment_name\Scripts\activate (optional) note: use forward slahs (/) if you are on linux.
      - pip install -r requirements.txt
      - python manage.py migrate
      - python manage.py makemigrations
      - python manage.py createsuperuser

To start the project simply copy and paste the url bellow on your browser
- http://127.0.0.1:8000

and you are ready to go
