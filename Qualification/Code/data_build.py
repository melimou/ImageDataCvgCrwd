import csv

#
# with open('data_full_full.csv', 'a+') as csvfile:
#     write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     root_dir = '/Users/melika/Documents/feret_db/colorferet/dvd1/data/ground_truths/xml'
#     # root_dir = '/Users/melika/Documents/feret_db/colorferet/dvd2/data/ground_truths/xml'
#     ms = 0
#     for subdir, dirs, files in os.walk(root_dir):
#         # while fs < 215:
#         for dir in dirs:
#             # print(dir)
#             xml_path = root_dir + '/' + dir + '/' + dir + '.xml'
#             # print(xml_path)
#             with open(xml_path) as f:
#                 xml_doc = xmltodict.parse(f.read())
#                 if xml_doc['Subjects']['Subject']['Gender']['@value'] == 'Male':
#                     print(dir)
#                     # write.writerow([dir, 'female'])
#                     image_root_dir = '/Users/melika/Documents/feret_db/colorferet/dvd1/data/images'
#                     # image_root_dir = '/Users/melika/Documents/feret_db/colorferet/dvd2/data/images'
#                     destination_folder = '/Users/melika/Documents/feret_db/full_full'
#                     compressed_files_path = image_root_dir + '/' + dir
#                     dirListing = os.listdir(compressed_files_path)
#                     for fff in dirListing:
#                         if ".bz2" in fff:
#                             print(fff)
#                             new_name = fff.split('.')
#                             write.writerow([new_name[0], 'male'])
#                             existing_file_path = os.path.join(compressed_files_path, fff)
#                             unpackedfile = bz2.BZ2File(existing_file_path)
#                             data = unpackedfile.read()
#                             new_file_path = os.path.join(destination_folder, fff)
#                             # print(new_file_path)
#                             with open(new_file_path, 'wb') as ff:
#                                 ff.write(data)
#                             new = destination_folder + '/' + new_name[0]
#                             # print(new)
#                             os.rename(new_file_path, new + '.jpg')
#                             os.remove(existing_file_path)
#                             # bre`ak
#                             # ms += 1
#                             # if ms > 1306:
#                             #     exit()
#






#
# with open('data_full.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     data = {rows[0]: rows[1] for rows in reader}
#
# # with open('predictions.csv', mode='r') as infile:
# #     reader = csv.reader(infile)
# #     pred = {rows[0]: rows[1] for rows in reader}
#
# dataset_size = len(data)
# true = 0
# false_female = 0
# false_male = 0
# females = 0
# males = 0
# for image, label in data.items():
#     # print(image)
#     # print(pred[image])
#     # print(label)
#     # if pred[image] == label:
#     #     true += 1
#     # if pred[image] == 'female' and label == 'male':
#     #     false_male += 1
#     # if pred[image] == 'male' and label == 'female':
#     #     false_female += 1
#     if label == 'male':
#         males += 1
#     if label == 'female':
#         females += 1
# # print((true*100.00)/dataset_size)
# print(dataset_size)
# print(females, males)
# print("Model accuracy:", (true*100.00)/dataset_size)
# print("Female prediction accuracy:", ((females-false_female)*100.00)/females)
# print("Males prediction accuracy:", ((males-false_male)*100.00)/males)


with open('data_full.csv', mode='r') as infile:
    reader = csv.reader(infile)
    data = {rows[0]: rows[1] for rows in reader}

vals = list(data.values())
print('males: ', vals.count('male'))
print('females: ', vals.count('female'))