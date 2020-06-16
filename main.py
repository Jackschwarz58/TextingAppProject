import json
import config
from termcolor import colored # To get colored terminal output

data = {}

## Loads in the default users list and handles errors for the 2 known potential issues
## Expected issues: No JSON File, Empty file or Non-JSON file
def load_user_list():
    try:
        with open(config.DATA_FILEPATH) as users_file:
            data = json.load(users_file)
        print('')
        print(colored('SUCCESS:', 'green'), config.DATA_FILEPATH, "sucessfully read and parsed")
        print('')
    except FileNotFoundError:
        print('')
        print(colored('ERROR:', 'red'), "No Data File Found: Expected JSON at source", config.DATA_FILEPATH)
        print(colored('NOTE:', 'yellow'), "Please check and ensure you put your specified file at the correct file path.")
        print('')
        print("...Creating empty file and restarting function run...")
        print('')
        f = open(config.DATA_FILEPATH, 'w+')
        load_user_list()
    except ValueError:
        print('')
        print(colored('ERROR:', 'red'),'No JSON data found in file!')
        print('')

load_user_list()