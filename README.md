# django_board

## Installation and Setup

- Navigate to directory of choice on terminal.
- Clone this repository on that directory.

   - Using SSH;

     ```
     git clone git@github.com:eshaibu/django_board.git
     ```
   - Using HTTP;

     ```
     https://github.com/eshaibu/django_board.git
     ```
- Navigate  to the repo's folder on your computer.

     ```
     cd django_board
     ```

- Ensure you have Python3 and virtualenv installed.
- Create a virtualenv
    ```
    virtualenv venv -p python3
    ```
- Install the app's dependencies using pip
 
     ```
     pip install -r requirements.txt
     ```

- Setup the local configurations (Copy content from `.env.sample` file to `.env` file):
    ```
    cp .env.example .env
    ```
    
- Run tests in your terminal.

     ```
     python manage.py test
     ```

- Start the application.

     ```
     python manage.py runserver
     ```

- This launches the app on your default browser on `http://localhost:8000`
