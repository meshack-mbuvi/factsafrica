### Description
This is a challenge project for maintaining customer data. A customer can request loan subject to their loan limit.
An interest is accrued every 30 seconds for the requested loan.

### Installation
To ensure smooth functioning of this project, ensure you have install python3 and postgresQL database engine in your machine.
Then follow these steps to have a working copy locally:
  - Clone this repository to your local machine
  - Change your workin directory to the project directory
  - Create a virtual environment in the current directory
  - Activate the above virtual environment
  - Run pip install -r requirements.txt
  - Copy .env-sample to .env and fill it with the database credentials
  - Run python manage.py migrate
  - Run python manage.py runserver
  - Open your browser and navigate to http://127.0.0.1:8000/admin/

Enjoy the features provided.

### Support
For any issue encountered that you are not able to resolve by your own, feel free to reach out to [me](meshmbuvi@gmail.com)

### Author
[Meshack Mbuvi](https://github.com/meshack-mbuvi)

### Note:
I have not been able to have cron run the tasks in the background. As I find a way to implement it, please run the command:
 `python manage.py runcrons` in your terminal
### HOSTING
The application is hosted [here](https://factsafrica.herokuapp.com/admin)