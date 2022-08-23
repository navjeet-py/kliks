# KLIKS
**An image sharing site using Django, where user can signup, login, upload pictures, see and search for other people’s profiles and pictures and download them.**

### Technologies used - 
**Front-end:** HTML, CSS, and JavaScript

**Backend:** Django, SQL

### Pages Views
<p align="center">
  <img src="https://raw.githubusercontent.com/navjeet-py/kliks/main/media/landing-page.jpeg" width="400" title="hover text">
  <img src="https://github.com/navjeet-py/kliks/blob/main/media/signup-page.jpeg" width="400" alt="accessibility text">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/navjeet-py/kliks/main/media/upload-page.jpeg" width="400" title="hover text">
  <img src="https://github.com/navjeet-py/kliks/blob/main/media/imageview-page.jpeg" width="400" alt="accessibility text">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/navjeet-py/kliks/main/media/search-page.jpeg" width="400" title="hover text">
  <img src="https://github.com/navjeet-py/kliks/blob/main/media/profile-page.jpeg" width="400" alt="accessibility text">
</p>


### The website will consist of seven pages –
1. Sign-up page
2. Log-in page
3. Main view page of a logged-in user
4. Image upload page
5. Image full view page
6. Profile page
7. Search results page


### Major Functionality Descriptions –
1. **Signup:** To create an account, a user will be asked to enter their name, email, and
password. This will be saved in a table in the database. The password will be encrypted
before saving. Users may also add a profile picture.

2. **Login:** The user will be asked to enter their registered email and password. This data will
be verified using users’ data saved in the database. They will be logged in to their profile
if the verification was successful.

3. **Upload image:** A user will be able to upload pictures, and add related tags. Those tags
can be used to search for an image. This data, along with the respective user and tags,
will be saved in the database.

4. **Search:** Any user will be able to look for required images by searching with relevant
words. The results will show images by other users, earmarked with the related tag.

5. **Main view page:** Latest pictures uploaded by other users will be picked up from the
database to be displayed here.

6. **Profile page:** The user’s basic information along with all the pictures uploaded by them
will be displayed here.

7. **Image full view page:** Here, an enlarged image will be displayed with a download
button. This will also tell us about the user who uploaded this. 

**Image Handling -** The images uploaded will be renamed to a random string and will be saved in
the uploaded_images folder and the file name along with other pieces of information related to
the image will be saved in the database, which will be used to fetch and display the image later.
Also, all images will be uniquely identified with an id.

### How to run at your computer
1. Download or pull the project directory at your system. 
2. We must have Python3 installed in our computer.
3. Set up a python virtual environment in the project folder and install all the libraries in the *requirements.txt* file. We may do it by typing `pip install requirements.txt` in our cmd or terminal.
4. Ta-da! We're ready to run the server. We'll go to the project directory in our cmd or terminal and type `py manage.py runserver`. Open `localhost:8000` in the web browser.
5. We have it running now. Create an account, upload pictures, see other's pictures, have fun!


Thank you.
