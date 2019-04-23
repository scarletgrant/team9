# Dublin Bikes Availability checker
**Team9**

Software Engineering Project

Computer Science Conversion Program

**1. Introduction**

The DublinBikes Project is part of the Software Engineering module of the Computer Science conversion course. It is the first group project of the program where the students explore Scrum and agile development methodologies.

Software Engineering (COMP 30830) is a core module on the MSc Computer Science (Conversion) and Higher Diploma in Computer Science Programmes. Software engineering focuses on the processes and techniques fundamental to the creation of reliable, software systems. The module will cover the core concepts and tools used in software engineering. There is a focus on developing sound fundamentals in the areas of requirements engineering, process models, software design, architecture, design patterns and software testing.

The Team has further specified the requirements in several versions of Software Requirement Specifications that were confirmed with the Product Owner. Most of them are mentioned in this report. For the changelog of the requirements and the latest agreed version please refer to the following Appendix:


**1.1 Product Scope**

The BikePlanner Application is a solution to remove all possible friction of biking with DublinBikes, the shared bike scheme run by Dublin City Council. It is build to be a potential extension of the website www.dublinbikes.com. The Application could however be customized and delivered to any other bike sharing scheme provider that offers similar bike data services.

The application helps users finding the nearest bike station to get and return a bike from the bike scheme. It includes a function to predict the availability. This prediction function is delivered as beta feature in version 1 of the application.

The app aims to help Dublin Bike users with the following benefits as provided by the client: 

•Find the best station with available bikes to start a journey 

•Find the best station with free spaces to return the bike 

•Should display relevant and useful information learned from recent occupancy trends 

•Incorporate weather information, as it affects the occupancy 

•Include other sources of information


**2. Overall description**

**2.1 Product Perspective**

The BikePlanner is an independent, standalone application that collects data from the API’s of JCDecaux and DarkSky to show bike stations, availability and weather. A prediction module analyses the gathered data from the API’s. The site consists of one single main page that displays all functionalities.

There are many applications out there in the market that show the nearest bike stations. Yet, the quality of the user interface is limited and they do not provide prediction features.


**2.2 Product Functions**

The application delivers the following functionalities to the user:

● Find nearest bike at desired/current location in least amount of clicks;

● Find nearest dock at desired/current destination in least amount of clicks;

● Show forecast of bike availability (at given datetime and location);

● Show availability for card payments at given location;

● Show weather-forecast upon opening the app to help the user decide whether to bike or not to bike.


**2.3 User characteristics**

The user is not expected to have any technical knowledge. The users might be once off users who try out DublinBikes or they could be frequent users of the Bike sharing service who will rely on the app every day. It is likely they will use the app mostly on their mobile phone before starting their journey.

**2.4 Operating environment**

Taking the expected usage in consideration, the app is firstly designed and build for mobile use, with a responsive scheme for larger screen usage. It is able to stay responsive under complex situations. It works on any standard internet browser.


**2.5 Constraints**

1. The budget for the hardware devices / servers:

The application needs to run as lean as possible. Various performance optimization will need to be done to keep cost below 10 Euro a month on Amazon Web Server (AWS)

2. The request limitation set by service providers:

The API providers such as JCDecaux allow only a maximum amount of requests of 5000 a day. To make the application scalable we need to create a solution to store data so that it can be reused for multiple requests.


**3. System features**

**3.1 Overview functionalities 


Web Application:

● The application is able to display the map on the web browser.

● The application is able to display current available bikes on the web browser.

● The application is able to display the prediction of available bikes on the web browser.

● The application is able to adjust its appearance on different devices (Responsive design)


Data Collection:

● The Data Collection Server is able to fetch weather data from service provider.

● The Data Collection Server is able to fetch geocoding data from service provider.

● The Data Collection Server is able to fetch bike station data from service provider.


Interaction between Data Collection Server and Web Application Server

● The Data Collection Server is able to return data to Web Application Server.
13

● The Web Application Server is able to send request to Data Collection Server and process the returned data from Data Collection Server .


Machine Learning:

● The Machine Learning Server is able to read data from database.

● The Machine Learning Server is able to process request and send required data to
the client.

● Beta Feature: A Linear Regression Model is applied to predict bike availability for the next hour. The functionality is in beta and shows currently a minimum accuracy of 20%.


**4. Wireframe, Mockup V1**

<p align="left">
  <img src="https://github.com/scarletgrant/team9/blob/master/documentation/Wireframe_DublinBikes_Desktop_V01.png" height="400" title="hover text">
<alt="wireframes">
</p>

