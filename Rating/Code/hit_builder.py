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

    def create(self):
        access_key_id = 'AKIA2MBONTRUT5ZPA67D'
        secret_access_key = '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'



        mturk = boto3.client('mturk',
                             aws_access_key_id=access_key_id,
                             aws_secret_access_key=secret_access_key,
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
            QualificationRequirements=[
                {
                    'QualificationTypeId': '00000000000000000040',
                    'Comparator': 'GreaterThanOrEqualTo',
                    'IntegerValues': [
                        1,
                    ],
                    'ActionsGuarded': 'Accept'
                },
                {
                    'QualificationTypeId': '000000000000000000L0',
                    'Comparator': 'GreaterThanOrEqualTo',
                    'IntegerValues': [
                        95,
                    ],
                    'ActionsGuarded': 'Accept'
                },
            ]
        )
        print("*** Task created ***")
        # print("https://worker.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
        print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
        print("HITID = " + new_hit['HIT']['HITId'])
        self.id = new_hit['HIT']['HITId']
        self.creation_time = new_hit['HIT']['CreationTime'].isoformat()
        return new_hit['HIT']['HITId']

    def result(self, hit_id):
        answers = []
        access_key_id = 'AKIA2MBONTRUT5ZPA67D'
        secret_access_key = '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'
        mturk = boto3.client('mturk',
                             aws_access_key_id=access_key_id,
                             aws_secret_access_key=secret_access_key,
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
            time.sleep(15)
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

