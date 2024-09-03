import yaml
import mhtmlpy
from bs4 import BeautifulSoup


if __name__ == "__main__":
    mhtml_file = '~/input_mhtmls/aug_2024.mhtml'

    table_x_path = "/html/body/div[1]/div[3]/div/div[1]/div[1]/form/section[2]/div[2]"
    ip_x_path = "//*[@id="activity0"]/div/div[2]/div[3]/span/span[2]"
    full_ip_x_path = "/html/body/div[1]/div[3]/div/div[1]/div[1]/form/section[2]/div[2]/div[1]/div/div/div[2]/div[3]/span/span[2]"

    with open(mhtml_file, 'rb') as f:
        mhtml_content = f.read()
        parser = mhtmlpy.MHTMLParser(mhtml_content)
        html_content = parser.main_content()
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Extract all links
        for link in soup.find_all('a'):
            print(link.get('href'))
