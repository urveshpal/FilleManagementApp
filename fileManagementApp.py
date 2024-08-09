import os
def create_file(filename):
    try:
        with open(filename,'x')as f:
            print(f"file name {filename}:Created successfully!")
    except FileExistsError:
        print(f"file name {filename} already exists!")
    except Exception as e:
        print("An error occured!",e)

def view_all():
    file = os.listdir()
    if not file:
        print("No file found")
    else:
        print("files in directory!")
        for f in file:
            print(f)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successful!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as e:
        print('An error occured!',e)

def read_file(filename):
    try:
        with open(filename,'r')as f:
            content = f.read()
            print(f"content of '{filename}': \n{content}")
    except FileNotFoundError:
        print("File not found Error!")
    except Exception as e:
        print("An exception occured",e)

def edit_file(filename):
    try:
        with open(filename,'a')as f:
            content = input("enter data:")
            f.write(content+"\n")
            print(f"content added to {filename} successful")
    except FileNotFoundError:
        print(f"file {filename} not found. ")

def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1: Create file")
        print("2: View all file")
        print("3: Edit File")
        print("4: Read file")
        print("5: Delete file")

        ch = input("Enter your choice:")
        match ch:
            case '1': 
                filename = input("Enter the filename:")
                create_file(filename)
            case '2': view_all()
            case '3':
                filename = input("Enter file name:")
                edit_file(filename)
            case '4':
                filename = input("Enter filename:")
                read_file(filename)
            case '5':
                filename = input("Enter filename:")
                delete_file(filename)
            case '6': break
if __name__ == '__main__':
    main()