# Retry - A second-hand online store

# Portfolio Project 5

**Retry** is a online store provide second-hand product with online payment.\
User can purchase items from our collaborator and use stripe to complete online payment.\
They can also sign up to track their previous order payment and product status.

**Active website**: https://ci-portfolio-project-5.herokuapp.com/ \
**Git Repository**: https://github.com/cloki0610/CI-Portfolio-Project-5
![screen-capture](readme-img/screenshot_sc.png)

## **Table of Contents**

<hr>

- [User Experience Design](#User-Experience-Design)
- [Feature](#Feature)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Technologies](#Technologies)
- [Credits](#Credits)

<br>

## **User Experience Design**

### **The Strategy Plane**

<hr>

The project is about to begin a business based on social media and community that cooperate with a different collaborator from organizations, groups, or individuals who want to sell their product and unwanted item in their name or anonymously. Each collaborator will work with us for a maximum of two months to sell their stuff products on our e-commerce platform. Our team will provide an online e-commerce platform, support their social media promotion, and deliver if collaborator needed in some special situation.

Based on the business strategy the e-commerce platform in the project will provide a solution to let users search and filter the products, store items into their shopping cart, create a new order, and complete the online payment. They could also sign up their account to track their previous order, manage their payment details, and directly connect with website admin through the platform. The application should also have responsive design and have a nice layout on mobile and desktop browser.

<br>

#### **Site Goal**

<hr>

- Provide a full functional e-commerce platform with online payment.
- Provide user validation to let user create their own account with personal profile.
- Provide review and 1:1 communicate platform to review and discuss about their order.
- Provide a report page to unauthenticated user to report the product which have problem.
- Provide a pages to let all user to subscribe news letter and submit contact details.

<br>

### **Scope Plane**

<hr>

Planned Features the website should have:

- Responsive Design
- Navigation Bar
- Category page to filter the type of contents
- Sort option
- Search bar to search specific item(s)
- Paginator to split product list to different pages
- Shopping cart
- Payment method
- User validation
- Personal user profile
- Order review
- Comment section in review page
- Contact form
- News letter subscription

<br>

### **Structure Plane**

<hr>

User story:

> As a User, I want to be able to view a list of products, so that I can add my interested item to my cart.

Acceptance Criteria:

- The product page should display full list of product, and display some detail of these product with friendly user interface.

Implementation:

- User can click the link on landing page or nav bar to visit the full item list.
- The product list split to few pages divide by the paginator.
- Each item display their name, price, category with product image as a card component.
- User can click the card to visit detail page to add item to card or report the product if needed.

<br>

User story:

> As a User, I want to be able to view a specific category of products, so that I can easily find my interested products.

Acceptance Criteria:

- User should able to filter the product list by category through click a link or button to view the list of item in specific category.

Implementation:

- User can click the link on the nav bar to view the product list filter by category.
- The product list split to few pages divide by the paginator as the full product list.
- The filter parameter will save in the context for the paginator links.

<br>

User story:

> As a User, I want to be able to view individual product details, so that I can identify all information about the product.

Acceptance Criteria:

- When user click on the relavent link, they should be able to view the full detail of product with product image.

Implementation:

- When user click on the link on the product card, they will able to visit the product detail on product_detail template.
- The product detail page will display the full detail of products, with quantity form, add product button, return link, and a lint to report page.

<br>

User story:

> As a User, I want to be able to view the total of my purchases at any time, so that I can know how much I would pay.

Acceptance Criteria:

- User should able to see their current total cost on every page.

Implementation:

- On the shopping cart navbar link, the current total cost will display below the 'shopping cart' text.
- On the mobile version, the totoal cost will display with the link in the same line.
- There also have a badge to display how many type of item customer purchase if their cart have item.

<br>

User story:

> As a User, I want to be able to register my own account, so that I can be able to use my own profile to store my personal information.

Acceptance Criteria:

- User should be able to register a new account to use some feature only provide to authenticated user.

Implementation:

- All feature related to user authentication are provide by allauth library.
- The template style by bootstrap 5 and the folder are place under /templates folder.
- The 'Sign Up' link show on the account sub-navbar.

<br>

User story:

> As a Member/Admin, I want to be able to login or logout, so that I can access my profile, and purchase as of my own identity.

Acceptance Criteria:

- User should be able to login and logout to use the services as quest or registered user base on their requirement.

Implementation:

- All feature related to user authentication are provide by allauth library.
- The template style by bootstrap 5 and the folder are place under /templates folder.
- The 'Sign In' and 'Sign Out' link show on the account sub-navbar, if user successfully login, the sign out link will display and the sign in link will hide and vice versa.

<br>

User story:

> As a Member/Admin, I want to be able to recover my password in case I forget it, so that I can recover access to my account.

Acceptance Criteria:

- User should be able to recover their password by input a valid e-mail address, and they should able to receive a email to set new account to access their account.

Implementation:

- All feature related to user authentication are provide by allauth library.
- The template style by bootstrap 5 and the folder are place under /templates folder.
- The link display on the sign in template, there is the only way user can click to visit the password reset page to use this feature.

<br>

User story:

> As a Member/Admin, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.

Acceptance Criteria:

- User and admin should be able to receive a e-mail after registering, and only allow to login after confirmation.

Implementation:

- When user register a new account, the function provide by allauth library will send a e-mail to user.
- E-mail account provided by google, and the information about the e-mail and the pass secret key store in the eny.py and heroku.

<br>

User story:

> As a Member/Admin, I want to be able to have a personalized user profile, so that I can check my personal order history, order confirmations, and save my payment information.

Acceptance Criteria:

- User should able to visit a profile page to check their profile details and order history.

Implementation:

- A userprofile data model create in profiles application.
- Some view to handle all of the get and post method to visit the profile page and post data to manage their record.
- Templates style by customer css and bootstrap 5 style the user interface.
- User can edit and submit their profile on the left side of the page, and check their order history on the right side.
- Below the profile form, there are button to submit the form and a link to remove the account if user is not superuser

<br>

User story:

> As a Member, I want to be able to remove my account so that I can feel free to be involved in the community and secure my information if needed.

Acceptance Criteria:

- Authorized user should about to click the delete account on the profile page to remove their account.

Implementation:

- Below the profile form, if user is not superuser they will see the 'delete account' button next to the submit buttom.
- Once they click the button, they will visit a confirm page with some warning message.
- They can also click return button to return to profile page.
- Once they click the delete button, a modal component will pop up for the final confirm.
- User can close the modal and return to the website, but once user click that button, they will redirect to landing page and their account will be removed.
- Related message should show up once the action is made.

<br>

User story:

> As a Member, I want to be able to create/edit a review to my previous order, so that I can directly communicate with the store owner.

Acceptance Criteria:

- User should be able to create a order review to provide some feedback about their order.
- The review page should have a section to show all comment about the review.
- Only customer who place the order and the superuser allow to visit the review record.

Implementation:

- User can create a new review in profile page, or visit the review page if record exist.
- In the review page, they can see the details of their review, or click update/delete link to manage their record.
- User can leave comment on the review page by submit the comment form.
- All comment will display on the right side in the review page.

<br>

User story:

> As a User, I want to be able to sort the list of available products, so that I can find the products by category, price or by name.

Acceptance Criteria:

- User should be able to sort the product list to easily search the product they need.

Implementation:

- The sort select box place on top of the product list, in the same line with result details and paginator.
- User can sort the result by name, price and category name.
- The parameter will save in the context for the paginator links.

<br>

User story:

> As a User, I want to be able to sort a specific category of product, so that I can find the products by price or by name.

Acceptance Criteria:

- After click the link to filter the result by category, user should still about to sort the result by price or by name.

Implementation:

- The sort select box still place on the same place as before after filter the result.
- The parameter will save in the context for the paginator links.

<br>

User story:

> As a User, I want to be able to search for a product by name or description, so that I can find my interested product easily.

Acceptance Criteria:

- User should able to search the product by name or description and get the result to find the product they need.

Implementation:

- The search bar create by a input box and submit button.
- The search bar place on the sub menu of the navbar in desktop version.
- The search bar place below the title in mobile version.
- User can input some text to search the product by product name and description.
- If user submit the form with blank input, they will see some warning message.

<br>

User story:

> As a User, I want to be able to see what I've searched for and the number of results, so that I can quickly decide whether the product I want is available.

Acceptance Criteria:

- User should able to see the number of search result on the product page.

Implementation:

- The number of result display on the same line with the sorting box and the paginator.

<br>

User story:

> As a User, I want to be able to select the quantity of a product when purchasing it, so that I can ensure I always select the correct product and quantity.

Acceptance Criteria:

- User should able to see the current item quantity they select, and able to change the item quantity by input or button.

Implementation:

- Add two button around the input field to change the quantity.
- Add javascript to make these new button functional.
- If selected quantity less than 1 or more than 99, related button will be disable.

<br>

User story:

> As a User, I want to be able to view all selected items in my shopping cart, so that I can know the total cost of purchase and the items I will receive.

Acceptance Criteria:

- User should able to view a full list of item they have added to their shopping cart.

Implementation:

- Create a context file to create a dictionary to store the added item.
- When user click the link on the navbar, they will see a complete list of the items they added.
- The shopping card page should have button to return to shop, ajust button and to payment page.

<br>

User story:

> As a User, I want to be able to adjust the quantity of items in my shopping cart, so that I can make edit my order before checkout.

Acceptance Criteria:

- User should able to adjust every item they added to the shopping cart in the shopping cart page.

Implementation:

- Reuse the existed quantity form and javascript.
- Edit the exist javascript to handle all buttons in the shopping cart page.
- If quantity is zero, the item will be remove from the shopping cart.

<br>

User story:

> As a User, I want to be able to enter my payment information on checkout page, so that I can check out with no hassles.

Acceptance Criteria:

- User should be able to enter their payment information on the checkout page to submit the data about the payment and delivery informations.

Implementation:

- On the left side in the checkout page, user can submit a form to provide the payment detail.
- If the form is valid, the payment information will send to stripe by webhook and the order record will store in database.
- If user is authorized, they will allow to press a checkbox to save their payment information to save their input to their profile.

<br>

User story:

> As a User, I want to be able to view an order confirmation after checkout, so that I can verify that I haven't made any mistakes.

Acceptance Criteria:

- After a successful checkout, user should be able to see the record about their successful purchase.

Implementation:

- A Order and order item record will be create to store all purchase record.
- After checkout, user should be redirect to the checkout_success page.
- The page will get the order record from database and display on template.

<br>

User story:

> As a User, I want to be able to receive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records.

Acceptance Criteria:

- User should receive email after checkout with order details.

Implementation:

- The email content created and store in checkout application's template file.
- Once the purchase is successfully complete, the stripe webhook will send a email from my google account.

<br>

User story:

> As an Admin, I want to be able to add a product, so that I can add new items to my store.

Acceptance Criteria:

- Website admin should able to submit a valid form to add a new product for sale.

Implementation:

- If user is not superuser, access will be denied and redirect to home page.
- If input is invaild, some message will show up.
- If input is valid, user will be redirect to new product's product detail page.
- The link to add product will display in the sub menu of 'account' and only show up when user is a superuser.

<br>

User story:

> As an Admin, I want to be able to update my products, so that I can change product prices, descriptions, images, and other product criteria.

Acceptance Criteria:

- Website admin should able to submit a valid form to update a exist product.

Implementation:

- The page is familiar with the add product page.
- If user is not superuser, access will be denied and redirect to home page.
- If input is invaild, some message will show up.
- If input is valid, user will be redirect to new product's product detail page.
- The link to update product will display in the product detail page and on the bottom of the product card component
- The button only show up when user is a superuser.

<br>

User story:

> As an Admin, I want to be able to delete a product, so that I can remove items that are no longer for sale.

Acceptance Criteria:

- Website admin should able to delete a exist product to let customer know its not for sale anymore.

Implementation:

- When admin click the delete button, they will rediect to a confirm page.
- Admin can click the link to return to product detail page, or press delete button to remove product.
- The link to update product will display in the product detail page and on the bottom of the product card component.
- The button only show up when user is a superuser.

<br>

User story:

> As a User, I want to be able to report a problem product, so that the shop owner can know if there is some problem with their products.

Acceptance Criteria:

- User should able to submit a form to report a product with some problem, whatever authorized or not.

Implementation:

- Use can submit a report data to the database to report a product.
- The link to the report form are in the product_detail page.

<br>

User story:

> As a User, I want to be able to leave my contact information and comment to the store owner, so that I can leave my feeling of the shop and try to connect with the shop owner personally.

Acceptance Criteria:

- User should able to submit a form with some data to allow admin to contact user out of the website.

Implementation:

- A contact data model created to store the contact details.
- A form can allow user to submit data about their contact details.
- The link to the contact form are in the about submenu in the navbar.

<br>

User story:

> As an Admin, I want to view details of the customer's contact detail and report, so that I can easily know customer's response.

Acceptance Criteria:

- Admin should able to view a list of contact detail and report to view all data in these table.

Implementation:

- Contact detail page display the full details and style with bootstrap and jquery animation.
- Report list style as a bootstrap component, and divide by paginator.
- Report list provide a toggle button to mark the report as checked or not.
- Link of these list are display in the sub menu of the account menu in navbar.

<br>

User story:

> As a User, I want to be able to leave my e-mail address to the store owner, so that I can recieve their news letter to get more information about their latest products or activities.

Acceptance Criteria:

- User should able to submit their e-mail address to the admin for subscribe the newsletter for the latest information.

Implementation:

- A simple form with a field can allow user to send their email address to the database.
- The link to the newsletter page will place in the sub menu in the about menu.

<br>

### **Skeleton Plane**

<hr>

#### **Wireframes**

#### **Database Design**

#### **Security**

With Heroku's config var feature, all sensitive keys like stripe and AWS secret key were stored in local env.py file are now stored in the Heroku server to prevent unwanted connections to the database or cloud service.

The project also use Django allauth to set up a user authorization system to provide restricted access to certain features on the website that are not intended for unauthorized users. User need a valid e-mail to receive confirmation e-mail to confirm their e-mail to login to the website.

All image file uploads from the user should store and be protected in AWS S3 bucket, but there are limit of the usage because it is still using AWS free tier service.

### **Surface Plane**

<hr>

#### **Color Sheme**

Background color: #fafafa\
font color: #3a3a3a\
Navbar background color: #075E31\
Navbar font color: #FFF1CE\
Navbar icon color: #D29D2B

#### **Typography**

#### **Differences to Design**

## **Feature**

### **Existing Features**

<hr>

- Authentication system provided by allauth library.
- Admin panel provided by Django framework with customized search and filter function.
- Customer user profile.
- Page for Error 404.
- Page for Error 500.

### **Features Left to Implement**

<hr>

## **Testing**

### Code Validation

<hr>

### Manual test

<hr>

### Automated test

<hr>

### Issue found and solved

<hr>

<br>

### Unsolved Issue

<hr>

## **Deployment**

### **Create a new project**

<hr>

## **Technologies**

### **Language**

<hr>

- HTML
- CSS
- JavaScript
- Python

### **Libraries**

- PostgreSQL
- Bootstrap 5
- JQuery
- Google Fonts
- Font Awsome
- Stripe

and those python libraries install with [requirements.txt](requirements.txt):

- PostgreSQL
- asgiref
- dj-database-url
- django-allauth
- django-crispyforms
- boto3 and django-storages
- gunicorn
- psycopg2
- django-countries
- Pillow
- stripe

### **Project manage and deployment**

- GitHub
- Git
- Heroku

### **Testing**

- Google DevTool
- WAVE Web Accessibility Evaluation Tool
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
- [PEP8 online](http://pep8online.com/)

### **Documentation**

- Balsamiq Wireframes
- DbVisualizer

## **Credits**

### **Code**

- [Code Institute Buotique Ado walk-through project](https://github.com/cloki0610/boutique_ado_Walkthrough)

  I use quite a lot of code in my clone of the code institute project with some change to complete the purchase and payment flow.

- [How to create a UserProfile form in Django with first_name, last_name modifications?](https://stackoverflow.com/questions/1727564/how-to-create-a-userprofile-form-in-django-with-first-name-last-name-modificati)

  To add the first name, last name and email to the profile form and edit them in user interface, I find this solution with some improvement to fulfill the requirement.

- [My Project 4](https://github.com/cloki0610/CI-Portfolio-Project-4)

  I reuse some code from my previous project to create the view as class-based view, and complete my test cases of my web application.
  <hr>

## **Media**

- Pexels

  All images come from and copyrighted by Pexels, the images will be remove or replaced if their policy have changed.

- Flaticon

  The no image icon come from this website.

### **Acknowledgment**

<hr>
