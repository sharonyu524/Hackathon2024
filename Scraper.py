import requests
from bs4 import BeautifulSoup
import json



def get_page(url):
    response = requests.get(url)
    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.content, "html.parser")
    return soup

#  TODO: get course descriptions for each course
def extract_course(soup):
    # filtered_courses = []
    filteredCourses = {}
    courseInfo = soup.find_all('div', class_='courseblock')
    # print(courseInfo)

    for course in courseInfo:
        courseTitle = course.find('strong').get_text()
        if int(courseTitle[4]) >= 5:
            filteredCourses[courseTitle] = {}
            courseDescription = course.find('p', class_='courseblockextra noindent').get_text()
            filteredCourses[courseTitle] = courseDescription
    print(courseInfo)

    #     courseDescription = course.find_all('p', class_='courseblockextra noindent').get_text()
    #     filteredCourses[courseTitle] = courseDescription
    
    # courseBlocks = soup.find_all('div', class_='courseblock')
    # courseTitles = soup.find_all('p', class_='courseblocktitle noindent')
    # courseTitles = soup.find_all('strong')

    # course['title'] = soup.find_all('strong')
    # course['description'] = soup.find('p').text.strip()
    # courses = [courseTitles.get_text() for courseTitles in courseTitles]
    # for course in courses:
    #     if int(course[4]) >= 5:
    #         filtered_courses.append(course)
   
    print(filteredCourses)
    with open('courseDescriptions.json', 'w') as fp:
        json.dump(filteredCourses, fp)
    # print(len(filtered_courses))
    return filteredCourses

def main():
    url = "https://catalog.upenn.edu/courses/cis/"
    soup = get_page(url)
    if soup:
        extract_course(soup)

if __name__ == '__main__':
    main()