# import requests
# from bs4 import BeautifulSoup
# # !pip3 install pdfkit
# import pdfkit

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'  # Replace with the base URL of the website
# num_pages = 487  # Replace with the total number of paginated pages

# for page in range(486, num_pages + 1):
#     url = f'{base_url}/?sp={page}'  # Replace '/page/' with the actual URL pattern
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Scrape the links as before
#     pdf_links = soup.select('ul li a span.label')
#     # pdf_links = soup.find_all('div', class_='pdf-link')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#             response = requests.get(pdf_url)

#             # Save the PDF file
#             with open('file.pdf', 'wb') as file:
#                 file.write(response.content)


# import requests

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'  # Replace with the base URL of the website
# num_pages = 487  # Replace with the total number of paginated pages

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'  # Replace '/page/' with the actual URL pattern
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Scrape the links as before
#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         pdf_url = link.find_parent('a')['href']
#         if pdf_url.endswith('.pdf'):
#             response = requests.get(pdf_url)

#             # Save the PDF file
#             with open(pdf_url.split('/')[-1], 'wb') as file:
#                 file.write(response.content)

# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         pdf_url = None
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             label = link.text
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#     # for link in pdf_links:
#     #     pdf_url = link.find_parent('a')['href']
#     #     label = link.text

#         response = requests.get(pdf_url)

#         # Save the PDF file with the label as the filename
#         with open(f'{label}.pdf', 'wb') as file:
#             file.write(response.content)

# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         pdf_url = None  # Define pdf_url with a default value
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             label = link.text
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#         if pdf_url is not None:  # Check if pdf_url is defined before using it
#             response = requests.get(pdf_url)

#             # Save the PDF file with the label as the filename
#             with open(f'{label}.pdf', 'wb') as file:
#                 file.write(response.content)

# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         pdf_url = None
#         label = ''  # Define label with a default value
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             label = link.text
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#         if pdf_url is not None:
#             response = requests.get(pdf_url)

#             # Save the PDF file with the label as the filename
#             with open(f'{label}.pdf', 'wb') as file:
#                 file.write(response.content)

# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         pdf_url = None
#         label = ''  # Define label with a default value
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             label = link.text
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#         if pdf_url is not None:
#             response = requests.get(pdf_url)

#             # Save the PDF file with the label as the filename
#             decoded_url = urllib.parse.unquote(pdf_url)
#             filename = decoded_url.split('/')[-1]
#             with open(f'{label}.pdf', 'wb') as file:
#                 file.write(response.content)

# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487
# file_path = '/home/voodoo/_Projects/_Repos/web-scraper/Supreme-Court-Rulings/files/'

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         parent_a = link.find_parent('a')
#         pdf_url = None
#         label = ''  # Define label with a default value
#         if parent_a is not None:
#             pdf_url = parent_a['href']
#             label = link.text
#             if isinstance(pdf_url, list):
#                 pdf_url = pdf_url[0]  # Assuming the first element of the list is the correct URL
#             elif not isinstance(pdf_url, str):
#                 pdf_url = str(pdf_url)  # Convert to string if not already a string

#         if pdf_url is not None:
#             response = requests.get(pdf_url)

#             # Save the PDF file with the label as the filename
#             decoded_url = urllib.parse.unquote(pdf_url)
#             filename = decoded_url.split('/')[-1]
#             with open(f'{file_path}{label}.pdf', 'wb') as file:
#                 file.write(response.content)

# import requests
# from bs4 import BeautifulSoup

# base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
# num_pages = 487

# def download_pdf(url):
#     response = requests.get(url)

#     # Save the PDF file with a custom filename or extract it from the URL
#     filename = url.split('/')[-1]  # Extract the filename from the URL
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#     print(f"Downloaded: {filename}")

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
#         pdf_url = select_box.select_one('option[data-file-download="PDF"]')['value']
#         download_pdf(pdf_url)
#     else:
#         print(f"No PDF URL found for: {label}")

# for page in range(1, num_pages + 1):
#     url = f'{base_url}/?sp={page}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     pdf_links = soup.select('ul li a span.label')

#     for link in pdf_links:
#         navigate_and_download(link)

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.loc.gov/collections/united-states-reports/index/subject/'
num_pages = 487

def download_pdf(url):
    response = requests.get(url)

    # Save the PDF file with a custom filename or extract it from the URL
    filename = url.split('/')[-1]  # Extract the filename from the URL
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {filename}")

def navigate_and_download(link):
    label = link.find('span', class_='label').text
    level_1_url = link.find_parent('a')['href']

    # Navigate to the next page
    response = requests.get(level_1_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    level_2_url = soup.select_one('.results li a')['href']

    # Navigate to the PDF options page
    response = requests.get(level_2_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    select_box = soup.select_one('select.select-default')
    if select_box:
        pdf_url = select_box.select_one('option[data-file-download="PDF"]')
        if pdf_url is not None:
            pdf_url = pdf_url['value']
            download_pdf(pdf_url)
        else:
            print(f"No PDF URL found for: {label}")
    else:
        print(f"No PDF URL found for: {label}")

for page in range(1, num_pages + 1):
    url = f'{base_url}/?sp={page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    pdf_links = soup.select('ul li a span.label')

    for link in pdf_links:
        navigate_and_download(link)





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