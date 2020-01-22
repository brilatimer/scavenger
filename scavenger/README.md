**Scavenger**

**Introduction**

Version 1: Scavenger is a React web app integrated with [Twilio SMS API](https://www.twilio.com/docs/iam/keys/api-key-resource) to enable a user to create a customizable scavenger hunt experience and then send it to friends. A [form](https://reactjs.org/docs/forms.html) prompts the user to enter question, answer, hints to build their tailored scavenger hunt through a series of clues. Once launched, Twilio SMS API will automatically send the clues to the player and adapt based on their response (hint, next is built in).

Deployed with [Heroku](https://dashboard.heroku.com/apps). 

**Installation**

1. Clone this repository.
2. Install Python 3.7.4, Django and pip
3. Setup React
4. Install dependencies with npm install.
5. Start server with npm start.
6. In the project directory, you can run the following prompts:
  ``` yarn start
      yarn build
      yarn test ```

7. Import dependancies
8. Sign up or login to your Twilio account and create an access token for the API. Authenticate the REST API. Claim a Twilio personal number to be the sender.
9. Setup Heroku app server and deploy
10. Enjoy Scavenger!

Scavenger was developed by Bri Latimer as a capstone project for [Ada Developers Academy](https://adadevelopersacademy.org/).
