# This is a sample Python script.
import requests
from bs4 import BeautifulSoup

from program import Program
from speaker import Speaker

my_parser = 'html.parser'
google_io_link = "https://io.google"
google_io_program = f"{google_io_link}/2023/program"
program_title_class = "font-medium sm:s-h4 md:l-h4 my-2"
short_description_class = "my-2 sm:s-p2 md:l-p2"
overview_class = "font-normal sm:s-p1 md:l-p1 mt-4 text-md:mt-6"
speaker_link_tag = "min-h-[270px]"
speaker_image_class = "rounded-full"
speaker_name_class = "sm:l-cta2 font-medium text-center"
speaker_role_class = "font-normal text-center"
program_img_class = "absolute h-full w-full object-cover rounded-xl"
program_tags_class = 'h-translated-category'
following_class = "mt-auto text-grey"


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def crawl_io_program():
    response = requests.get(google_io_program)
    soup = BeautifulSoup(response.content, my_parser)

    for program_tag in soup.find_all('div', role="listitem", class_="session"):
        link = program_tag.a['href']
        title = program_tag.find('h3', class_=program_title_class).string.strip()
        full_link = f"{google_io_link}{link}"
        program_image = program_tag.find('img', class_=program_img_class)['src']
        short_description = program_tag.find('p', class_=short_description_class).string.strip()
        # print("Prog desc")
        # print(title)
        full_image = f"{google_io_link}{program_image}"

        detail_request = requests.get(full_link)
        detail_soup = BeautifulSoup(detail_request.content, my_parser)
        overview = detail_soup.find('p', class_=overview_class).string.strip()
        following = detail_soup.find('div', class_=following_class).string
        tags = ','.join(set([tag["data-name"] for tag in detail_soup.find_all('div', class_=program_tags_class)]))
        # print(tags)
        speaker_tags = detail_soup.find_all('a', class_=speaker_link_tag)
        my_program = Program(title=title, short_description=short_description,
                             tags=tags, url=full_link, profile_image=full_image, speakers=[],
                             description=overview, following_session=following)
        for speaker_tag in speaker_tags:
            speaker_profile = f"{google_io_link}{speaker_tag['href']}"
            image = speaker_tag.find('img', class_=speaker_image_class, width="125", height="125")['src']
            speaker_image_url = f"{google_io_link}{image}"
            name = speaker_tag.find('p', class_=speaker_name_class).string
            role = speaker_tag.find('p', class_='font-normal').string
            pronoun_nullable = speaker_tag.find('p', class_='uppercase')
            pronoun = ''
            if pronoun_nullable is None:
                pass
            else:
                pronoun = pronoun_nullable.string.strip()
            new_speaker = Speaker(image=speaker_image_url, name=name, pronoun=pronoun,
                                  role=role, profile_url=speaker_profile)
            my_program.speakers.append(new_speaker)
        print("Program")
        print(my_program)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crawl_io_program()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
