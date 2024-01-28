# import pandas as pd
from flask import Flask, request, jsonify
import json 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open('../mergedData.json', 'r') as json_file:
    data = json.load(json_file)

# print(type(data))

def calculate_ratings(user_preferences):
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
    
    for course, info in data.items():
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
        # calculate weighted average
        # add to ratings dictionary
        # print(user_preferences["careerPath"][0]['label'])
        # print(user_preferences["careerPath"][0]['label'], info["careerTags"][0])
        if user_preferences["careerPath"][0]['label']== info["careerTags"][0]:
            # print(user_preferences["careerPath"])
            tagVariable = 5
        # print(user_preferences["categories"] == "Course Quality")
        if user_preferences["categories"] == "Course Quality":
            val = info.get("Course Quality", "N/A")
            if val == "N/A":
                courseQualityVariable = 0
            else:
                courseQualityVariable = float(info["Course Quality"])
            courseQualityCoefficient = 0.2
            
        elif user_preferences["categories"] == "Instructor Quality":
            val = info.get("Instructor Quality", "N/A")
            if val == "N/A":
                instructorQualityVariable = 0
            else:
                instructorQualityVariable = float(info["Instructor Quality"])
            instructorQualityCoefficient = 0.2
        elif user_preferences["categories"] == "Difficulty (High)":
            val = info.get("Difficulty", "N/A")
            if val == "N/A":
                difficultyVariable = 0
            else:
                difficultyVariable = float(info["Difficulty"])
            difficultyCoefficient = 0.2
        elif user_preferences["categories"] == "Difficulty (Low)":
            val = info.get("Difficulty", "N/A")
            if val == "N/A":
                difficultyVariable = 0
            else:
                difficultyVariable = 5 - float(info["Difficulty"])
            difficultyCoefficient = 0.2
        elif user_preferences["categories"] == "Workload (High)":
            val = info.get("Workload", "N/A")
            if val == "N/A":
                workloadVariable = 0
            else:
                workloadVariable = float(info["Workload"])
            workloadCoefficient = 0.2
        elif user_preferences["categories"] == "Workload (Low)":
            val = info.get("Workload", "N/A")
            if val == "N/A":
                workloadVariable = 0
            else:
                workloadVariable = 5 - float(info["Workload"])
            workloadCoefficient = 0.2
        # if "5480" in course:
        #     print("course", course)
        #     print("tagVariable", tagVariable)
        #     print("courseQualityVariable", courseQualityVariable)
        #     print("instructorQualityVariable", instructorQualityVariable)
        #     print("difficultyVariable", difficultyVariable)
        #     print("workloadVariable", workloadVariable)
        # if "5620" in course:
        #     print("course", course)
        #     print("tagVariable", tagVariable)
        #     print("courseQualityVariable", courseQualityVariable)
        #     print("instructorQualityVariable", instructorQualityVariable)
        #     print("difficultyVariable", difficultyVariable)
        #     print("workloadVariable", workloadVariable)
        weighted_average = (tagVariable * tagCoefficient) + (courseQualityVariable * courseQualityCoefficient) + (instructorQualityVariable * instructorQualityCoefficient) + (difficultyVariable * difficultyCoefficient) + (workloadVariable * workloadCoefficient)
        ratings[course] = {}
        ratings[course]["Average"] = weighted_average
        ratings[course]["Semester Offered"] = info["Semester Offered"]
        
    # print(ratings)
    return ratings


def get_top_courses(courses, graduation, current):
    # return a list of the top num_courses courses
    semester = ["24Spring", "24Fall", "25Spring", "25Fall"]
    curIdx = 0 
    gradIdx = 0
    springCount = 0
    fallCount = 0
    for i in range(len(semester)):
        if semester[i] == current:
            curIdx = i
        if semester[i] == graduation:
            gradIdx = i
    numCourses = (curIdx - gradIdx + 1) * 2 

    for season in semester[curIdx:gradIdx+1]:
        if season == "24Spring" or season == "25Spring":
            springCount += 1
        else:
            fallCount += 1    
    # if (current == graduation):
    #     numCourses = 2
    # elif (current == "24Spring" and graduation == "24Fall"
    #     or current == "24Fall" and graduation == "25Spring"
    #     or current == "25Spring" and graduation == "25SFall"):
    #     numCourses = 4
    
    # elif (current == "24Spring" and graduation == "25Spring"):
    #     numCourses = 6
    # elif (current == "24Fall" and graduation == "25Fall"):
    #     numCourses = 8
    # else:
    #     numCourses = 0
    sorted_courses = sorted(courses.items(), key=lambda x: x[1]['Average'], reverse=True)
    top_fall_courses = [course for course, details in sorted_courses if 'Fall' in details['Semester Offered']]
    # print("top fall courses", top_fall_courses)
    top_spring_courses = [course for course, details in sorted_courses if 'Spring' in details['Semester Offered']]
    # print("top spring courses", top_spring_courses)

    unique_fall_courses = top_fall_courses
    # print("unique fall courses", unique_fall_courses)
    unique_spring_courses = [course for course in top_spring_courses if course not in top_fall_courses]
    # print("unique spring courses", unique_spring_courses)

    # Select the top courses based on numCourses
    # print("numCourses", numCourses)
    selected_fall_courses = unique_fall_courses[:fallCount*2]
    # print("selected fall courses", selected_fall_courses)
    selected_spring_courses = unique_spring_courses[:springCount*2]
    # print("selected spring courses", selected_spring_courses)

    top_courses = selected_fall_courses + selected_spring_courses
    # top_courses = top_fall_courses + top_spring_courses
 
    res = {}
    for top in top_courses:
        res[top] = data[top]

    return res

# { user_preferences format 
#       careerPath,
#       currentSemester,
#       graduation,
#       categories
#     };

@app.route('/get_top_courses', methods=['POST'])
def api_get_top_courses():
    user_preferences = request.json  # Get data from POST request
    # print(data)
    # user_preferences = data.get('searchParams')
    # print(user_preferences)
    # courses = data.get('courses')

    if not user_preferences:
        return jsonify({'error': 'Missing user preferences or courses data'}), 400

    ratings = calculate_ratings(user_preferences)
    # jsonRatings = jsonify(ratings)



    # data = request.json  # Get data from POST request
    # courses = data.get('courses')

    # TODO: fix, numcourses should not be hardcoded
    # num_courses = data.get('num_courses', 4)  # Default to 4 courses

    # if not courses:
    #     return jsonify({'error': 'Missing courses data'}), 400
    # print(ratings)
    top_courses = get_top_courses(ratings, user_preferences["graduation"], user_preferences["currentSemester"])
    # print(top_courses)
    jsonTopCourses = jsonify(top_courses)
    return jsonTopCourses



    
# def main():

#     user_preferences = {
#         "career": "Software Engineer",
#         "Graduation Year": "2025",
#         "most important": "course quality",
#     }
#     ave = calculate_ratings(user_preferences)
#     get_top_courses(ave, 4)


if __name__ == '__main__':
    app.run(debug=True)
    # main()