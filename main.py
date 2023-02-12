from xml.etree import ElementTree as ET

# TODO: remove all atributes from mediawiki element, otherwise it will not load it properly

for event, element in ET.iterparse('./data_preprocessing/original_data/skwiki-latest-pages-logging.xml', events=('start', 'end')):
    if event == 'end' and element.tag == 'logitem':

        log_id = element.find('id').text

        file_name = f'./upload_service/test_files/sk_wiki_logs/log_{log_id}.txt'

        f = open(file_name, 'wb')

        f.write(ET.tostring(element, encoding='utf-8'))

        f.close()

        element.clear()

