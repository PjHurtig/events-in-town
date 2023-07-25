# Events in Town

## Events in Town is a webite that shows the user time and place of concerts and other events in The county of Jämtland, Sweden

![responsive](https://i.imgur.com/3HCf0OP.png)>

Users can carry out the following actions on the site:

1. See added events
2. Sort events by upcoming and date added
3. Create an account and log in
4. Add events
5. Edit their added events
6. Delete their added events

The project is live here: [Events-in-Town](https://events-in-town-b0051e4a58da.herokuapp.com/)

___

## Table of Contents

- [Events in Town](#events-in-town)
  - [Events in Town is a webite that shows the user time and place of concerts and other events in The county of Jämtland, Sweden](#events-in-town-is-a-webite-that-shows-the-user-time-and-place-of-concerts-and-other-events-in-the-county-of-jämtland-sweden)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Profile](#user-profile)
    - [User Navigation](#user-navigation)
    - [Site Administration](#site-administration)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Future User Stories](#future-user-stories)
    - [Colour Scheme](#colour-scheme)
  - [Planning](#planning)
    - [Methodology](#methodology)
    - [Models](#models)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [General](#general)
    - [Home Page](#home-page)
    - [My Events Page](#my-events-page)
    - [Sorted Events](#sorted-events)
    - [Add Event Page](#add-event-page)
    - [Edit Event Page](#edit-event-page)
    - [Delete Event Page](#delete-event-page)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
  - [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Accessibility](#accessibility)
    - [Device Testing](#device-testing)
      - [Phones](#phones)
      - [Computers](#computers)
    - [Browser Testing](#browser-testing)
    - [Manual Testing](#manual-testing)
      - [base.html](#basehtml)
      - [index.html](#indexhtml)
      - [post\_detail.html](#post_detailhtml)
      - [sorted\_posts.html](#sorted_postshtml)
      - [my\_posts.html](#my_postshtml)
      - [update\_post.html](#update_posthtml)
      - [delete\_posts.html](#delete_postshtml)
      - [other](#other)
    - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credit](#credit)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)

## User Experience (UX)

### User Profile

- As a User I can create an account so that i can contribute to the site
- As a User I can view all active events so that i can see what events are available
- As a User I can add event to the event list so that I can contribute to the completeness of the event list
- As a user I can update and delete my posts so that i can keep the information up to date and remove unwanted events

### User Navigation

- As a site user i can navigate around the site so i can find the content im looking for
- As a site user i can click on events to take me to the full event page with information

### Site Administration

### Project Goals

The goal is to have a communtiy driven site where people can find and add information about local events.

### User Stories

- As a User I can create an account so that i can contribute to the site
- As a User I can view all active events so that i can see what events are available
- As a User I can add event to the event list so that I can contribute to the completeness of the event list
- As a user I can update and delete my posts so that i can keep the information up to date and remove unwanted events
- As a site user i can navigate around the site so i can find the content im looking for
- As a site user i can click on events to take me to the full event page with information

### Future User Stories

- As a site user i can see the location of my event via the google maps API

### Colour Scheme

The main colors are a nice, simple combination of dark and light.

![alt](https://i.imgur.com/jDB1PTk.png)

## Planning

### Methodology

The project was planned and implemented following agile methodology principles. GitHub Projects was used to manage and document this process.

The GitHub project can be viewed here: [Events in Town Project](https://github.com/users/PjHurtig/projects/6)

Following MoSCoW Priortisation principles, each User Story was assigned a tag from one of the following:

- Must Have
- Should Have
- Could Have
- Won't Have

### Models

the main model is the Post model that is the basis for the event post functionality.

### Wireframes

Initial wireframe for mobile with [Balsamiq](https://balsamiq)

![wireframe](https://i.imgur.com/SVeXOnY.png)

## Features

### General

- the website is responsive and looks good across mobile devices and desktop
- The website has a consistent and responsive navigation bar on all pages
- color scheme is consistent across the page, with buttons in colors that represents their function
- The website has a responsive footer with social media links and a back-to-top link

### Home Page

- The home page features the last added and the next upcoming event that is filtered for events that has already passed.

### My Events Page

- Displays all of the logged in users posted events
  
### Sorted Events

- Displays all events that has not passed and can be sorted by event date or date added in ascending or descending order

### Add Event Page

- Displays a form for adding an event with all the neccessary fields and tells the user if something required is missing or is filled out incorectly

### Edit Event Page

- Displays the form with prepopulated fields that the user can update and save or cancel

### Delete Event Page

- A page that asks the user if they want to delete event

### Register Page

- Displays a form for account creation with username, password confirmation and optional email. The form tells the user if something required is missing or is filled out incorectly or not up to standard

### Login Page

- Displays a form for a user to log in to their account

### Logout Page

- Confirms that the user want to log out

## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python

### Frameworks, Libraries and Programmes

- [Balsamiq](https://balsamiq.com/): was used to create wireframes.
- [Font Awesome](https://fontawesome.com/): was used to add social media icons.
- [Unsplash](https://www.unsplash.com/): was used to find placeholder image for the project.
- [Django](https://www.djangoproject.com/): was the framework used.
- [Bootstrap 5](https://getbootstrap.com/): the CSS framework used to make the site responsive.
- [Cloudinary](https://cloudinary.com/): was used to store static and media files.
- [Codeanywhere](https://codeanywhere.com/): was used to write, commit and to push the code to Github.
- [Github](https://github.com/): for version control.
- [Heroku](https://dashboard.heroku.com/login): was used to host and deploy the finished project.
- [ElephantSQL](https://www.elephantsql.com/): the SQL database used in production.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): was used throughout the project to check responsiveness and debug.
- [W3C Markup Validator](https://validator.w3.org/): was used throughout the project to validate HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): was used throughout the project to validate CSS code.
- [CI Python Linter](https://pep8ci.herokuapp.com/): was used to validate python code.
- [JSHint](https://jshint.com/): this was used to validate Javascript code.
- [Responsive Design Checker](https://www.responsivedesignchecker.com/): this was used to check responsiveness on various device sizes.
- [Am I Respsonsive?](https://ui.dev/amiresponsive): this was used to create an image to show how the site looks on different device sizes for this README file.

## Testing

### Testing User Stories

As a User I can create an account so that i can contribute to the site

- The user is able to click sig up in the main navigation and from the form add their details to create an account

As a User I can view all active events so that i can see what events are available

- Via the main navigation the user can klick view events and from that page they can sort all the available events

As a User I can add event to the event list so that I can contribute to the completeness of the event list

- The logged in user can via the dropdown "manage events" in the navigation, choose to add an event that they think is missing from the site

As a user I can update and delete my posts so that i can keep the information up to date and remove unwanted events

- The logged in user can via the events page or the "My Events" in the "Manage Events"-dropdown click on "update" to change detail or "delete" to remove the post

As a site user i can navigate around the site so i can find the content im looking for

- The navigation bar changes depending on if the user is logged in or not,  where the logged in user has acces to more functionality and a user that is not logged in has relevant links in the navigation to view events or create an accout/log in

As a site user i can click on events to take me to the full event page with information

- When clicking on the event image, event title or the event link, the user is redirected to that events full page

### Code Validation

Unresolved python errors:
AUTH_PASSWORD_VALIDATORS lines are too long in the way setting.py is configured from the start

### Accessibility

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to check the accessibility of the site and to see if there were any issues.

Lighthouse Results:

index:

![index](https://i.imgur.com/KiMO4T0.png)

sorted_posts:

![sorted_posts](https://i.imgur.com/Od1PODV.png)

post_detail:

![post_detail](https://i.imgur.com/OUDlpSN.png)

### Device Testing

I have successfully tested the site on these devices available to me

#### Phones

Huawei mate 20 pro

- Chrome
- Firefox

Samsung s8

- Chrome
- Firefox

#### Computers

lenovo ideapad

- Chrome
- Firefox
- Edge
- Opera

Lenovo thinkbook

- Firefox
- Edge

### Browser Testing

- Chrome
- Firefox
- Edge
- Opera

### Manual Testing

These functions have been successfully tested:

#### base.html

- Logo | when clicked the user is directed to the home page
- Logged in/out user| when a user is logged in the navigation bar shows "Manage Posts" and "Logout" instead of "Sign Up" and "Log In" as it does for unauthenticated users
- Responsive navigation | The menu collapses to a clickable burger icon on smaller screens
- Link: Sign Up | Takes the user to the sign up page
- Link: My Events | Takes the user to a list of their events
- Link: View Events | Takes the user to the sorted events page
- Link: Add Event | Takes the user to the Add Event page
- Link: Log In | Takes the user to the Log In page
- Link: Log Out | Takes the user to the Log Out page
- Footer Link: Social Media | Takes the user to the social media sites in a new tab
- Footer Link: Back to Top | Scrolls the page back to the top

#### index.html

- Upcoming events | Shows the next upcoming event based on the event start and filters out events that has passed
- Latest events | Shows the next upcoming event based on the date and time added
-The about text is truncated and "read more" takes the user to the event page

#### post_detail.html

- displays the event in full, if user is logged in and is the author of the event there is update and delete buttons as well

#### sorted_posts.html

- Shows all posts that the date and time has not yet passed
- If event has the status "Cancelled" there is a visual indication of this
- Links let the user sort the posts

#### my_posts.html

- Displays a list of events that the logged in user has added
- there are "update" and "delete" buttons available in the list for easier managment

#### update_post.html

- Prepopulated fields of the post that the user can edit and save
- Cancel button takes the user back to "my events"

#### delete_posts.html

- Confirms deletion
- Deletes the event if "delete" button is pressed
- Cancel button takes the user back to the event page

#### other

- if there are no posts, a card is displayed with information

Logged in user sees:
![no posts](https://i.imgur.com/RlwYbNE.png)

Unauthorized user sees:
![no posts](https://i.imgur.com/Ylcf0DU.png)

### Bugs

in the console when a page that does not display an alert message, this error came up.

![typerror](https://i.imgur.com/6sPlY6m.png)

it had to do with the setTimeout function in the javascript code for closing alert messages. I first tried to fix it with an eventlistener for the DOM but the error still appeared.

Together with my mentor Anthonio we solved it this way:

![fix](https://i.imgur.com/mNkPx4i.png)

## Deployment

Deployment to Heroku was completed using the following steps:

1. Open and login to [Heroku](https://id.heroku.com/login).
2. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu.
3. Enter the App name, choose a region, then click 'Create app'.
4. Navigate to the 'Settings' tab.
5. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
6. Add config vars using the 'KEY' and 'VALUE' pairs from env.py.
7. Add additional config var of key: PORT, value: 8000
8. Navigate to the 'Deploy' tab.
9. Within 'Deploy', navigate to 'Deployment method'.
10. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub'
11. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
12. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
13. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method.
14. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
15. Click 'View' to see the deployed app.

## Credit

### Content

- Content in some events from wikipedia
  
### Media

- Favicon made by me
- Images in events are from unsplash or wikipedia

### Code

- README.md: the outline and deployment information for this readme is based on Orlagh Sweeney's PP4 readme found [here](https://github.com/orlagh-sweeney/the-big-review/blob/main/README.md)
- Reverse lazy, info from [fullstackpython](https://www.fullstackpython.com/django-urls-reverse-lazy-examples.html)
- get_context_data for views, info from [stackoverflow](https://stackoverflow.com/a/36950584)
- Truncate text info from [djangoproject](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
- Navbar code from [getbootstrap](https://getbootstrap.com/docs/5.0/components/navbar/)
- info about sorting from: [stackoverflow](https://stackoverflow.com/questions/6262629/sorting-through-request-get-in-django)
- info about timezones from: [djangoproject](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/)
- initial code for add events, my events, update and delete views from [AliOKeeffe's](https://github.com/AliOKeeffe) PP4 project found [here](https://github.com/AliOKeeffe/PP4_My_Meal_Planner)
- pagination and initial post model from django-blog walkthrough project
