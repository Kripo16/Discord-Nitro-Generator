import requests
import subprocess
import os
import time
from colorama import init, Fore

def print_with_delay(text, color, delay=0.1):
    for char in text:
        print(Fore.__dict__[color] + char, end='', flush=True)
        time.sleep(delay)
    print(Fore.RESET, end='', flush=True)

def welcome_animation():
    init(autoreset=True)  # Initialize colorama

    print_with_delay("WELCOME TO ", "GREEN")
    print_with_delay("KRIPO GENERATOR\n", "YELLOW")

welcome_animation()



syntax = "https://discord.com/billing/partner-promotions/1180231712274387115/"
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authority': 'api.discord.gx.games',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

data = {
    'partnerUserId': '24600c8d4e29e8e85dbda8ed562c5c03be51ae8ac8f0249ec5a64e9fe42313e3'
}
x = 1
file_path = 'CODES\\code.txt'
def generate():
    global x
    global file_path
    number = int(input('How many nitros do u want to generate? '))
    while x <= number:
        # Make the POST request using the requests library
        response = requests.post(url, headers=headers, json=data)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            json_response = response.json()

            # Extract and print the "token" value without quotes and braces
            token_value = json_response.get('token', '')
            code = str(x) + ': ' + syntax + token_value
            # Open the file in write mode ('w' flag)
            with open(file_path, 'a') as file:
                # Write the data to the file
                file.write(str(code) + '\n')
            print(code)
            print('____________________________________________________')
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            break
        x+=1
    with open(file_path, 'a') as file:
            # Write the data to the file
            file.write('                                                        [THE END]\n')
    print(f"Nitro Gift Codes has been stored in {file_path}")
    if (x-1) == number:
        x = 1
    ask()
def ask():
    answer = input("Wanna generate again? (yes/no) ")
    if answer.lower() == "yes":
        generate()
    elif answer.lower() != "no" and answer.lower() != "yes":
        print("Choose a VALID ANSWER !!")
        ask()
    elif answer.lower() == 'no':
        openfile(app_name)
def openfile(app_name):
    subprocess.run(['start', '', app_name], shell=True)
app_name = 'CODES\\code.txt'  


generate()


    


