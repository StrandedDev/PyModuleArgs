import inspect
import subprocess
import time
import os

def install_module(module_name):
    """Attempts to install a Python module using pip."""
    try:
        print(f"Status: Module {module_name} is not installed. Installing...")
        subprocess.check_call(['pip', 'install', module_name])
        print(f"Status: Module {module_name} has been installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing module {module_name}: {e}")

def install_another_module(module_name):
    """Installs another Python module using pip."""
    clear()
    try:
        subprocess.check_call(['pip', 'install', module_name])
        print(f"Status: Module {module_name} has been installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing module {module_name}: {e}")

def check_and_install_module(module_name):
    """Checks if a module is installed and installs it if not."""
    try:
        pip_list_output = subprocess.check_output(['pip', 'list']).decode('utf-8')
        if module_name not in pip_list_output:
            install_module(module_name)
        else:
            print(f"Status: Module {module_name} is already installed.")
    except Exception as e:
        print(f"Error checking or installing module {module_name}: {e}")

def list_members(module, member_type):
    """Lists classes or functions within a module."""
    members = inspect.getmembers(module, member_type)
    print(f"\n\t*****{member_type.__name__.upper()}*****\n")
    for name, member in members:
        print(f"{member_type.__name__}: {name}")

def list_members_with_args(module, member_type):
    """Lists classes or functions within a module along with their arguments."""
    members = inspect.getmembers(module, member_type)
    print(f"\n\t*****{member_type.__name__.upper()} and ARGUMENTS*****\n")
    for name, member in members:
        sig = inspect.signature(member)
        args = ', '.join(str(param) for param in sig.parameters.values())
        print(f"{member_type.__name__}: {name}, Arguments: {args}")

def run_all_functions(module):
    """Runs all functions within a module."""
    print("\n\t*****RUNNING ALL FUNCTIONS*****\n")
    list_members(module, inspect.isclass)
    list_members(module, inspect.isfunction)
    list_members_with_args(module, inspect.isfunction)
    list_members_with_args(module, inspect.isclass)

def clear():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    module_name = input("Enter the name of the module you want to get information of: ")
    try:
        module = __import__(module_name)
        check_and_install_module(module_name)
        
        time.sleep(2)
        clear()
        
        print("\nMenu:")
        print("1. List Classes")
        print("2. List Functions")
        print("3. List Functions and Arguments")
        print("4. List Classes and Methods")
        print("5. List Functions, Methods, and Arguments")
        print("6. Run All Functions")
        print("7. Install another module")
        print("8. Exit")
        
        choice = input("Please select an option: ")
        
        if choice == '1':
            list_members(module, inspect.isclass)
        elif choice == '2':
            list_members(module, inspect.isfunction)
        elif choice == '3':
            list_members_with_args(module, inspect.isfunction)
        elif choice == '4':
            list_members_with_args(module, inspect.isclass)
        elif choice == '5':
            list_members_with_args(module, inspect.isclass)
        elif choice == '6':
            run_all_functions(module)
        elif choice == '7':
            module_name = input('Enter the name of the module: ')
            install_another_module(module_name)
        elif choice == '8' or choice == 'exit' or choice == 'Exit':
            print("Exiting...")
            time.sleep(2)
        else:
            print("Invalid option. Please try again.")
    except ImportError:
        print(f"Module {module_name} is incorrect or not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    clear()
    main()
