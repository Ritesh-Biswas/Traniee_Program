import threading
import requests # type: ignore

# List of websites for checking
websites = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.python.org',
    'https://www.askdksxke.xyz',  # Invalid URL to test error handling
    'https://www.stackoverflow.com'
]

print_lock = threading.Lock() #Just memorize it it use to prevent the overlaping of the threads

def check_website_status(url):
    try:
        response = requests.get(url,timeout=5)
        with print_lock:
            if response.status_code == 200:
                print (f"[ONLINE]:- {url}")
            else:
                #'with' is the context manager that automatically handles the acquring & releasing the lock
                with print_lock:
                    print(f"[OFFLINE]:- {url} - Status Code is :- {response.status_code}")
    except requests.RequestException as e:
        with print_lock:
            print(f"[ERROR] :- {url} - {e}")

def main():
    threads = []

    for website in websites:
        # the comma ',' is used because args except the Tuple , but we have single element therefore we use comma
        thread = threading.Thread(target=check_website_status, args=(website,)) #Creating new Thread for each website
        threads.append(thread) #Adding threads after each other like stack

        thread.start()

# Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("\nFinished checking all websites.")


main()    
