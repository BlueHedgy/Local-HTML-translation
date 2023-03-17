import time
from bs4 import BeautifulSoup
import os
from googletrans import Translator

dir = "G:/Scrape testing/www.classcentral.com"
# url = "G:/Scrape testing/www.classcentral.com/index.html"
invalid_tags = ['meta', 'script', 'style', 'path', 'svg', 'noscript']

def translate(input_text):
    translator  = Translator()
    output_text = ""
    if (input_text != "\n"):
        translation = translator.translate(input_text, src="en", dest="hi")
        output_text = translation.text
    return output_text

def parse_html(filename):
    with open(filename, encoding="utf-8") as file:

        soup = BeautifulSoup(file, 'lxml')
        for tag in soup.find_all():
            if tag.name not in invalid_tags:
                if (tag.string != None):
                    translated = translate(str(tag.string))
                    tag.string.replace_with(translated)
                    print(tag.string)
                    time.sleep(3)

    with open(filename, "wb") as file_output:
        file_output.write(soup.prettify("utf-8"))


def main():

    for root, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            time.sleep(2)
            if filename.endswith('.html'):
                file = os.path.join(dir, filename)
                parse_html(file)
            time.sleep(1)

    # parse_html(url)
    
if __name__== "__main__":
    main()
    
