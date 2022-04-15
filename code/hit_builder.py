import boto3
import xmltodict as xmltodict
import time


class Hit:
    def __init__(self, endpoint, xml_question, title, desc, reward, max_assignments):
        self.endpoint = endpoint
        self.xml_question = xml_question
        self.title = title
        self.desc = desc
        self.reward = reward
        self.max_assignments = max_assignments

        self.id = ''
        self.creation_time = ''

    # prod          access_key = AKIA2C74GNZEAZQQZ3EU       secret_key = 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
    # dev           access_key =AKIA2MBONTRUQTYESU2G        secret_key = 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

    def create(self):
        mturk = boto3.client('mturk',
                             aws_access_key_id="AKIA2C74GNZEAZQQZ3EU",
                             aws_secret_access_key="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",
                             region_name='us-east-1',
                             endpoint_url=self.endpoint
                             )
        question = open(self.xml_question, mode='r').read()
        new_hit = mturk.create_hit(
            Title=self.title,
            Description=self.desc,
            Keywords='image, category',
            Reward=self.reward,
            MaxAssignments=self.max_assignments,
            LifetimeInSeconds=604800,
            AssignmentDurationInSeconds=300,
            AutoApprovalDelayInSeconds=1,
            # AutoApprovalDelayInSeconds=1,
            Question=question,
        )
        print("*** Task created ***")
        print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
        print("HITID = " + new_hit['HIT']['HITId'])
        self.id = new_hit['HIT']['HITId']
        self.creation_time = new_hit['HIT']['CreationTime'].isoformat()
        return new_hit['HIT']['HITId']

    def result(self, hit_id):
        answers = []
        mturk = boto3.client('mturk',
                             aws_access_key_id="AKIA2MBONTRUQTYESU2G",
                             aws_secret_access_key="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",
                             region_name='us-east-1',
                             endpoint_url=self.endpoint
                             )
        worker_results = mturk.list_assignments_for_hit(HITId=hit_id)
        if worker_results['NumResults'] == self.max_assignments:
            for assignment in worker_results['Assignments']:
                xml_doc = xmltodict.parse(assignment['Answer'])
                # print(worker_results)
                # print("Worker's answer was:")
                print("$Answered")
                if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
                    # Multiple fields in HIT layout
                    for ans in xml_doc['QuestionFormAnswers']['Answer']:
                        if ans['QuestionIdentifier'] == 'gender.yes':
                            if ans['FreeText'] == 'true':
                                answers.append(True)
                            else:
                                answers.append(False)

                # else:
                #     # One field found in HIT layout
                #     print("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
                #     print("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
        else:
            print("Waiting for result...")
            list_hits = mturk.list_hits()
            # print(result('3KL228NDN6M023TD16A1JKVTOAAKGV'))
            for hit in list_hits['HITs']:
                print(hit['HITId'], hit['CreationTime'], hit['HITStatus'])
            print('-------------------------')
            time.sleep(60)
            return self.result(hit_id)

        res = self.majority_vote(answers)
        f = open('log.txt', 'a')
        f.write(self.id + '\t' + self.creation_time + '\t' + str(answers) + '\t' + 'maj_vote:' + str(res) + '\n')
        f.close()
        print(answers)
        return res

    def majority_vote(self, l):
        t, f = 0, 0
        for item in l:
            if item:
                t += 1
            else:
                f += 1
        return t > f

# test

client = boto3.client('mturk',
                             aws_access_key_id="AKIA2C74GNZEAZQQZ3EU",
                             aws_secret_access_key="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",
                             region_name='us-east-1',
                             endpoint_url='https://mturk-requester.us-east-1.amazonaws.com'
                             )
response = client.list_hits(
    MaxResults=99
)
print(response['NextToken'])
for hit in response['HITs']:
    print(hit['Reward'])

response = client.list_hits(
    NextToken = 'p2:gJDaMiwcP/w6OQ3Xahs9GO8Qg1nBrtp2XmIFqYRpWY/vYKL/H9ltw8y4B3lSiA==',
    MaxResults=99
)
print(response['NextToken'])
for hit in response['HITs']:
    print(hit['Reward'])

response = client.list_hits(
    NextToken = 'p2:TVbwmLsv2+alIAajZvT4NbPT9NammAvUtFMXvXQZHzgyPOXyDd463NNjWxSwmA==',
    MaxResults=99
)
print(response['NextToken'])
for hit in response['HITs']:
    print(hit['Reward'])