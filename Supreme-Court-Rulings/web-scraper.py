# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# def download_pdf(url):
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         # Save the PDF file with a custom filename or extract it from the URL
#         filename = url.split('/')[-1]  # Extract the filename from the URL
#         with open(filename, 'wb') as file:
#             file.write(response.content)
#         print(f"Downloaded: {filename}")
#     else:
#         print(f"Failed to download: {url}")

# def navigate_and_download(link):
#     label = link.find('span', class_='label').text
#     level_1_url = link.find_parent('a')['href']

#     # Navigate to the next page
#     response = requests.get(level_1_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     level_2_url = soup.select_one('.results li a')['href']

#     # Navigate to the PDF options page
#     response = requests.get(level_2_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     select_box = soup.select_one('select.select-default')
#     if select_box:
#         pdf_url = select_box.select_one('option[data-file-download="PDF"]')
#         if pdf_url is not None:
#             pdf_url = pdf_url['value']
#             download_pdf(pdf_url)
#         else:
#             print(f"No PDF URL found for: {label}")
#     else:
#         print(f"No PDF URL found for: {label}")

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         pdf_links = soup.select('ul li a span.label')

#         for link in pdf_links:
#             navigate_and_download(link)
#     else:
#         print(f"Failed to retrieve page: {url}")

# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# def download_pdf(url):
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         # Save the PDF file with a custom filename or extract it from the URL
#         filename = url.split('/')[-1]  # Extract the filename from the URL
#         with open(filename, 'wb') as file:
#             file.write(response.content)
#         print(f"Downloaded: {filename}")
#     else:
#         print(f"Failed to download: {url}")

# def navigate_and_download(link):
#     label_element = link.find('span', class_='label')
#     if label_element:
#         label = label_element.text
#         level_1_url = link.find_parent('a')['href']

#         # Navigate to the next page
#         response = requests.get(level_1_url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         level_2_url = soup.select_one('.results li a')['href']

#         # Navigate to the PDF options page
#         response = requests.get(level_2_url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         select_box = soup.select_one('select.select-default')
#         if select_box:
#             pdf_url = select_box.select_one('option[data-file-download="PDF"]')
#             if pdf_url is not None:
#                 pdf_url = pdf_url['value']
#                 download_pdf(pdf_url)
#             else:
#                 print(f"No PDF URL found for: {label}")
#         else:
#             print(f"No PDF URL found for: {label}")
#     else:
#         print("No label element found.")

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         pdf_links = soup.select('ul li a span.label')

#         for link in pdf_links:
#             navigate_and_download(link)
#     else:
#         print(f"Failed to retrieve page: {url}")

# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# def download_pdf(url):
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         # Save the PDF file with a custom filename or extract it from the URL
#         filename = url.split('/')[-1]  # Extract the filename from the URL
#         with open(filename, 'wb') as file:
#             file.write(response.content)
#         print(f"Downloaded: {filename}")
#     else:
#         print(f"Failed to download: {url}")

# def navigate_and_download(level_1_link):
#     level_1_url = level_1_link['href']
#     label = level_1_link.select_one('span.label').text

#     # Navigate to the next page
#     response = requests.get(level_1_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     level_2_link = soup.select_one('#results ul li div div span a')['href']

#     # Navigate to the PDF options page
#     response = requests.get(level_2_link)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     select_box = soup.select_one('select.select-default')
#     if select_box:
#         pdf_url = select_box.select_one('option[data-file-download="PDF"]')
#         if pdf_url is not None:
#             pdf_url = pdf_url['value']
#             download_pdf(pdf_url)
#         else:
#             print(f"No PDF URL found for: {label}")
#     else:
#         print(f"No PDF URL found for: {label}")

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)

#     # Check if the response was successful
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         level_1_links = soup.select('div#body div ul li a')

#         for link in level_1_links:
#             navigate_and_download(link)
#     else:
#         print(f"Failed to retrieve page: {url}")


# def navigate_and_download(level_1_link):
#     level_1_url = urljoin(base_url, level_1_link['href'])  # Join the base URL with the href value
#     span_label = level_1_link.find('span', class_='label')
    
#     if span_label:
#         label = span_label.text
#     else:
#         label = "Unknown label"

#     # Navigate to the next page
#     response = requests.get(level_1_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     level_2_link_element = soup.select_one('#results ul li div div span a')
#     if level_2_link_element is None:
#         print(f"No level 2 link found for: {label}")
#         return  # Skip this link if no level 2 link is found
#     level_2_link = level_2_link_element['href']
#     # level_2_link = soup.select_one('#results ul li div div span a')['href']

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
num_pages = 487
sleep_interval = 2  # in seconds

