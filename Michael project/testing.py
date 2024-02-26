
from bs4 import BeautifulSoup, NavigableString
import requests
import csv

def find_h2_with_string(tag):
    return tag.name == 'h2' and 'Subject' in tag.get_text()

def find_h2_tag(tag):
    return tag.name == 'h2' and 'UN Sustainable Development Goals' in tag.get_text()


def inner_data(name, url, acrony_text, founded, city_hq, country, type_1, type_2, uia_id):
    with open('your_output_file.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['Name', 'URL', 'Acronym', 'Founded', 'City_HQ', 'Country', 'Type_1', 'Type_2', 'UIA_ID', 'Founded_Text', 'History', 'Events', 'Aims', 'Finance','Activity', 'Structure', 'Members', 'Consultative_Status', 'Registrations', 'Type_1_Classification', 'Type_2_Classification', 'Subjects', 'UN Sustainable Development Goals','Last_News', 'Contact_Details']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Writing header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'lxml')

            # Example: get the title of the webpage
            founded_h2_tags = soup.find('h2', text='Founded')
            try:
                founded_text = founded_h2_tags.find_next_sibling('p').text.replace('\n\t',' ') #************************
            except:
                founded_text = ''
            

            #History
            try:
                histroy_h2_tags = soup.find('h2',text='History')
                history_paragraph = []
                if histroy_h2_tags:
                    for sibling in histroy_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            history_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            history_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text
                                history_paragraph.append(t + " | ")
            except:
                pass
            
            history_paragraph = ' '.join(history_paragraph) #*************************




        # Events 
            events_list = []
            event_h2_tag = soup.find('h2', text='Events')
            if event_h2_tag:
                try:
                    for sibling in event_h2_tag.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name is None:
                            events_list.append(sibling.strip().replace('\n',' '))
                        elif sibling.name == 'p':
                            events_list.append(sibling.text.strip().replace('\n',' '))
                        elif sibling.name == 'a':
                            events_list.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text
                                events_list.append(t + " | ")
                except:
                    pass
                        

            events_text = ' '.join(events_list)
            






            #Aims 
            aims_list = []
            aims_h2_tags = soup.find('h2', text='Aims')
            try:
                if aims_h2_tags:
                    for sibling in aims_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            aims_list.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            aims_list.append(sibling.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.replace('\n',' ')
                                aims_list.append(t + " | ")
            except:
                pass
            aims = ' '.join(aims_list) #*********************************
        

            




            # Activity
            activity_h2_tags = soup.find('h2',text='Activities')
            activity_paragraph = []
            try:
                if activity_h2_tags:
                    for sibling in activity_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            activity_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            activity_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.replace('\n',' ')
                                activity_paragraph.append(t + ' | ')
            except:
                pass
            
            activity_paragraph = ' '.join(activity_paragraph) #************************* 
            


            # Structure
            structure_h2_tags = soup.find('h2',text='Structure')
            structure_paragraph = []
            try:
                if structure_h2_tags:
                    for sibling in structure_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            structure_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            structure_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags =sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.strip().replace('\n',' ')
                                structure_paragraph.append(t +" | ")
   
            except:
                pass


            
            structure_paragraph = ' '.join(structure_paragraph) #*************************
            

            #Members
            members_h2_tags = soup.find('h2',text='Members')
            members_paragraph = []
            try:
                if members_h2_tags:
                    for sibling in members_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            members_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            members_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.replace('\n',' ')
                                members_paragraph.append(t + ' | ')
            except:
                pass
            
            members_paragraph = ' '.join(members_paragraph) #*************************
        


            #Consultative Status
            cs_h2_tags = soup.find('h2',text='Consultative Status')
            cs_paragraph = []
            try:
                if cs_h2_tags:
                    for sibling in cs_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            cs_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            cs_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags =sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.strip().replace('\n',' ')
                                cs_paragraph.append(t +" | ")
            except:
                pass

            cs_paragraph = ' '.join(cs_paragraph)
 #*****************************






            #Finance
            finance_h2_tags = soup.find('h2',text='Finance')
            finance_paragraph = []
            try:
                if finance_h2_tags:
                    for sibling in finance_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            finance_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            finance_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags =sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.strip().replace('\n',' ')
                                finance_paragraph.append(t +" | ")

            except:
                pass
            finance_paragraph = ' '.join(finance_paragraph) #*****************************




            #Registrations
            registration_h2_tags = soup.find('h2',text='Registrations')
            registration_paragraph = []
            try:
                if registration_h2_tags:
                    for sibling in registration_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            registration_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            registration_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags =sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.strip().replace('\n',' ')
                                registration_paragraph.append(t +" | ")
            except:
                pass

            registration_paragraph = ' '.join(registration_paragraph) #*****************************

            #type 1 classification
            t_1_classification_h2_tags = soup.find('h2',text='Type I Classification')
            t_1_classification_paragraph = []
            try:
                if t_1_classification_h2_tags:
                    for sibling in t_1_classification_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            t_1_classification_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            t_1_classification_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tags.text.replace('\n',' ')
                                t_1_classification_paragraph.append(t + ' | ')
            except:
                pass
            
            t_1_classification_paragraph = ' '.join(t_1_classification_paragraph) #*************************
            


            #type 2 classification 
            t_2_classification_h2_tags = soup.find('h2',text='Type II Classification')
            t_2_classification_paragraph = []
            try:
                if t_2_classification_h2_tags:
                    for sibling in t_2_classification_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            t_2_classification_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            t_2_classification_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.replace('\n',' ')
                                t_2_classification_paragraph(t + " | ")
            except:
                pass
            
            t_2_classification_paragraph = ' '.join(t_2_classification_paragraph) #*************************
            



            #Subjects 
            subj_h2_tags = soup.find(find_h2_with_string)
            subj_paragraph = []
            try:
                if subj_h2_tags:
                    for sibling in subj_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            subj_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'a':
                            subj_paragraph.append(sibling.text.replace('\n',' '))
                        elif sibling.name == 'ul':
                            li_tags = sibling.find_all('li')
                            for li_tag in li_tags:
                                t = li_tag.text.replace('\n',' ')
                                subj_paragraph.append(t + ' | ')
            except:
                pass
            subj_paragraph = ' '.join(subj_paragraph)
          

         



            #UN Sustainable Development Goals
            sdg_paragrah = []
            try:
                sdg_h2_tag = soup.find(find_h2_tag)
                p_tag = sdg_h2_tag.find_next_sibling('p')
                
                if p_tag:

                    achors = p_tag.find_all('a')
                    
                    for achor in achors:
                        sdg_paragrah.append('https://uia.org'+achor.get('href') + ' | ')
            except:
                pass
            sdg_paragrah = ' '.join(sdg_paragrah)


            #last news
            last_news_h2_tags = soup.find('h2', text='Last News')
            try:
              last_news_text = last_news_h2_tags.find_next_sibling('p').text.replace('\n',' ') #************************
            except:
                last_news_text = ''
            
            
            #contact details
            contact_list = []
            contact_h2_tags = soup.find('h2', text='Contact Details')
            try:
                if contact_h2_tags:
                    for sibling in contact_h2_tags.find_next_siblings():
                        if sibling.name == 'h2':
                            break
                        elif sibling.name == 'p':
                            # Find all <a> tags inside the <p> tag
                            if sibling.name == 'a':
                                a_tags = sibling.find_all('a')
                                for a_tag in a_tags:
                                    a = a_tag.get('href','')
                                    contact_list.append(a + ' | ')
                                
                            else:
                                contact_list.append(sibling.text.replace('\n',' ') + " ")
            except:
                pass
            contact_result = ' '.join(contact_list)
            

            writer.writerow({
                'Name': name,
                'URL': url,
                'Acronym': acrony_text,
                'Founded': founded,
                'City_HQ': city_hq,
                'Country': country,
                'Type_1': type_1,
                'Type_2': type_2,
                'UIA_ID': uia_id,
                'Founded_Text': founded_text,
                'History': history_paragraph,
                'Events': events_text,
                'Aims': aims,
                'Finance' : finance_paragraph,
                'Activity': activity_paragraph,
                'Structure': structure_paragraph,
                'Members': members_paragraph,
                'Consultative_Status': cs_paragraph,
                'Registrations': registration_paragraph,
                'Type_1_Classification': t_1_classification_paragraph,
                'Type_2_Classification': t_2_classification_paragraph,
                'Subjects': subj_paragraph,
                'UN Sustainable Development Goals': sdg_paragrah,
                'Last_News': last_news_text,
                'Contact_Details': contact_result
            })














            print({
                    'Founded_Text': founded_text,
                    'History': history_paragraph,
                    'Events': events_text,
                    'Aims': aims,
                    'Activity': activity_paragraph,
                    'Structure': structure_paragraph,
                    'Members': members_paragraph,
                    'Consultative_Status': cs_paragraph,
                    'Registrations': registration_paragraph,
                    'Type_1_Classification': t_1_classification_paragraph,
                    'Type_2_Classification': t_2_classification_paragraph,
                    'Subjects': subj_paragraph,
                    'Last_News': last_news_text,
                    'Contact_Details': contact_result
                })

            # first_h2 = soup.find('h2', text='Events')

            # # Find all the text until the next <h2> tag
            # text_between_h2_tags = []
            # current_tag = first_h2.find_next()
            # while current_tag and current_tag.name != 'h2':
            #     if isinstance(current_tag, NavigableString):
            #         text_between_h2_tags.append(str(current_tag).strip())
            #     elif hasattr(current_tag, 'text'):
            #         text_between_h2_tags.append(current_tag.text.strip())
            #     current_tag = current_tag.find_next()

            # result = ' '.join(text_between_h2_tags)
            # print(result)
            # print(result)
        #  print(events_text)
            # print(structure_paragraph)










