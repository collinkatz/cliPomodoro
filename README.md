# cliPomodoro
## About
- cliPomodoro is an easy to use, minimal setup, pomodoro timer.
- This timer was created to help with eye strain, and follows the 20-20-20 rule. I.e. if you spend 20 minutes looking at a screen, look at something 20 feet away for 20 seconds.
- Other pomodoro applications force you to pay money to customize the timer, but this allows you to customize your timer, and works seamlessly on your work, school, or home computer (as long as you have python installed).

## How to use
### Requirements
- Have git installed
- Have python and a package manager of your choice installed (pip works fine)

### Setup
- Clone this git repository

- Using a command line that has git, CD to a directory where you want the timer to be accessible then use the following
    ```python
        git clone https://github.com/collinkatz/cliPomodoro.git
    ```

- CD into the cloned repository directory
    ```python
        cd ./cliPomodoro
    ```

- Now create a virtual environment where we will install the packages
    ```python
        python -m venv .venv
    ```

- Now activate the virtual environment by running the activate script
    ```python
        ./.venv/Scripts/activate
    ```

- Now install the packages from the requirements.txt file with your virtual environment activated
    ```python
        pip install -r ./requirements.txt
    ```

### Run

- You may edit the timer's times in the config.py file to your liking
- To run the timer:
    ```python
        python ./timer.py
    ```