from selenium import webdriver
from selenium.webdriver import Firefox 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from colorama import Style , Fore , init 
import time , pathlib , csv , os , random

init()

os.system("clear")

while True:
    try:
        target_amount = int(input(f"{Style.BRIGHT + Fore.WHITE}Please enter target amount of quotes:{Style.RESET_ALL} "))
        break
    except ValueError:
        print(f"{Style.BRIGHT + Fore.RED}Input must be a number!{Style.RESET_ALL}")

respectful_scraping = input(f"{Style.BRIGHT + Fore.WHITE}Turn {Fore.GREEN}on{Fore.WHITE} respectful scraping?({Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}):{Style.RESET_ALL} ").lower()

while respectful_scraping not in ["y" , "n"]:
    respectful_scraping = input(f"{Style.BRIGHT + Fore.WHITE}Turn {Fore.GREEN}on{Fore.WHITE}respectful scraping?({Fore.GREEN}Y{Fore.WHITE}/{Fore.RED}N{Fore.WHITE}):{Style.RESET_ALL} ").lower()

path = pathlib.Path(__file__).resolve().parent

os.system("clear")
print(f"{Style.BRIGHT + Fore.WHITE}Initializing browser...{Style.RESET_ALL}")

options = Options()
options.add_argument("--headless")

browser = webdriver.Firefox(options=options)

browser.get("https://quotes.toscrape.com/scroll")

os.system("clear")
print(f"{Style.BRIGHT + Fore.WHITE}Opening .csv file for writing...{Style.RESET_ALL}")

output = []

while len(output) < target_amount:
    html_quotes = browser.find_elements(By.CLASS_NAME , "quote")

    for quote in html_quotes[len(output):]:
        if len(output) <  target_amount:
            os.system("clear")
            print(f"{Style.BRIGHT + Fore.WHITE}Scraping {len(output) + 1} quote...{Style.RESET_ALL}")

            text = quote.find_element(By.CLASS_NAME , "text").text
            author = quote.find_element(By.CLASS_NAME , "author").text

            output.append([text , author])

            browser.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
            
            print(f"{Style.BRIGHT + Fore.GREEN}Success{Fore.WHITE}: Appended new quote.{Style.RESET_ALL}")
            if respectful_scraping == "y":
                time.sleep(random.uniform(1 , 2))
        else:
            break

os.system("clear")
print(f"{Style.BRIGHT + Fore.WHITE}Writing scraped data to 'results.csv'...{Style.RESET_ALL}")

with open(f"{path}/results.csv" , "a" , newline="") as file:
    csvwriter = csv.writer(file)
    for text , author in output:
        csvwriter.writerow([text , author])

browser.quit()

os.system("clear")
print(f"{Style.BRIGHT + Fore.GREEN}Success!{Fore.WHITE} Output at 'results.csv'.{Style.RESET_ALL}")