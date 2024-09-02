import yaml
import mhtmlpy
from bs4 import BeautifulSoup


if __name__ == "__main__":
    mhtml_file = 'path/to/your/file.mhtml'

    with open(mhtml_file, 'rb') as f:
        mhtml_content = f.read()
        parser = mhtmlpy.MHTMLParser(mhtml_content)
        html_content = parser.main_content()
        soup = BeautifulSoup(html_content, 'html.parser')
        # Example: Extract all text
        print(soup.get_text())

        # Example: Extract all links
        for link in soup.find_all('a'):
            print(link.get('href'))
