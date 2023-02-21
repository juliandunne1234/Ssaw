# Ssaw Collections

![Enter Pic](assets/images/amiresponsive.jpg)

[Live application can be found here](https://ssaw-collections.herokuapp.com/)

This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript. I have created a website for 'Ssaw - Nature Collection' that and allows customers to purchase prints of photography from the online shop. Ssaw is an acronym for Spring, Summer, Autumn and Winter and the nature collection is a theme of the shop whereby each collection focuses on a subject that captures the four seasons.

## Table of Contents
1. [**UX**](#ux)
    - [**Strategy**](#strategy)
    - [**User stories**](#user-stories)
    - [**Scope**](#scope)

2. [**Features**](#features)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)

---
## UX

## Strategy
Using the core UX principles I first started with Strategy, thinking about the target audience for this e-commerce store and the features they would benefit from.

The target audience for 'Ssaw' are:
- Homeowners, landlords, renting
- 20 to 65 year olds

These users will be looking for:
- An informative website, that is easy to use and easy to purchase items
- Ability to view all prints that are for sale
- User account functionality to view past orders and store billing information

It is assumed that there will be an even split between users viewing the website on their mobiles phone and laptops. Creating a responsive is integral to the website design. Bootstrap grids and elements & custom CSS was used for this purpose.

## User Stories

See defined user stories [here](https://github.com/users/juliandunne1234/projects/15)

### **Epic 1 - Website Layout and Navigation**:
1. As a user I can view the full list of items so that I can see everything that is for sale.
2. As a user I can view individual item details so that I can see the price, picture sizes, rating and the picture for sale.
3. As a user I can see cost of items in my shopping bag so that I can remain within budget.

### **Epic 2 - Registration and User Accounts**:
4. As a user I can register & login so that I can save my billing/shiping details for future purchases.
5. As a user I can login to my account so that I can see my previous purchases.
6. As a user I can recieve email confirmation so that I can verify my account registration.
7. As a user I can reset my password so that I can login to my account if I forget my password.

### **Epic 3 - Filtering Categories**:
8. As a user I can filter pictures by season so that I can search more easily for what I require.

### **Epic 4 - Purchasing Items**:
9. As a user I can see the items in my shopping bag so that I can add/remove items as required prior to purchasing them.
10. As a user I can change the item size so that I can order different sized pictures if required.
11. As a user I will recieve a confirmation email from the seller so that I can be sure the purchase completed successfully.

### **Epic 5 - Admin**:
12. As admin user I can add items so that I can add items available to purchase from the store.
13. As admin user I can update item details so that I can change price if on sale.
14. As admin user I can delete items so that I can remove items that are not in demand.

## Scope

In order to achieve the desired user & business goals, the following features will be included:

- Responsive navbar to navigate the various pages throughout the site
- Landing page with informative image carousel
- Products page, that displays all prints available for purchase with the option to filter by season.
- My Account page, for logged in users to update their details which in turn updates the user model. User is also able to view their previous orders and wishlist.
- Register/login feature using Django AllAuth so that users can create an account.
- Edit/Delete functionality so that future Ssaw collections can be added/removed from the website.
- Custom 404 and 500 error pages.

### Databases

The Elephant SQL database has been used for all database models: 

#### **Profiles App**

Profiles app allows authenticated users to save their information so that when a user is logged in the order form is pre-populated with their userprofile information, creating an improved user experience. The `UserProfile` model has a one-to-one field that is linked to the Django AllAuth user account, upon logging in the model method `create_or_update_user_profile` creates the profile if it isn't already present in the model.

#### **Products App**

Products app controls the products that are available  to purchase using the models `Product1` & `Category1`.

`Product1` allows adding/removing of products with the database. Only admin users are able to access this functionality and it can be done from the front end using the `add_product` view.

`Category1` stores the seasons  which each print is categorised under. The user can filter all products by season if required.

#### **Checkout App**

Checkout app is used to purchase prints from website using the models, `Order` & `OrderLineItem`. 

`OrdeLineItem` contains information regarding the products that have been purchased as part of a specific order. It has a foreign key to `Product1` & `Order`, it also contains the quantity purchased of that product and then the item total. This is then used to calculate the total cost for the order.

`Order` contains all of the relevant information for billing/shipping, a foreign key to the `UserProfile`. An order number is automatically generated when a new order is added to the database using `UUID`.

### Landing Page

'Ssaw Collections' was chosen for the name of the e-commerce store because the theme of the store is based on the four seasons of spring, summer, autumn and winter.

---

## Features

### Navbar

A fixed navbar remains at the top of each webpage at all times, allowing the user to easily navigate the website. The navbar is responsive and collapses the menu for smaller screen sizes. The options displayed vary depending on if the user is logged in and the access level that their account allows.

![](assets/images/fixed-navbar.jpg)

On mobile, the navbar is collapsed:

![](assets/images/mobile-navbar.jpg)

There is also a shopping bag icon with the order total including delivery displayed, to allow the user to keep track of the cost of their order.

### Footer

The footer includes a newsletter sign up form that uses Mailchimp and social media icons that are also links to social media sites. 
![](assets/images/footer.jpg)


### Home page

The home page implements the four seasons theme. There is a title and an animated bootstrap carousel, that displays images of each of the four seasons. 

![](assets/images/homepage.jpg)

### All products

This page displays all of the available prints for sale, displayed in a bootstrap grid. Each print has an image, name, photographer name, choice of sizes, price and rating.

![](assets/images/all_products.jpg)

Products can be filtered by category. The filter sends a query to the database and returns the products categorised by season.

![](assets/images/filter-by-season.jpg)


### Bag

The bag page provides an overview of all of the items added by the user. Product information is displayed that includes image, name, photographer, quantity, price and subtotal. The user can drop the item from the bag from this page. There is also buttons to proceed to the checkout or to keep shopping.  

![](assets/images/shopping-bag.jpg)

If there is nothing in the bag then the user can select the return to search button.

![](assets/images/return-to-search.jpg)

### Checkout

The checkout page is used to complete a purchase. There is a billing & card detail form to populate and a submit button to complete the transaction.

![](assets/images/checkout.jpg)

The card payment feature has been built using [Stripe](https://stripe.com/). Payment functionality was tested using the Stripe development payment card details:

![](assets/images/card-payment.jpg)

Following the successful completion of a customer order the user is directed to the 'checkout success' page, which displays the order number and delivery details.

![](assets/images/checkout-success.jpg)

If the payment can not be completed, the form does not submit, and an error message is displayed.

![](assets/images/card-invalid.jpg)

### User profile

A logged-in user can use the `my account` dropdown to select a link to the `My Profile` which contains their account details.

The profile page can be used to update default shipping/billing address and contact information.

![](assets/images/my-profile-customer-details.jpg)

A list of all the orders previously made by the user are also displayed.

![](assets/images/my-profile-order-history.jpg)

### Admin

The admin section of this website allows a logged-in superuser to update the product models from the front end.

#### **Product management**

Superusers can edit/add/remov products using edit/delete links and also from the `Product Management` page that can be accessed from the `My Account` dropdown.

![](assets/images/product-management.jpg)

---
## Technologies Used

I have used several technologies that have enabled this design to work:

- [Django](https://www.djangoproject.com/)
    - Django is the framework that has been used to build the website.
- [Python](https://www.python.org/)
    - Python is the programming language used to write all of the backend code.
- [Bootstrap](https://getbootstrap.com/)
    - Used for creating responsive design.
- [Google Fonts](https://fonts.google.com/)
    - Used to obtain the fonts used throughout the website
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used on the high scores and rules pages.
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness across the project.
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy my application.
- [Pep8](http://pep8online.com/)
    - Used to test my code for any issues or errors.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate all HTML code written and used in this webpage.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate all CSS code written and used in this webpage.
- [JSHint](https://jshint.com/)
    - Used to validate JS code
- [AmIResponsive](http://ami.responsivedesign.is/)
    - Used to generate responsive image used in README file.
- [SQLite](https://www.sqlite.org/index.html)
    - SQLite used to run database tests locally.
- [ElephantSQL](https://www.elephantsql.com/)
    - ElephantSQL relational database used when deploying to Heroku to store the data for all models.
- [AWS](https://aws.amazon.com/)
    - Amazon AWS S3 to store all media files.

---
## Deployment

The master branch of this repository has been used for the deployed version of this application.

### Using Github & Gitpod

To deploy the Django application, I had to use the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- To create a Gitpod workspace you then need to click `Gitpod`, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than create a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.

### Stripe

Stripe was used for setting up payments for the e-commerce store. This required creating a Stripe account and using the [documentation](https://stripe.com/docs/payments/online-payments) provided to add the relevant HTML, python & JS code to the project.

### AWS static and media storage

All static and media files are stored in the cloud using Amazon AWS S3; i have used the same boutique-ado project bucket, user group and user that can access this site and the relevant files. 

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial and [Django Blog cheatsheat](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed. A `Procfile` is also required that specifies the commands that are executed by the app on startup. 

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; if you do not already have an account then you will need to create one.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

*Heroku Settings*
You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.
- In the Settings tab, click on `Reveal Config Vars`. The variables that need to be set are:

![](assets/images/config-variables.jpg)

*Heroku Deployment using website*
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    1. Click on the `Deploy` tab and choose `Github-Connect to Github`.
    2. Enter the GitHub repository name and click on `Search`.
    3. Choose the correct repository for your application and click on `Connect`.
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the `Deploy Branch` button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should see the below `View` button, click this to open your application.

*Heroku CLI deployment*
Whilst building this project there was a security breach on Heroku which caused issues with deployment via their website. Due to this, I had to add a `runtime.txt` file specifying which version of Python to build the app with and used the following commands to push the code to Heroku:

1. Login to Heroku via the CLI using `heroku login -i`
2. Enter your email and password
3. Connect to the Heroku git remote using the `heroku git:remote -a YOURAPPNAME`
4. Push to the Heroku git remote using `git push heroku main`
---
## Credits

Due to time constraints and to meet the submission deadlines a large part of this poject has used the Code insitute 
[Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) walkthrough project.
