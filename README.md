## Crawl Google IO 2023

This is a Python script that uses [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the
Google IO 2023 website and builds program data as well as
data for speakers.

### How is the parsing done?

Parsing happens this way:

- make a request to the [programs page](https://io.google/2023/program) and grab all programs
- For each program, make a request to the program's URL and get further details about the including the speakers
  handling that program
- Each time a program is encountered, add it to the programs list
- Convert the list of speakers to a set to avoid duplicates
- Write the programs and speakers to a JSON file