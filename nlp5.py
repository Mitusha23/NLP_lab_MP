"""
Name :Mitusha Pawar
Roll No :44
Batch :B3 
Pract no 5: Implement Regular Expression Function to fing URL,
IP address,Date,PAN Number in textual data using python library

"""
import re

def find_entities(text):

    result = {
        'URLs': re.findall(r'https?://\S+|www\.\S+', text),
        'Us Number': re.findall(r'[+]{1}[1]{1}[0-9]{10}', text),
        'Dates': re.findall(r'[0-9]{2}[-]{1}[0-9]{2}[-]{1}[0-9]{4}', text),
        'UPI id': re.findall(r'[0-9]{10}[@]{1}[a-z]{3}', text),
        'Seat no': re.findall(r'[A-Z]{2}[0-9]{5}',text),

    }
    return result

# Example usage:
sample_text = """
First Dataset
Visit our website at https://www.google.com.
For support, contact us at support@example.com.
Us Number:+14345678912
Date: 11-22-2023
UPI id:9371678021@ybl
Seat no:DO85677

: 

Second Dataset
Visit our website at https://www.youtube.com.
For more info connect with  info@example.com.
IP address: +14545768889
Date: 30-10-2023
UPI id:9881235104@ibl
Seat no:AO23249
"""

result = find_entities(sample_text)

for entity_type, entities in result.items():
    print(f"{entity_type}: {entities}")


"""
Output:

URLs: ['https://www.google.com.', 'https://www.youtube.com.']
Us Number: ['+14345678912', '+14545768889']
Dates: ['11-22-2023', '30-10-2023']
UPI id: ['9371678021@ybl', '9881235104@ibl']
Seat no: ['DO85677', 'AO23249']

"""