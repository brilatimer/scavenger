# **Scavenger**

## **Introduction**

Version 1: Scavenger is a React web app integrated with [Twilio SMS API](https://www.twilio.com/docs/iam/keys/api-key-resource) to enable a user to create a customizable scavenger hunt experience and then send it to friends. A [form](https://reactjs.org/docs/forms.html) prompts the user to enter question, answer, hints to build their tailored scavenger hunt through a series of clues. Once launched, Twilio SMS API will automatically send the clues to the player and adapt based on their response (hint, next is built in).

Deployed with [Heroku](https://dashboard.heroku.com/apps). 

### **Installation**

1. Clone this repository.
2. Install Python 3.7.4, Django and pip
3. Setup React
4. Install dependencies with npm install.
5. Start server with npm start.
6. Run: python3 manage.py runserver. This will now be accessible at http://localhost:3000/
7. In the project directory, you can run the following prompts: yarn    test, yarn start, yarn build
8. Import dependancies
9. Sign up or login to your Twilio account and create an access token for the API. Authenticate the REST API. Claim a Twilio personal number to be the sender.
10. Setup Heroku app server and deploy
11. Enjoy Scavenger!

_**Scavenger was developed by Bri Latimer as a capstone project for [Ada Developers Academy](https://adadevelopersacademy.org/).**_
