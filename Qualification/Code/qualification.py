import datetime

import boto3




# q ID = 367CUFXBXYGAHN6V9D61W56SUZNA1X

# 3YKCTFUEVZQVCSFM7XSFJLH5WSM7NB


# last: 3RESO6GZA5S0VLZNH8JE5E93OJ9HHE



# Create a client for the Amazon Mechanical Turk API
endpoint = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
prod = 'https://mturk-requester.us-east-1.amazonaws.com'
# access_key_id = ''
# secret_access_key = ''

access_key_id = 'AKIA2MBONTRUT5ZPA67D'
secret_access_key = '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'

client = boto3.client('mturk',
                      aws_access_key_id=access_key_id,
                      aws_secret_access_key=secret_access_key,
                      region_name='us-east-1',
                      endpoint_url=endpoint)

# Define the qualification name and description
qual_name = "Image-Gender-Identification/"
qual_description = "This qualification tests your ability to label images with the correct gender of the person."

# Define the qualification question schema in QuestionFormat
qual_question = """<?xml version="1.0" encoding="UTF-8"?>
<QuestionForm xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd">
<Overview>
<Title>Image Labeling Qualification</Title>
<Text>This qualification tests your ability to label images with the correct gender of the person.</Text>
<Text>Is there a female in this set of images? Answer with "Yes" or "No".</Text>
<Text>You need to answer all the questions correctly to pass this qualification.</Text>
</Overview>
<Question>
<QuestionIdentifier>Q1</QuestionIdentifier>
<IsRequired>true</IsRequired>
<QuestionContent>
<FormattedContent><![CDATA[
<table>
<tr>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00096_940128_fa.jpeg"  alt="Image 3" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00708_941201_rc.jpeg"  alt="Image 4" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00708_960530_re.jpeg"  alt="Image 3" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00341_940422_hr.jpeg"  alt="Image 4" width="100%" height="300" /></td>
</tr>
<tr>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00462_940422_pr_a.jpeg"  alt="Image 4" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00497_940519_qr.jpeg"  alt="Image 3" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00587_940928_fb.jpeg"  alt="Image 4" width="100%" height="300" /></td>
<td><img src="https://cov-img.s3.amazonaws.com/feret-full/00630_941121_fa.jpeg"  alt="Image 3" width="100%" height="300" /></td>

</tr>
</table>
]]></FormattedContent>
</QuestionContent>
<AnswerSpecification>
<SelectionAnswer>
<StyleSuggestion>radiobutton</StyleSuggestion>
<Selections>
<Selection>
<SelectionIdentifier>Yes</SelectionIdentifier>
<Text>Yes</Text>
</Selection>
<Selection>
<SelectionIdentifier>No</SelectionIdentifier>
<Text>No</Text>
</Selection>
</Selections>
</SelectionAnswer>
</AnswerSpecification>
</Question>
<!-- Repeat for other questions -->
</QuestionForm>"""

# Define the qualification answer key schema in AnswerKeyFormat
qual_answer_key = """<?xml version="1.0" encoding="UTF-8"?>
<AnswerKey xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd">
<Question>
<QuestionIdentifier>Q1</QuestionIdentifier>
<AnswerOption>
<SelectionIdentifier>Yes</SelectionIdentifier>
<AnswerScore>100</AnswerScore> <!-- Correct answer gets 1 point -->
</AnswerOption>
<AnswerOption>
<SelectionIdentifier>No</SelectionIdentifier>
<AnswerScore>0</AnswerScore> <!-- Incorrect answer gets 0 points -->
</AnswerOption>
</Question>
<!-- Repeat for other questions -->
</AnswerKey>"""

# Create the qualification type using the client object
response = client.create_qualification_type(
    Name=qual_name,
    Description=qual_description,
    QualificationTypeStatus='Active',  # Set the status to active so workers can request it
    Test=qual_question,  # Set the test parameter to the question schema
    AnswerKey=qual_answer_key,  # Set the answer key parameter to the answer key schema
    TestDurationInSeconds=300,  # Set the test duration to 5 minutes (300 seconds)
)

# Get the qualification type ID from the response
qual_type_id = response['QualificationType']['QualificationTypeId']

# Print the qualification type ID
print(f"Qualification type ID: {qual_type_id}")


# response = client.list_workers_with_qualification_type(
#     QualificationTypeId='3YKCTFUEVZQVCSFM7XSFJLH5WSM7NB',
#     Status='Granted',
# )
#
# print(response)

#
# response = client.list_qualification_types(
#     Query='Master',
#     MustBeRequestable=False,
#     MustBeOwnedByCaller=False,
# )
#
# qualifications = []
#
# # Loop through the qualification types in the response
# for qual in response['QualificationTypes']:
#     qual_dict = {}
#     # Add the QualificationTypeId to the dictionary
#     qual_dict['QualificationTypeId'] = qual['QualificationTypeId']
#     # Add the Description to the dictionary
#     qual_dict['Description'] = qual['Description']
#     # Add the QualificationTypeStatus to the dictionary
#     qual_dict['QualificationTypeStatus'] = qual['QualificationTypeStatus']
#     # Add the IsRequestable to the dictionary
#     qual_dict['IsRequestable'] = qual['IsRequestable']
#     # Add the AutoGranted to the dictionary
#     qual_dict['AutoGranted'] = qual['AutoGranted']
#     # Append the dictionary to the list
#     qualifications.append(qual_dict)
#
# # Print the list of qualifications
# for q in qualifications:
#     print(q)

# {'QualificationTypeId': '3JC3H4XMUAV4AV1ERBRYYG7HCYY3CB', 'Description': 'Label each person image based on their gender', 'QualificationTypeStatus': 'Active', 'IsRequestable': True, 'AutoGranted': False}
# {'QualificationTypeId': '3V2N8HP7QX3JIIB5601F05NBLQIDB7', 'Description': 'Label each person image based on their gender', 'QualificationTypeStatus': 'Active', 'IsRequestable': True, 'AutoGranted': False}
# {'QualificationTypeId': '33206IYBCSFMXN73YAQZPNNZYJ6449', 'Description': 'Label each person image as either: Male, Female', 'QualificationTypeStatus': 'Active', 'IsRequestable': True, 'AutoGranted': False}
# {'QualificationTypeId': '32DH4YCIPI6SYC48QO1ABEGPBF7YJN', 'Description': 'Label each person image with your best guess for gender', 'QualificationTypeStatus': 'Active', 'IsRequestable': True, 'AutoGranted': False}
# {'QualificationTypeId': '332K4KOFDKMQKOT8JBBLJSKA6YE0DC', 'Description': 'Label each person image with the most likely gender', 'QualificationTypeStatus': 'Active', 'IsRequestable': True, 'AutoGranted': False}


# response = client.list_workers_with_qualification_type(
# QualificationTypeId='2F1QJWKUDD8XADTFD2Q0G6UTO95ALH',
# Status='Granted')
#
# # Print the response
# print(response)

# response = client.associate_qualification_with_worker(
#     QualificationTypeId='2ARFPLSP75KLA8M8DH1HTEQVJT3SY6',
#     WorkerId='A2NLC4HSEZ4U81',
#     # IntegerValue=123,
#     SendNotification=True
# )