def download_pdf(url):
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        # Save the PDF file with a custom filename or extract it from the URL
        filename = url.split('/')[-1]  # Extract the filename from the URL
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

# def navigate_and_download(level_1_link):
#     level_1_url = urljoin(base_url, level_1_link['href'])  # Join the base URL with the href value
#     print(f"Level 1 URL: {level_1_url}")  # Debug line

#     span_label = level_1_link.find('span', class_='label')
    
#     if span_label:
#         label = span_label.text
#     else:
#         label = "Unknown label"

#     # Navigate to the next page
#     response = requests.get(level_1_url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(f"Level 1 content: {soup.prettify()}")  # Debug line

#     level_2_link_element = soup.select_one('#results ul li div div span a')
#     if level_2_link_element is None:
#         print(f"No level 2 link found for: {label}")
#         return  # Skip this link if no level 2 link is found
#     level_2_link = level_2_link_element['href']
#     print(f"Level 2 URL: {level_2_link}")  # Debug line

#     # Sleep to prevent getting blocked
#     time.sleep(sleep_interval)

#     # Navigate to the PDF options page
#     response = requests.get(level_2_link)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     select_box = soup.select_one('#select-resource0')
#     if select_box:
#         pdf_url = select_box.select_one('option[data-file-download="PDF"]')
#         if pdf_url is not None:
#             pdf_url = pdf_url['value']
#             download_pdf(pdf_url)
#         else:
#             print(f"No PDF URL found for: {label}")
#     else:
#         print(f"No PDF URL found for: {label}")

def navigate_and_download(level_1_link):
    with open('debug.txt', 'a') as debug_file:  # Open the debug file in append mode
        level_1_url = urljoin(base_url, level_1_link['href'])  # Join the base URL with the href value
        debug_file.write(f"Level 1 URL: {level_1_url}\n")  # Write the debug line to the file

        span_label = level_1_link.find('span', class_='label')

        if span_label:
            label = span_label.text
        else:
            label = "Unknown label"

        # Navigate to the next page
        response = requests.get(level_1_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        debug_file.write(f"Level 1 content: {soup.prettify()}\n")  # Write the debug line to the file

        level_2_link_element = soup.select_one('#results ul li div div span a')
        if level_2_link_element is None:
            debug_file.write(f"No level 2 link found for: {label}\n")  # Write the debug line to the file
            return  # Skip this link if no level 2 link is found
        level_2_link = level_2_link_element['href']
        debug_file.write(f"Level 2 URL: {level_2_link}\n")  # Write the debug line to the file

        # Sleep to prevent getting blocked
        time.sleep(sleep_interval)

        # Navigate to the PDF options page
        response = requests.get(level_2_link)
        soup = BeautifulSoup(response.text, 'html.parser')
        select_box = soup.select_one('#select-resource0')
        if select_box:
            pdf_url = select_box.select_one('option[data-file-download="PDF"]')
            if pdf_url is not None:
                pdf_url = pdf_url['value']
                download_pdf(pdf_url)
            else:
                debug_file.write(f"No PDF URL found for: {label}\n")  # Write the debug line to the file
        else:
            debug_file.write(f"No PDF URL found for: {label}\n")  # Write the debug line to the file


for page in range(1, num_pages + 1):
    url = f'{base_url}/?sp={page}'
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        level_1_links = soup.select('#body div ul li a')

        for link in level_1_links:
            navigate_and_download(link)

        # Sleep to prevent getting blocked
        time.sleep(sleep_interval)

    else:
        print(f"Failed to retrieve page: {url}")





# <span class="label">Zwickler V. Koota, 389 U. S. 241 (1967)</span>

# /html/body/div/div[2]/div/div/div[2]/ul/li[2]/a/span[1]

# /html/body/div/div[2]/div/div/div[2]/ul/li[1]/a/span[1]
# https://www.loc.gov/collections/united-states-reports/?fa=subject:zoning+regulations


# /html/body/div/div[2]/div/div/div[2]/ul/li[2]/a/span[1]
# https://www.loc.gov/collections/united-states-reports/?fa=subject:zwickler+v.+koota,+389+u.+s.+241+%281967%29


# if isinstance(pdf_url, list):
#     pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
# elif not isinstance(pdf_url, str):
#     pdf_url = str(pdf_url)  # Convert to string if not already a string

# response = requests.get(pdf_url)

# https://www.loc.gov/collections/united-states-reports/?fa=subject:zwickler+v.+koota,+389+u.+s.+241+%281967%29