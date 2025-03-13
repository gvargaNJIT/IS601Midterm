# Advanced Command-line Calculator with Calculation History Management

## Description

This calculator has many different functionalities including basic operations of addition, subtraction, multiplication, and division. You can activate this program by typing 'python main.py' into the command line. Then you can enter 'add', 'subtract', 'multiply', 'divide', 'menu', 'history', or 'exit' to do the actions you desire out of the program. Typing 'history' will present to you option on how to view and manage your history. Those options and their abilities are 'view history' which views all the saved history of the program that wasn't deleted, 'delete history' which deletes the saved history, 'get latest' which get the last equation that was operated from history, and 'back' which goes back to the main calculator. This was created with python and pandas for the calculator history data and when the program closes through exit, the history is saved and loaded back when the program starts again. This was tested with pytest, pylint, pytest coverage, and faker to simulate equations. There is logging configuration as well to keep status of the activity of the program.

Link to demonstration of the program - [here](https://youtu.be/DLKnmqZJeYw)

## Implementation of Design Patterns

- **Facade Pattern** [link](https://github.com/gvargaNJIT/IS601Midterm/blob/main/app/__init__.py): The App class simplifies the interface for managing Pandas by encapsulating its operations from the Data class in commands/__init__.py.
- **Command Pattern** [link](https://github.com/gvargaNJIT/IS601Midterm/blob/main/app/commands/__init__.py): The Command class and Commandlist class allow easy registering and excuting commands from any class that is a subclass of Command.
- **Factory Method** [link](https://github.com/gvargaNJIT/IS601Midterm/blob/main/calculations/calcHistory.py): Calculator.performOperation() function allows for factory-like methodology by avoiding the creation of Calculation objects in the code manually.
- **Singleton Pattern** [link](https://github.com/gvargaNJIT/IS601Midterm/blob/main/calculations/__init__.py): CalcHistory class lets history be a class attribute and the class method on the functions operate on that history list.
- **Strategy Pattern** [link](https://github.com/gvargaNJIT/IS601Midterm/blob/main/app/strategies/__init__.py):The MenuStrategy and MenuContext classes allow scalibility with dynamic, interchangeable commands through their subclasses.

## Logging Configuration

There is a logging.conf file ([here](https://github.com/gvargaNJIT/IS601Midterm/blob/main/logging.conf)) which holds the basic information on how the logging will be formatted when it is printed. I will used my divide plugin ([here](https://github.com/gvargaNJIT/IS601Midterm/blob/main/app/plugins/divide/__init__.py)) as an example of my implementation of logging. For basic information, like what number was inputted for the equation, I used logging.info and a message of that number to keep track of where the program is at in the code. But when the user puts in a character instead of a number or the second number is a 0, a logging.error will occur showing the time where the program rejected input from the user. These logs are saved in a directory that is created when the app first runs if it is not already there.

## Try/Catch (LBYL and EAFP)

The example I will use for a try/catch, ie try: except:, is class NumberInput ([here](https://github.com/gvargaNJIT/IS601Midterm/blob/main/app/commands/__init__.py)). I use this method because most of the time a number is the input on the user's end. But in case they use something other than a number, I put except Exception as e then printed and logged that whatever they put in {a} was not a valid number where a is their input.

## Environment Variable

I do have an environment variable in this code that likes to the csv file where the calculations are saved. That env file has this in it: CSV_PATH=./data/gpt_calc_history.csv