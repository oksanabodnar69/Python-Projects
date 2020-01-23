import xml.etree.ElementTree as ET
import re


def parse_and_remove(filename, path):
   path_parts = path.split('/')
   doc = ET.iterparse(filename, ('start', 'end'))
   # Skip root element
   next(doc)
   tag_stack = []
   elem_stack = []
   for event, elem in doc:
    if event == 'start':
      tag_stack.append(elem.tag)
      elem_stack.append(elem)
    elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError:
                    pass


def unique_government():
    gover = []
    countries = parse_and_remove('mondial-3.0.xml', 'country')
    for country in countries:
        government = country.attrib['government'].strip()
        gover.append(government)
    unique_government=set(gover)
    print(",".join(unique_government))


def government_for_complicated_country_name():
    gover = []
    countries = parse_and_remove('mondial-3.0.xml', 'country')
    for country in countries:
        name=country.attrib['name'].strip()
        if re.match('(\w+) (\w+)',name):
           government = country.attrib['government'].strip()
           gover.append((name,government))
    for name,government in sorted(gover):
        print(f'{name} - {government}')


if __name__ == "__main__":
    print('List of unique government: \n')
    unique_government()
    print('\nList of government for countries with more then 1 word in name:\n')
    government_for_complicated_country_name()

