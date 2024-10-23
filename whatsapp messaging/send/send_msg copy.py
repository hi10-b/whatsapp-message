# Working script but attaches as file instead of image
# ===================================================================================>

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to format phone number from +61412345678 to +61 412 345 678
def format_phone_number(phone_number):
    return f"{phone_number[:3]} {phone_number[3:6]} {phone_number[6:9]} {phone_number[9:]}"

# Function to send WhatsApp messages with images to multiple contacts
def send_whatsapp_messages(phone_numbers):
    # Set Chrome options
    chrome_options = Options()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Adjust if necessary
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")  # Start maximized for visibility

    # Initialize ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # WebDriverWait instance for handling explicit waits
    wait = WebDriverWait(driver, 15)

    try:
        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com")
        print("Please scan the QR code to log in.")
        
        # Wait for user to scan the QR code and WhatsApp Web to load completely
        time.sleep(20)  # Increase the wait time to ensure everything is fully loaded

        for phone_number in phone_numbers:
            # Format the phone number to include spaces
            formatted_phone_number = format_phone_number(phone_number)
            
            # Normalize the phone number for file matching (remove + sign and spaces for image name)
            normalized_phone_number = phone_number.replace("+", "").replace(" ", "")  # Remove the + sign and spaces for the image name
            image_path = f"{formatted_phone_number}.png"  # Use normalized phone number for image name
            
            if os.path.exists(image_path):
                # Locate the search box
                try:
                    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[title="Search input textbox"]')))
                except:
                    # Fallback to XPath if CSS selector fails
                    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))

                search_box.clear()
                search_box.send_keys(formatted_phone_number)
                time.sleep(3)  # Wait for search results

                # Locate the contact and click on it, including spaces in the number
                try:
                    contact_element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{formatted_phone_number}"]')))
                    contact_element.click()
                except Exception as e:
                    print(f"Failed to select contact {formatted_phone_number}: {e}")
                    continue

                time.sleep(2)  # Wait for the chat to open

                # Attach the image
                attach_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]')))
                attach_button.click()
                time.sleep(1)

                # Upload the image
                file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
                file_input.send_keys(os.path.abspath(image_path))  # Use the absolute path
                time.sleep(2)  # Wait for the upload

                # Send the message
                send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]')))
                send_button.click()
                print(f"Message sent to {formatted_phone_number} with image {image_path}.")
                time.sleep(2)  # Wait between messages

            else:
                print(f"Image for {formatted_phone_number} not found.")  # Now prints the formatted phone number

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    phone_numbers = [
        "+61413598987","+61413598987"
    ]
    send_whatsapp_messages(phone_numbers)
