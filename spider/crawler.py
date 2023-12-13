import httpx
from bs4 import BeautifulSoup


class Spider:
    def __init__(self):
        self.websites_list: list = []
        self.robots = 'robots.txt'
        self.meta_attr = 'robots'
        self.disallowed_pages: list | dict = []

    def _is_robots_in_meta_tag(self, resp) -> bool:
        """
        Checks in html source code in meta tag if class_name == robots
        :return: Bool
        """
        html = BeautifulSoup(resp.text, 'html.parser')
        # find all img tags in html
        metas = html.find_all('meta', attrs={'name': self.meta_attr})
        if self.meta_attr in metas:
            print(metas)
            return True
        return False

    def _is_robot_file_on_domain(self, website) -> bool:
        """
        Checks if the file >robots.txt< exists on website url_website/robots.txt
        :return: Bool
        """

        if self.robots in website:
            return True
        return False

    def append_excluded_pages(self) -> None:
        for line in self.robots:
            ...

    def get_html(self, website: str) -> httpx.Response:
        response = httpx.get(website)
        return response



    def crawl_for_images(self):
        """
        Main execution of Spider
        :return:
        """
        if len(self.websites_list) < 1:
            raise
        for website in self.websites_list:
            website_html = self.get_html(website)


webpage = 'https://kwejk.pl/'

crawler = Spider()
crawler.websites_list = [webpage]
crawler.crawl()
