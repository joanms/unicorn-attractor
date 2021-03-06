[![Build Status](https://travis-ci.com/joanms/unicorn-attractor.svg?branch=master)](https://travis-ci.com/joanms/unicorn-attractor)

# UnicornAttractor

This is the Full-Stack Frameworks milestone project for Code Institute's full-stack web development course. It is an issue tracker for a fantasy game called UnicornAttractor. Users can report bugs they have experienced and request features they want added to the game. They can also upvote bugs and features. 

Upvoting bugs is free, but users can't upvote a bug they submitted, or upvote the same bug more than once. The only limit on upvoting features is the user's budget. Users can upvote any features they like as often as they like, but they need to pay a fee of at least €5 per upvote. The site developers will prioritise fixing the bugs with the most upvotes and spend at least 50% of their time implementing the highest-paying features.

The status of bugs and features is set to either To Do, In Progress, Done or cancelled by the site's admin via the Django admin interface.


## UX
 
### User Stories
- **As a new user, I want clear information about the site's purpose.** There is a welcome message on the home page, clearly explaining the site's purpose. When a new user registers, they are taken to a profile page with links to pages where they can submit or upvote tickets.

- **As a returning user, I want a history of my interactions with the site.** As soon as the user logs in, they see a profile page listing the bugs and features that they have submitted and upvoted, with links to those bugs and features. If they haven't submitted or upvoted tickets in a given category, they see links to pages where they can do so.

- **I want to be able to navigate easily around the site.** The navbar has clearly labelled links to all pages on the site, grouped in dropdown menus where appropriate. There are also buttons and text links throughout the site linking users to pages directly related to the page they are on.

- **I want to be able to communicate with other users.** Each page giving details of a bug or feature has a comments panel where users can read comments about it from other users, and add their own comments.

- **I want to be able to communicate with the site's admin.** There is a link in the navbar and in the welcome text on the home page enabling users to email the site's admin. Please note that since this is a site for a fictional game, the email address is fake. I consider email preferable to a contact form because the user will automatically have a copy of their communication in their email sent items and any chain of communication between the user and the site admin can be maintained.

- **I want the process of submitting tickets to be clear and intuitive.** There are links in the navbar to forms where users can report bugs and request features. These links also appear as buttons on the pages listing all reported bugs and all requested features.

- **I want the process of upvoting bugs to be clear and intuitive.** There is a clearly labelled upvote button on each page giving the details of a single bug. If the user submitted the bug or upvoted it on a previous occasion, they see a message telling them they can't upvote it instead of the upvote button. If the clicks the upvote button again after upvoting, they see a message telling them they have already upvoted.

- **I want the process of upvoting features to be clear and intuitive.** On each page giving the details of a single feature, there is a box where users can enter their chosen price and an upvote button beside it. The box will not accept any value below the minimum price of €5, and if the user attempts to enter a value below €5, they see a message reminding them of this.

     When the user enters a valid price for upvoting a feature and clicks the upvote button, the upvote is added to their cart, and they are taken to a page showing the cart contents. They click the plus or minus buttons to change the price, the delete button to remove an item or the button inviting them to view other features to upvote. 

- **I want the payment process to be clear and efficient.** If the user doesn't want to alter the cart contents, or if they have finished doing so, they can click the checkout button, which takes them straight to the payment page. When they enter their details and click the Submit Payment button, they see a message telling them whether or not the payment was succesful.

### Design
Please [click here](static/plans/unicorn_attractor_wireframes.pdf) to view the wireframes.

The site is for a fantasy game, and the colour scheme, fonts and background image were chosen with this in mind. Because the site is supposed to serve a practical purpose, I made it as straightforward and streamlined as possible to avoid confusing or frustrating users, but still visually interesting so that it would be pleasant to use.

The pages displaying all reported bugs, all requested features and the cart comprise cards with summaries of the bugs or features. I considered using tables for these pages, but tables do not work very well on small screens. The content can look squashed, or have horizontal scrollbars because the columns don't all fit on the screen. Cards in a flexbox container are much more suitable for a responsive website. They can be displayed in a single column on the smallest screens, with the number of columns increasing with the width of the screen. The height of the cards is set to adjust to their contents. This results in unequal heights, but I decided that this was preferable to blank spaces at the bottom of cards with less content than others.

The buttons are prominently displayed and clearly labelled to make it easy for users to see what they have to click to progress through the site.


## Features

- **Home Page** welcoming users to the site and explaining its purpose.
- **Registration and Login Pages** allowing users to register and log into their accounts.
- **Profile Page** where logged in users can view their account details.
- **Bug Report Form** for users to report bugs they have experienced.
- **Page Listing All Reported Bugs** where users can see which bugs have already been submitted and click on buttons for more details about each one.
- **Bug Detail Page** giving all details for a single bug along with a button to upvote it and a comments panel where users can read comments about the bug from other users and make their own.
- **Feature Request Form** for users to report features they want.
- **Page Listing All Requested Features** where users can see which features have already been requested and click on buttons for more details about each one.
- **Feature Detail Page** giving all details for a single feature along with a form to purchase upvotes and a comments panel where users can read comments from other users and make their own.
- **Comments Panels** on the bug and feature detail pages where users can read comments about the feature from other users and make their own.
- **Cart** where users can see which upvotes they have added to their order. They can also adjust the price of their order, add items by clicking the button linking them to the page listing all features, and delete them by clicking the delete button for the feature they want to delete.
- **Checkout** for users to pay for their upvotes.
- **Graphs** showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the highest-voted bugs and features.


## Technologies Used

### Languages
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)** was used to set up the templates for the site.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)** was used to style the site content.
- **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** was used for the tooltips and Stripe payment functionality.
- **[Python](https://www.python.org/)** was used to write the site's logic.
- **[SQL](http://www.sqlcourse.com/intro.html)** was used for the database.

### Frameworks/Libraries
- **[Bootstrap](https://getbootstrap.com/)** was used to facilitate the design and responsiveness of the site.
- **[Django](https://www.djangoproject.com/)** was used as a framework to facilitate the development of the site.

### Tools
- **[Balsamiq](https://balsamiq.com/)** was used to create the wireframes.
- **[Heroku](https://www.heroku.com/)** was used to deploy the project.
- **[Pygal](http://pygal.org/en/stable/)** was used to create the graphs.
- **[SendGrid](https://sendgrid.com/)** is used to send emails from the site.
- **[Stripe](https://stripe.com/ie)** is used to process payments.
- **[Travis](https://travis-ci.org/)** was used to test the code.


## Testing

### Code Validation
I validated the HTML with the [W3C Markup Validation Service](https://validator.w3.org/) and the CSS with the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The HTML marked the Django template language code and some code necessary to run Stripe as incorrect. I visually checked the code in question.

### Automated Testing
Automated testing is carried out with Django's own testing framwork. To run the tests, run the following command in the CLI: ``python3 manage.py test``

### Manual testing
I carried out manual testing as follows:

#### Cross-Browser and Device Compatibility
1. Test the app on Chrome, Edge, Firefox, Opera and Safari browsers to ensure that it works on all of them.
2. Test the app on a desktop, laptop, tablet and smartphone to ensure that it works on all devices.

#### Responsiveness
1. View the app in responsive mode with Chrome Developer Tools to ensure that the size and position of elements adjusts correctly.
2. View the app on a desktop, laptop, tablet and smartphone to ensure that it displays correctly.


#### Accounts

##### Registration
1. Navigate to the registration page.
2. Enter the email address of an already registered user and a new username.
3. Ensure that an error message appears, saying that email addresses must be unique.
4. Enter a unique email address and the username of an already registered user.
5. Ensure that an error message appears saying that a user with that username already exists.
6. Register several new users by filling in all fields correctly, and ensuring that all data entered is saved in the database.

##### Login
1. Navigate to the login page.
2. Log in as each registered user in turn, entering correct username and password combinations.
3. Ensure that the users are logged in successfuly.
4. Attempt to log in as each registered user, entering incorrect usnername and password combinations.
5. Ensure that an error message displays saying that the username or password is incorrect.

##### Password Reset
1. Click on the password reset link on the login page.
2. Ensure that a page appears inviting me to enter my email address.
3. Enter my email address in the box and click the Reset Password button.
4. Ensure that a page appears telling me that an email has been sent.
5. Check my inbox for the email.
6. Click on the link in the email and ensure that a page appears invting me to enter a new password.
7. Ensure that a page appears confirming that the password has been reset, and inviting me to log in.
8. Log in with the new password to ensure that it has been changed successfully.


#### Bugs

##### Reporting Bugs
1. Navigate to bug report form.
2. Enter text in both fields and click "Submit Report".
3. Ensure that the bug appears on the page listing all reported bugs.
4. Click on "View Details" for the bug on the page listing all reported bugs and ensure that a page with its details appears.
5. Ensure that the bug is listed on the profile page of the user who submitted it.

##### Viewing Bug Details
1. Click on the "More Details" button of a bug on the page listing reported bugs.
2. Ensure that a page showing the details of that bug appears.
3. Ensure that all comments made about that bug, and only that bug, appear at the bottom of the page.

##### Upvoting Bugs
1. Click on the upvote button for a bug not submitted or already upvoted by the logged in user.
2. Ensure that the upvote count increases by one.
5. Click on the upvote button again.
6. Ensure that a message displays saying 'You have already upvoted this bug'.
7. Ensure that the upvote is listed on the user's profile page.

##### Commenting on Bugs
1. Navigate to the page giving details of a single bug.
2. Click on the Add a Comment button.
3. Enter a comment in the form that appears.
4. Click the Submit Comment button.
5. Ensure that the comment appears in the Comments panel with the correct user and date details.


#### Features

##### Requesting Features
1. Navigate to feature report form.
2. Enter text in both fields and click "Request Feature".
3. Ensure that the feature appears on the page listing all requested features.
4. Click on "View Details" for the bug on the page listing all requested features and ensure that a page with its details appears.
5. Ensure that the feature is listed on the profile page of the user who submitted it.

##### Viewing Feature Details
1. Click on the "More Details" button of a feature on the page listing reported bugs.
2. Ensure that a page showing the details of that feature appears.
3. Ensure that all comments made about that feature, and only that feature, appear at the bottom of the page.

##### Upvoting Features
1. On a feature details page, enter a price for an upvote in the field provided and click on "Upvote".
2. Ensure that a page showing the cart appears.
3. Change the price of the upvote by clicking on the plus and minus buttons.
4. Ensure that the price is updated.
5. Click on "Browse other features to upvote".
6. Select another feature from the list to upvote, click on "View Details" and upvote it by repeating step 1 above.
7. Ensure that the correct feature and price are added to the cart.
8. Click on the Delete button for a feature.
9. Ensure that the feature is deleted from the cart.
10. Click on "Checkout".
11. Ensure that a payment details form appears.
12. Fill in the form with fake details and click "Submit Payment".
13. Ensure that the payment is successful.
14. Ensure that the order is added to the database with all correct details.
15. Ensure that the upvotes are listed on the user's profile page.

##### Commenting on Features
1. Navigate to the page giving details of a single feature.
2. Click on the Add a Comment button.
3. Enter a comment in the form that appears.
4. Click the Submit Comment button.
5. Ensure that the comment appears in the Comments panel with the correct user and date details.


## Deployment

I deployed the app as follows:
1. Create a new app on Heroku and name it joans-unicorn-attractor.
2. Enter the environment variables in the Heroku config vars
3. Ensure that the project includes a Procfile and requirements.txt.
4. Push the app to GitHub
5. Go to the Deploy tab for the app on Heroku and select GitHub as the deployment method.
6. Ensure that the master branch is selected and click Deploy Branch
7. Open the app on Heroku and check to ensure that it's working correctly.

There is a branch on GitHub named chartjs which uses Chart.js for the graphs. This branch is incomplete, and I may work on it further at a later date. However, as stated above, the master branch, which uses Pygal for the charts, is the one that was deployed and is being submitted for assessment.

### Running the Code Locally
Steps 1-6 were copied from [here](https://help.github.com/en/articles/cloning-a-repository)
1. Under the repository name on GitHub, click Clone or download.
2. In the Clone with HTTPs section, click the icon beside the URL to copy the clone URL for the repository.
3. Open Git Bash.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type git clone, and then paste the URL you copied in Step 2.
6. Press Enter. Your local clone will be created.
7. Create a virtual environment in which to run the code.
8. Install Django in the virtual environment by entering the following in the CLI: pip install django==1.11.
9. Install the packages in requirements.txt by running the following command in the CLI: ``pip install -r requirements.txt``
10. Set an environment variable for the SECRET_KEY.
11. Run the following command in the CLI: 
``python manage.py runserver``.


## Credits

### Code

Much of the code for the accounts, cart and checkout apps was copied from course material and adapted for this project. The main change to the accounts app was to add a custom user model that included fields for tickets submitted by the user. The main changes to the cart and checkout apps were to enable users to select a price instead of a quantity, and to link the users to their orders with a foreign key in the Order model. Please refer to the comments in the files for details.


### Media

The images were downloaded from [PixaBay](https://pixabay.com/). 
The favicon is by [Clker-Free-Vector-Images](https://pixabay.com/users/Clker-Free-Vector-Images-3736/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=310175). 
The background image is by [Anna Soppe](https://pixabay.com/users/beautifulugly-3087213/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2262633).


### Acknowledgements

Ali Ashik, Niel McEwen, Marie Obradovic, John O'Sullivan, Michael Park, Haley Schafer and Chris Zielinski provided valuable help and advice on the project.

[Marcin Mrugacz's project](https://github.com/Migacz85/django_app) gave me ideas about how to approach my own.