# import pandas as pd
import json 

with open('mergedData.json', 'r') as json_file:
    data = json.load(json_file)

# print(type(data))


def calculate_ratings(courses, user_preferences):
    # user_preferences is a dictionary of user preferences????
    # user_preferences = {
    #    "career": "Software Engineer",
    #    "Graduation Year": "2025",
    #    "most important": "course quality",
    # }
    
    # loop through each course in courses_df
    # calculate the weighted average of each course
    # if course quality matters the most: weighted_average = (tagged * 0.5) + (course_quality * 0.2) + (instructor_quality * 0.1) + (difficulty * 0.1) + (workload * 0.1)
    # if instructor quality matters the most: weighted_average = (tagged * 0.5) + (course_quality * 0.1) + (instructor_quality * 0.2) + (difficulty * 0.1) + (workload * 0.1)
    # if difficult: weighted_average = (tagged * 0.5) + (course_quality * 0.1) + (instructor_quality * 0.1) + (difficulty * 0.2) + (workload * 0.1)
    # if easy: weighted_average = (tagged * 0.5) + (course_quality * 0.1) + (instructor_quality * 0.1) + ((5 - difficulty) * 0.2) + (workload * 0.1)
    # if workload matters the most (more practice): weighted_average = (tagged * 0.5) + (course_quality * 0.1) + (instructor_quality * 0.1) + (difficulty * 0.1) + (workload * 0.2)
    #  if less work: weighted_average = (tagged * 0.5) + (course_quality * 0.1) + (instructor_quality * 0.1) + (difficulty * 0.1) + ((5 - workload) * 0.2)
    ratings = {}
    tagVariable = 0 
    tagCoefficient = 0.5
    courseQualityCoefficient = 0.1 
    courseQualityVariable = 0
    instructorQualityCoefficient = 0.1
    instructorQualityVariable = 0
    difficultyCoefficient = 0.1
    difficultyVariable = 0
    workloadCoefficient = 0.1
    workloadVariable = 0
    for course, info in data.items():
        # calculate weighted average
        # add to ratings dictionary
       
        if user_preferences["career"] == info["careerTags"]:
            tagVariable = 1
        if user_preferences["most important"] == "course quality":
            val = info.get("Course Quality", "N/A")
            if val == "N/A":
                courseQualityVariable = 0
            else:
                courseQualityVariable = float(info["Course Quality"])
            courseQualityCoefficient = 0.2
        elif user_preferences["most important"] == "instructor quality":
            val = info.get("Instructor Quality", "N/A")
            if val == "N/A":
                instructorQualityVariable = 0
            else:
                instructorQualityVariable = float(info["Instructor Quality"])
            instructorQualityCoefficient = 0.2
        elif user_preferences["most important"] == "difficulty":
            val = info.get("Difficulty", "N/A")
            if val == "N/A":
                difficultyVariable = 0
            else:
                difficultyVariable = float(info["Difficulty"])
            difficultyCoefficient = 0.2
        elif user_preferences["most important"] == "workload":
            val = info.get("Workload", "N/A")
            if val == "N/A":
                workloadVariable = 0
            else:
                workloadVariable = float(info["Workload"])
            workloadCoefficient = 0.2
        
        weighted_average = (tagVariable * tagCoefficient) + (courseQualityVariable * courseQualityCoefficient) + (instructorQualityVariable * instructorQualityCoefficient) + (difficultyVariable * difficultyCoefficient) + (workloadVariable * workloadCoefficient)
        ratings[course] = {}
        ratings[course]["Average"] = weighted_average
        ratings[course]["Semester Offered"] = info["Semester Offered"]
    print(ratings)
    return ratings
def get_top_courses(courses, num_courses):
    # return a list of the top num_courses courses
    sorted_courses = sorted(courses.items(), key=lambda x: x[1]['Average'], reverse=True)
    top_fall_courses = [course for course, details in sorted_courses if 'Fall' in details['Semester Offered']][:2]
    top_spring_courses = [course for course, details in sorted_courses if 'Spring' in details['Semester Offered']][:2]
    top_courses = top_fall_courses + top_spring_courses
    print(top_courses)

    return top_courses
    
def main():

    user_preferences = {
        "career": "Software Engineer",
        "Graduation Year": "2025",
        "most important": "course quality",
    }
    ave = calculate_ratings(data, user_preferences)
    get_top_courses(ave, 4)


if __name__ == '__main__':
    main()