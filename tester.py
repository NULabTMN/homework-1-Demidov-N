from bs4 import BeautifulSoup

# New function to extract links using BeautifulSoup
def extract_links(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
    
    # Find all <id> elements and extract their content
    links = [elem.text for elem in soup.find_all('id')]
    return links

def extract_topics(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
    
    # Find all <topic> elements and extract their content
    topics = [elem.text for elem in soup.find_all('topic')]
    return topics

def get_result_ids(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
    
    # Find all <id> elements inside <results> elements and extract their content
    result_ids = [i 
                  for result in soup.find_all('results')
                  for i in result.find_all('id')]
    return result_ids


xml_file = 'topics.xml'  # Path to the XML file
links = extract_links(xml_file)

print("Extracted IDs:")
for id_value in links:
    print(id_value)

print(f"Number of ids: {len(links)}, should be 48")
assert len(links) == 48, f"Number of IDs is incorrect, expected 48 but got {len(links)}"

# count number of topics
topics = extract_topics(xml_file)
print(f"Number of topics: {len(topics)}, should be 3")
assert len(topics) == 3, f"Number of topics is incorrect, expected 3 but got {len(topics)}"

# count number of result ids
result_ids = get_result_ids(xml_file)
print(f"Number of result ids: {len(result_ids)}, should be 45")
assert len(result_ids) == 45, f"Number of result ids is incorrect, expected 45 but got {len(result_ids)}"


print("All tests passed!")