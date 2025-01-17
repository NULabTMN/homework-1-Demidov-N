from bs4 import BeautifulSoup

# New function to extract links using BeautifulSoup
def extract_links(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
    
    # Find all <id> elements and extract their content
    links = [elem.text for elem in soup.find_all('id')]
    return links


xml_file = 'topics.xml'  # Path to the XML file
links = extract_links(xml_file)

print("Extracted IDs:")
for id_value in links:
    print(id_value)

print(f"Number of ids: {len(links)}, should be 48")
assert len(links) == 48, f"Number of IDs is incorrect, expected 48 but got {len(links)}"