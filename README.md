# Unicorn Attractor

The Full-Stack Frameworks milestone project for Code Institute's full-stack web development course.

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

- **[Balsamiq](https://balsamiq.com/)** was used to create the wireframes.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)** was used to set up the templates for the site.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)** was used to style the site content.
- **[Bootstrap](https://getbootstrap.com/)** was used as the basis for the site's layout and responsiveness.
- **[Python](https://www.python.org/)** was used to write the site's logic.
- **[Django](https://www.djangoproject.com/)** was used as a framework to simplify the development of the site.
- **[SendGrid](https://sendgrid.com/)** was used to send emails from the site.
- **[Travis](https://travis-ci.org/)** was used to test the code.
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
#### Registration
1. Navigate to registration page.
2. Enter the email address of an already registered user and a new username.
3. Ensure that an error message appears, saying that email addresses must be unique.
4. Enter a unique email address and the username of an already registered user.
5. Ensure that an error message appears saying that a user with that username already exists.
2. Register several new users by filling in all fields correctly, and ensuring that all data entered is saved in the database.

#### Login
1. Navigate to the login page.
2. Log in as each registered user in turn, entering correct username and password combinations.
3. Ensure that the users are logged in successfuly.
4. Attempt to log in as each registered user, entering incorrect usnername and password combinations.
5. Ensure that an error message displays saying that the username or password is incorrect.

#### Password reset
1. Click on the password reset link on the login page.
2. Ensure that a page appears inviting me to enter my email address.
3. Enter my email address in the box and click the Reset Password button.
4. Ensure that a page appears telling me that an email has been sent.
5. Check my inbox for the email.
6. Click on the link in the email and ensure that a page appears invting me to enter a new password.
7. Ensure that a page appears confirming that the password has been reset, and inviting me to log in.
8. Log in with the new password to ensure that it has been changed successfully.

## Acknowledgements
### Media
The images were downloaded from [PixaBay](https://pixabay.com/). 
The logo is by [Clker-Free-Vector-Images](https://pixabay.com/users/Clker-Free-Vector-Images-3736/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=310175). 
The background image is by [M. Maggs](https://pixabay.com/users/Wild0ne-920941/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1158017).