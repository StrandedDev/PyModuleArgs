import inspect
import subprocess
import time
import os


def install_module(module_name):
    try:
        print(f"Status: Module {module_name} is not installed. Installing...")
        subprocess.check_call(['pip', 'install', module_name])
        print(f"Status: Module {module_name} has been installed.")
    except Exception as e:
        print(f"Error installing module {module_name}: {e}")

def install_another_module():
    clear()
    module_name = input('Enter the name of the module: ')
    subprocess.check_call(['pip', 'install', module_name])
    print(f"Status: Module {module_name} has been installed.")



def check_and_install_module(module_name):
    try:
        # Run 'pip list' and get the output
        pip_list_output = subprocess.check_output(['pip', 'list']).decode('utf-8')
        # Check if the module is in the list
        if module_name not in pip_list_output:
            install_module(module_name)
        else:
            print(f"Status: Module {module_name} is already installed.")
    except Exception as e:
        print(f"Error checking or installing module {module_name}: {e}")



def list_classes(module):
    classes = inspect.getmembers(module, inspect.isclass)
    print("\n\t*****CLASSES*****\n")
    for name, cls in classes:
        print(f"Class: {name}")

def list_functions(module):
    functions = inspect.getmembers(module, inspect.isfunction)
    print("\n\t*****FUNCTIONS*****\n")
    for name, func in functions:
        print(f"Function: {name}")

def list_functions_and_arguments(module):
    functions = inspect.getmembers(module, inspect.isfunction)
    print("\n\t*****FUNCTIONS and ARGUMENTS*****\n")
    for name, func in functions:
        sig = inspect.signature(func)
        args = ', '.join(str(param) for param in sig.parameters.values())
        print(f"Function: {name}, Arguments: {args}")

def list_classes_and_methods(module):
    classes = inspect.getmembers(module, inspect.isclass)
    print("\n\t*****CLASSES and METHODS*****\n")
    for name, cls in classes:
        methods = inspect.getmembers(cls, predicate=inspect.isfunction)
        for method_name, method in methods:
            print(f"Class: {name}, Method: {method_name}")

def list_functions_methods_and_arguments(module):
    classes = inspect.getmembers(module, inspect.isclass)
    print("\n\t*****FUNCTIONS, METHODS and ARGUMENTS*****\n")
    for name, cls in classes:
        methods = inspect.getmembers(cls, predicate=inspect.isfunction)
        for method_name, method in methods:
            sig = inspect.signature(method)
            args = ', '.join(str(param) for param in sig.parameters.values())
            print(f"Class: {name}, Method: {method_name}, Arguments: {args}")

def run_all_functions(module):
    print("\n\t*****RUNNING ALL FUNCTIONS*****\n")
    list_classes(module)
    list_functions(module)
    list_functions_and_arguments(module)
    list_classes_and_methods(module)
    list_functions_methods_and_arguments(module)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    module_name = input("Enter the name of the module you want to get information of: ")
    try:
        module = __import__(module_name)
        check_and_install_module(module_name)
        
        # 3-second delay
        time.sleep(2)
        
        # Clear the console
        clear()
        
        # Show menu one time
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
            list_classes(module)
        elif choice == '2':
            list_functions(module)
        elif choice == '3':
            list_functions_and_arguments(module)
        elif choice == '4':
            list_classes_and_methods(module)
        elif choice == '5':
            list_functions_methods_and_arguments(module)
        elif choice == '6':
            run_all_functions(module)
        elif choice == '7':
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
