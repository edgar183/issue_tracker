[![Build Status](https://travis-ci.org/edgar183/issue_tracker.svg?branch=master)](https://travis-ci.org/edgar183/issue_tracker)

# Issue Tracking App

The issue tracking web application that allows users to create issues tickets, comment on this issues, and show the status of the issue currently on the system (‘TODO’ ‘DOING,’ or ‘DONE’ status).

- Issues come in two types:
  - ‘Bugs’ that are fixed for free,
  - ‘features’ that are only implemented if offered enough money.
- To help prioritize the work, users are able to upvote bugs - signifying ‘I have this too’, and upvote feature requests - signifying ‘I want to have this too’ (features can be upvoted after purchasing them).
- This is a full stack web application (frontend and backend) that provides CRUD (Create, Read, Update, Delete) functionality to a database hosted in the cloud on Heroku platform as a service.
#### [Issue Tracker webiste](https://edgars-issue-tracker.herokuapp.com/)
## UX Design

This application is for users that are using [Book Reading Lists](https://book-reading-lists.herokuapp.com/index) web application and have encountered any bugs that they can report using **'bookbug'** issue tracking system or they want a new feature to be implemented in the application.

#### User Stories

- As a user can, I can browse all the bugs and features on the website, so that I can see all of them without registering an account.
- As a user can, I can see charts of bugs and features in the system, so that I can see how many of each of the issues are that in the system and see the status of all of them.
- As a user, I can search for issue by the title of the tag, so that I can see all the issues in the system.
- As a user, I can register an account, so that I have full access to the website.
- As a registered user, I can create a new bug report, so that I can show the issue I have encountered.
- As a registered user, I can create a new feature request, so that I can ask the developer to implement this feature.
- As a registered user, I can create a comment in 'bug' or 'feature' page, so that I can add my comments on the issue.
- As a registered user, I can edit my comments on the 'bug' or 'feature' pages so that the information is accurate.
- As a registered user, I can remove my comment from 'bug or feature' pages, so that I can remove unwanted comments.
- As a registered user, I can edit my 'bug' or 'feature' on the website so that the information is updated.
- As a registered user, I can delete my 'bug' or 'feature' on the website, so that I can remove unimportant issues.
- As a registered user, I can edit my profile, so that I can change my email, name and profile image.
- As a registered user, I can see all my 'bug' or 'feature reports, so that I can track the status of my reported issue.
- As a registered user, I can upvote bug report, so that I can show that I have this as well.
- As a registered user, I can purchase feature, so that I can show that I have would like this as well.
- As a super user (admin), I can edit all issue reports, so that I can change the status of each of them.

#### Wireframes

- [Issue page when the user is not registered](https://drive.google.com/file/d/1p3GGAZD_3aAa9tzUqLGxbkFHsHNOKQ6e/view?usp=sharing)
- [Issue details page when the user is signed in the system](https://drive.google.com/file/d/1NB6iiWidPnn7G_SeMmNWB7aSIOOlkaT0/view?usp=sharing)
- [Add new issue form](https://drive.google.com/file/d/1E9WuJu-zs3yF8oLAjR9ZbQyba-HTZDyk/view?usp=sharing)
- [User profile page](https://drive.google.com/file/d/1jT1ocgnkre4oe5iPW28JKtbujAgGvhce/view?usp=sharing)

## Features

- Unregistered users can look at all bug and feature reports and dashboard charts.
- Registered users can add new bug or feature reports and edit delete them.
- Registered users can comment on all bugs or feature reports.
- Superuser can change the status of bugs and features by editing details of them.

### Existing Features

Users can :

1. View list of all bugs and features sorted by newest descending with pagination and search by keyword.
2. Add New bug or feature, by filling in form.
3. Add New Comment to a bug or feature, by filling comment form on the bug detail page.
4. Upvote Bugs for free on the bug detail page, by clicking 'thumbs up' button.
5. Upvote Features, by adding the desired quantity of upvotes of a feature to the shopping cart and using the checkout functionality to submit payment.
6. Edit a bug or feature, Comment, by clicking the edit button in detail pages.
7. Edit shopping cart, by adding more or fewer quantity items in the cart page.
8. View list of bugs and features created by current logged in user, by visiting the profile page.
9. View dashboard showing charts for Bug Upvotes, Feature Upvotes, Number of Issues and Bug/Feature Status.

Super User:

1. Can change the status of bug or feature, by editing individual issue details.
2. Can mark a bug as fixed, by editing bug details and checking the fix checkbox.
3. Can mark feature be implemented, by editing feature details page and checking 'is implemented' checkbox.
4. Can edit, delete, add new bug and feature.

### Features Left to Implement

1. Superuser can assign new staff members to form his profile page.
2. User can replay on the comment
3. Add information in dashboard about a number of issues tended to on a daily, weekly and monthly basis.
4. Create a blog page to post updates about the main application

## Technologies Used

- HTML, CSS, JavaScript, AWS S3 API,
- [Bootstrap](https://getbootstrap.com/) - The frontend UI design framework.
- [Chart.js](https://www.chartjs.org/docs/latest/) - The chart library to create a dashboard
- [Stripe Payments API](https://stripe.com/ie) - The payment API that looks after the e-commerce part of the application.
- [Python](https://www.python.org/) - The project uses **Python 3.5** to handle backend logic of data processing between database and UI.
- [Django Full Stack Web Application Framework](https://www.djangoproject.com/) - The project uses this as the core application development framework version 1.11
- [PostgreSQL](https://www.postgresql.org/) - The project uses **PostgreSQL** database in the cloud on Heroku.

## Testing

Automated tests are located in the Issues app in test_models.py, test_forms.py and test_views.py. These 16 tests passed as per screenshot in Testing folder. To run the test:
`python3 manage.py test`

Manual testing was undertaken for this application and satisfactorily passed. A sample of the tests conducted are as follows:

1. Testing navigation buttons and hyperlinks throughout the page.
2. Testing the CRUD functionality: adding and editing Bugs, Features and Comments.
3. Testing the responsiveness of the application on different browsers and then using different devices.
4. Testing ecommerce functionality: generating order transactions with Add to Cart, Checkout and payments with Stripe test card details.
# 5. Testing image upload to AWS S3 bucket.?????

## Deployment

Heroku:
1. Install Heroku on a local terminal sudo (Linux OS) sudo snap install --classic heroku
1. After you install the CLI, run the heroku login -i command. You’ll be prompted to enter your email and password for heroku
1. Create a new heroku app by typing this command in terminal heroku create
1. In order to push a new app to heroku, we need requirements.txt, this file has all versions of all installed packages in a local virtual environment and Procfile file. With this command git push heroku master, we push the new app to heroku hosting server.
1. In heroku dashboard under Settings -> Config Vars we need to add
      - DATABASE_URL : postgres:// **url address**
      - SECRET_KEY : user adds this
      - STRIPE_PUBLISHABLE : user adds this
      - STRIPE_SECRET: user adds this
      - DEBUG : False


Run app Locally:
1. Clone repo from gitHub git clone https://github.com/edgar183/issue_tracker.git
1. Install requirements: pip install -r requirements.txt (may require sudo)
1. Run the local development server: python manage.py runserver
   - If host not allowed add a new host to `issues_tracker -> settings.py` in ALLOWED_HOSTS add your localhost address.
1. In CLI type `pyhon3 manage.py createsuperuser` to create admin for the application


Differences between development and production versions are:
- `debug=True` in settings.py file, development version
- `debug=False` in settings.py file, productions version

## Credits
### Media
The photos used in this site were obtained from:

- [Pexels](https://www.pexels.com/search/bug%20drowing/) was used to set the default profile picture.
- [IconFinder](https://www.iconfinder.com/) was used to get a favicon and logo icon.

### Acknowledgements

I used the following [blog](https://simpleisbetterthancomplex.com/) for tutorials on various Django topics such as AWS S3 integration, forms, integration

The Accounts, Cart and Checkout apps are based upon the sample apps from the User Authentication and Authorisation and Ecommerce mini project components of the Full Stack Frameworks with Django module.
