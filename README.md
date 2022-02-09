# Retry - A second-hand online store
# Portfolio Project 5
Retry is a online store provide second-hand product with online payment.\
User can purchase items from our collaborator and use stripe to complete online payment.\
They can also sign up to track their previous order payment and product status.\
You can click [here]() to the living website.\
Active website: 


## **Table of Contents**
<hr>

* [User Experience Design](#User-Experience-Design)
* [Feature](#Feature)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Technologies](#Technologies)
* [Credits](#Credits)

<br>

## **User Experience Design**
### **The Strategy Plane**
<hr>

The project is about to begin a business based on social media and community that cooperate with a different collaborator from organizations, groups, or individuals who want to sell their product and unwanted item in their name or anonymously. Each collaborator will work with us for a maximum of two months to sell their stuff products on our e-commerce platform. Our team will provide an online e-commerce platform, support their social media promotion, and deliver if collaborator needed in some special situation.

Based on the business strategy the e-commerce platform in the project will provide a solution to let users search and filter the products, store items into their shopping cart, create a new order, and complete the online payment. They could also sign up their account to track their previous order and manage their payment details. The application should have responsive design and have a nice layout on mobile and desktop browser.

<br>

#### **Site Goal**
<hr>

 - Provide a full functional e-commerce platform with online payment. <br>
 - Provide user validation to let user create their own account with personal profile. <br>
 - User will be allowed to write a review to their previous order.
 - User will be allowed to  report the product which have problem.
 - User will get the core information about our business and previous collaborators.

<br>

#### **User Stories**
<hr>

 
<br>

### **Scope Plane**
<hr>

Planned Features the website should have:
 - Responsive Design
 - Navigation Bar
 - Category page to filter the type of contents
 - Search bar to search specific item(s)
 - User validation
 - Shopping cart
 - Payment method
 - Order review
 - Contact form

<br>

### **Structure Plane**
<hr>
1. As a User, I want to be able to view a list of products, so that I can add my interested item to my cart.
2. As a User, I want to be able to view a specific category of products, so that I can easily find my interested products.
3. As a User, I want to be able to view individual product details, so that I can identify all information about the product.
4. As a User, I want to be able to view the total of my purchases at any time, so that I can know how much I would pay.
5. As a User, I want to be able to register my own account, so that I can be able to use my own profile to store my personal information.
6. As a Member/Admin, I want to be able to login or logout, so that I can access my profile, and purchase as of my own identity.
7. As a Member/Admin, I want to be able to recover my password in case I forget it, so that I can recover access to my account.
8. As a Member/Admin, I want to be able to receive an email confirmation after registering, so that I can verify that my account registration was successful.
9. As a Member/Admin, I want to be able to have a personalized user profile, so that I can check my personal order history, order confirmations, and save my payment information.
10. As a Member, I want to be able to remove my account so that I can feel free to be involved in the community and secure my information if needed.
11. As a Member, I want to be able to create/edit a review to my previous order, so that I can directly communicate with the store owner.
12. As a User, I want to be able to sort the list of available products, so that I can find the products by category, price or by name.
13. As a User, I want to be able to sort a specific category of product, so that I can find the products by price or by name.
14. As a User, I want to be able to search for a product by name or description, so that I can find my interested product easily.
15. As a User, I want to be able to see what I've searched for and the number of results, so that I can quickly decide whether the product I want is available.
16. As a User, I want to be able to select the quantity of a product when purchasing it, so that I can ensure I always select the correct product and quantity.
17. As a User, I want to be able to view all selected items in my shopping cart, so that I can know the total cost of purchase and the items I will receive.
18. As a User, I want to be able to adjust the quantity of items in my shopping cart, so that I can make edit my order before checkout.
19. As a User, I want to be able to enter my payment information on checkout page, so that I can check out with no hassles.
20. As a User, I want to be able to view an order confirmation after checkout, so that I can verify that I haven't made any mistakes.
21. As a User, I want to be able to receive an email confirmation after checking out, so that I can keep the confirmation of what I've purchased for my records.
22. As an Admin, I want to be able to add a product, so that I can add new items to my store.
23. As an Admin, I want to be able to update my products, so that I can change product prices, descriptions, images, and other product criteria.
24. As an Admin, I want to be able to delete a product, so that I can remove items that are no longer for sale.
25. As a User, I want to be able to report a problem product, so that the shop owner can know if there is some problem with their products.
26. As a User, I want to be able to leave my contact information and comment to the store owner, so that I can leave my feeling of the shop and try to connect with the shop owner personally.
27. As a User, I want to be able to view some descriptions about the store and their partner, so that I can get to know more about store owner and their partners.

### **Skeleton Plane**
<hr>

#### **Wireframes**


#### **Database Design**


#### **Security**
With Heroku's config var feature, all sensitive keys that were stored in env.py are now stored in the Heroku server to prevent unwanted connections to the database or cloud service.

This project also uses Django allauth to set up a user authorization system to provide restricted access to certain features on the website that are not intended for unauthorized users.

All image file uploads from the user should store and be protected in AWS S3 storage.

### **Surface Plane**
<hr>

#### **Color Sheme**
Background color: \
font color: \
Nav bar background color: \
Nav bar font color: \
standard border color: \
Color for represent fiction category: \
Color for represent non-Fiction category: \
Color for represent Lifestyle category: 

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

  and those python libraries install with [requirements.txt](requirements.txt):
 - PostgreSQL
 - asgiref
 - dj-database-url
 - django-allauth
 - django-crispyforms
 - gunicorn
 - psycopg2

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
<hr>

### **Acknowledgment**
<hr>
