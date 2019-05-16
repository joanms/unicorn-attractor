# UnicornAttractor

This is the Full-Stack Frameworks milestone project for Code Institute's full-stack web development course. It is an issue tracker for a fantasy game called UnicornAttractor. Users can report bugs they have experienced 
and request features they want added to the game. They can also upvote bugs and features. Upvoting bugs is free, but users can't upvote a bug they submitted, or upvote the same bug more than once. The only limit on 
upvoting features is the user's budget. Users can upvote any features they like as often as they like, but they need to pay a fee of €5 per upvote. The site developers will prioritise fixing the bugs with the most 
upvotes and spend at least 50% of their time implementing the highest-paying features.


## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.


## Features

### Existing Features
- **Home Page** welcoming users to the site and explaining its purpose.
- **Registration and Login Pages** allowing users to register and log into their accounts.
- **Profile Page** where logged in users can view their account details.
- **Bug Report Form** for users to report bugs they have experienced.
- **Page Listing All Reported Bugs** where users can see which bugs have already been submitted and click on buttons for more details about each one.
- **Bug Detail Page** giving all details for a single bug along with a button to upvote it and 
- **Feature Request Form** for users to report features they want.
- **Page Listing All Requested Features** where users can see which features have already been requested and click on buttons for more details about each one.
- **Feature Detail Page** giving all details for a single feature along with a form to purchase upvotes and a comments panel where users can read comments from other users and make their own.
- **Comments Panels** on the bug and feature detail pages where users can read comments from other users and make their own.
- **Cart** where users can see which upvotes they have added to their order.
- **Checkout** for users to pay for their upvotes.

### Features Left to Implement
- **Graphs** showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.


## Technologies Used

- **[Balsamiq](https://balsamiq.com/)** was used to create the wireframes.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)** was used to set up the templates for the site.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)** was used to style the site content.
- **[Bootstrap](https://getbootstrap.com/)** was used to facilitate the design and responsiveness of the site.
- **[Python](https://www.python.org/)** was used to write the site's logic.
- **[Django](https://www.djangoproject.com/)** was used as a framework to facilitate the development of the site.
- **[SendGrid](https://sendgrid.com/)** is used to send emails from the site.
- **[Travis](https://travis-ci.org/)** was used to test the code.
- **[Stripe](https://stripe.com/ie)** is used to process payments.
- **[Heroku](https://www.heroku.com/)** was used to deploy the project.


## Testing

### Travis Continuous Integration
[![Build Status](https://travis-ci.org/joanms/unicorn-attractor.svg?branch=master)](https://travis-ci.org/joanms/unicorn-attractor)

The Travis build is failing because of a syntax error in Travis' own env.py file:

File "/home/travis/virtualenv/python3.4.3/lib/python3.4/site-packages/env.py", line 51
    print k
          ^
SyntaxError: Missing parentheses in call to 'print'

The build passes when I comment out 'import env' in settings.py.

### Automated Testing
Automated testing is carried out with Django's own testing framwork. To run the tests, run the following command in the CLI:

python3 manage.py test

### Manual testing
I carried out manual testing as follows:

#### Registration
1. Navigate to registration page.
2. Enter the email address of an already registered user and a new username.
3. Ensure that an error message appears, saying that email addresses must be unique.
4. Enter a unique email address and the username of an already registered user.
5. Ensure that an error message appears saying that a user with that username already exists.
6. Register several new users by filling in all fields correctly, and ensuring that all data entered is saved in the database.

#### Login
1. Navigate to the login page.
2. Log in as each registered user in turn, entering correct username and password combinations.
3. Ensure that the users are logged in successfuly.
4. Attempt to log in as each registered user, entering incorrect usnername and password combinations.
5. Ensure that an error message displays saying that the username or password is incorrect.

#### Password Reset
1. Click on the password reset link on the login page.
2. Ensure that a page appears inviting me to enter my email address.
3. Enter my email address in the box and click the Reset Password button.
4. Ensure that a page appears telling me that an email has been sent.
5. Check my inbox for the email.
6. Click on the link in the email and ensure that a page appears invting me to enter a new password.
7. Ensure that a page appears confirming that the password has been reset, and inviting me to log in.
8. Log in with the new password to ensure that it has been changed successfully.

#### Viewing Bug Details
1. Click on the "More Details" button of a bug on the page listing reported bugs.
2. Ensure that a page showing the details of that bug appears.
3. Ensure that all comments made about that bug, and only that bug, appear at the bottom of the page.

#### Upvoting Bugs
1. Click on the upvote button for a bug not submitted or already upvoted by the logged in user.
2. Ensure that the upvote count increases by one.
3. Click on the upvote button for a bug submitted by the currently logged in user.
4. Ensure that a message displays saying 'You can't upvote a bug that you submitted'.
5. Click on the upvote button for a bug already upvoted by the currently logged in user.
6. Ensure that a message displays saying 'You have already upvoted this bug'.

#### Viewing Feature Details
1. Click on the "More Details" button of a feature on the page listing reported bugs.
2. Ensure that a page showing the details of that feature appears.
3. Ensure that all comments made about that feature, and only that feature, appear at the bottom of the page.

#### Upvoting Features
1. Enter a quantity of upvotes to purchase in the field provided and click on "Upvote".
2. Ensure that a page showing the cart appears.
3. Change the quantity of upvotes in the field provided and click "Update".
4. Ensure that the quantity is updated.
5. Click on "Checkout".
6. Ensure that a payment details form appears.
7. Fill in the form with fake details and click "Submit Payment".
8. Ensure that the payment is successful.
9. Ensure that the number of upvotes and amount paid for that feature are updated in the database.
10. Ensure that an upvote object with the details of the user, feature and amount paid is created in the database.


## Credits

### Media
The images were downloaded from [PixaBay](https://pixabay.com/). 
The logo is by [Clker-Free-Vector-Images](https://pixabay.com/users/Clker-Free-Vector-Images-3736/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=310175). 
The background image is by [M. Maggs](https://pixabay.com/users/Wild0ne-920941/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1158017).

### Acknowledgements
Michael Park, Haley Schafer and Chris Zielinski provided valuable help and advice on the project.

[Marcin Mrugacz's project](https://github.com/Migacz85/django_app) gave me ideas about how to approach my own.