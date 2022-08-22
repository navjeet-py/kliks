# KLIKS
#### An image sharing site, where user can signup, login, upload pictures, see and search for other’s profiles and pictures and download them.

#### For the front-end, we used HTML, CSS, and JavaScript. In the backend, Django and an SQL database are used. 

### Pages Views
<p align="center">
  <img src="https://raw.githubusercontent.com/navjeet-py/kliks/main/media/landing-page.jpeg" width="350" title="hover text">
  <img src="https://github.com/navjeet-py/kliks/blob/main/media/signup-page.jpeg" width="350" alt="accessibility text">
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

