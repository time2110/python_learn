import requests


def get_url():
    source = requests.get('http://exercise.kingname.info/exercise_requests_get.html')
    print(source.content.decode('utf-8'))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
