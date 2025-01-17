import re

# Just a small custom parser that converts a txt I used (which is more readable and easier to create) into an xml list of a single topic

def parse_and_convert_single_xml(file_path, topic_id):
    # Read input text from file
    with open(file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()
    
    # Split the input by double newlines to get individual blocks
    blocks = input_text.strip().split('\n\n')
    
    # Initialize the XML structure
    xml_output = f"<topic>\n<id>{topic_id}</id>\n<results>"
    
    for block in blocks:
        # Extract values using regex
        website_match = re.search(r'w:\s*(.+)', block)
        rel_match = re.search(r'rel:\s*(\d)', block)
        text_match = re.search(r'text:\s*(.+)', block, re.DOTALL)
        
        # Get values or set defaults
        website = website_match.group(1).strip() if website_match else ''
        rel = rel_match.group(1).strip() if rel_match else '0'
        text = text_match.group(1).strip() if text_match and rel == '1' else ''
        
        website = escape_special_characters(website)
        text = escape_special_characters(text)

        # Build the result entry
        xml_output += f"<result>\n<id>{website}</id>\n<rel>{rel}</rel>"
        if text:
            xml_output += f"\n<text>{text}</text>"
        xml_output += "\n</result>"
    
    # Close the results and topic tags
    xml_output += "\n</results>\n</topic>"
    
    return xml_output

def escape_special_characters(value):
    # based on this https://www.stuffaboutcode.com/2012/06/python-encode-xml-escape-characters.html
    return (value.replace('&', '&amp;')
    .replace('<', '&lt;')
    .replace('>', 'gt;')
    .replace('"', '&quot;')
    .replace("'", '&apos;'))
    
def combine_xmls(xml_original_files, topic_ids, output_name):
    # combine multiple xml into one
    
    output = "<topics>\n"
    
    for xml_file, topic_id in zip(xml_original_files, topic_ids):
        res = parse_and_convert_single_xml(xml_file, topic_id)
        output += res+"\n"

    output += "</topics>"
    
    with open(output_name, 'w', encoding='utf-8') as file:
        file.write(output)

files = ['topics-pigeon.txt', 'topics-plague.txt', 'topics-rasputin.txt']
topic_ids = ['https://guides.loc.gov/chronicling-america-war-pigeons',
             'https://guides.loc.gov/chronicling-america-spanish-flu', 
             'https://guides.loc.gov/chronicling-america-gregory-rasputin']
file_output = 'topics.xml'

combine_xmls(files, topic_ids, file_output)

