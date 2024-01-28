import json


description = 'courseDescriptions.json'
careerTags = 'careerTags.json'
ratings = 'courseRatings.json'

def get_descriptions(json_file_path):
    keys = []
    try:
        with open(description, 'r') as json_file:
        
            descriptionData = json.loads(json_file.read())
            # print(descriptionData.keys())
            # for key in descriptionData.keys():

            #     key.split(' ')
            #     print(key)
            # print(len(descriptionData))
            return descriptionData
    except FileNotFoundError:
        print(f"The file does not exist.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_careerTags(json_file_path):
    try:
        with open(careerTags, 'r') as json_file:
        
            careerTagsData = json.loads(json_file.read())
            
            # print(len(careerTagsData))
            return careerTagsData
    except FileNotFoundError:
        print(f"The file does not exist.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_ratings(json_file_path): 
    try:
        with open(ratings, 'r') as json_file:
        
            ratingData = json.loads(json_file.read())
            print(len(ratingData))
            return ratingData
    except FileNotFoundError:
        print(f"The file does not exist.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def merge_data(descriptionData, careerTagsData, ratingData):
    # TODO: complete this function
    mergedData = {}
    for course, description in descriptionData.items():
        mergedData[course] = {}
        mergedData[course]['description'] = description['Description']
        mergedData[course]['careerTags'] = careerTagsData[course]
        mergedData[course]['Semester Offered'] = description['Semester Offered']
    # print(mergedData)

    for code, rating in ratingData.items():
        print (code)
        for title, description in mergedData.items():
            print(title)
            print(title[4:8])
            if code in title[4:8]:
                mergedData[title]['Link'] = rating['Link']
                mergedData[title]['Course Quality'] = rating['Course Quality'] 
                mergedData[title]['Instructor Quality'] = rating['Instructor Quality']
                mergedData[title]['Difficulty'] = rating['Difficulty']
                mergedData[title]['Workload'] = rating['Workload']
            # print (mergedData[title])
    return mergedData

def find_all_tags(dict):
    tags = set()
    for course, tag in dict.items():
        tags.add(tag[0])
    
    print(tags)
    # return tags
def write_to_json(mergedData):
    with open('mergedData.json', 'w') as fp:
        json.dump(mergedData, fp)
     

    # # return mergedData
    #     # mergedData[course]['ratings'] = ratingData[course]

def main():
    
    # finalData = merge_data(get_descriptions(description), get_careerTags(careerTags), get_ratings(ratings))
    # write_to_json(finalData)
    find_all_tags(get_careerTags(careerTags))

if __name__ == '__main__':
    main()

# with open(careerTags, 'r') as json_file:
#     careerTagsData = json.load(json_file)

# with open(ratings, 'r') as json_file:
#     ratingData = json.load(json_file)



# print(len(careerTagsData))
# print(len(ratingData))