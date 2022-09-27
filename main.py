import requests


def get_url():
    source = requests.get('https://translate.google.cn/?sl=en&tl=zh-CN&text=ewq&op=translate')
    print(source.text)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_url()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
