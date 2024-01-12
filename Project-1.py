#importing the requests package
import requests
from bs4 import BeautifulSoup

#scrape data from the website Wisdom Pet Medicine and sabing to getResponse variable
getReponse = requests.get('https://www.wisdompetmed.com/')
print(getReponse.url)
print(getReponse.status_code)
print(getReponse.headers)
print(getReponse.content)
print(getReponse.text)

soup = BeautifulSoup(getReponse.text, features="html.parser")
print(soup.prettify())

#finding all the instances of article tag
print(soup.find_all("article"))

#find business phone number
print(soup.find("span", class_ ="phone").text)
# the underscore is necessary so that the class is pulled from  HTML instead of being considered as a python keyword
# .text allows to extract the text between the tags and ignore the rest of HTML code

#find all featured testimonials
featured_testimonial = soup.find_all("div" , class_ = "quote")
for testimonial in featured_testimonial:
    print(testimonial.text)

#finding all staff members
staff =  soup.find_all("div", class_ = "info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
for s in staff:
    print(s.text)

#find all links on the webpage
webpage_links = soup.find_all("a")
for link in webpage_links:
    print(link.text, link.get('href'))

#export the HTML to a text file
with open("wisdom_vet.txt", "w", encoding="utf-8" ) as file:
    file.write(soup.prettify())
# w signifies writing to the file
# f is initializing the new file function