

'use client'

import Link from "next/link";
import React, { useState, useEffect } from 'react';
import { getCourses } from "@/api/courses";

import Image from "next/image";

const FilterJobsBox = ({ searchParams }) => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    const fetchCourses = async () => {
      console.log('searchParams', searchParams)
      try {
        const fetchedCourses = searchParams ? await getCourses(searchParams) : await getCourses();
        setCourses(Object.entries(fetchedCourses));
        console.log('fetchedCourses', fetchedCourses)
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    };

    fetchCourses();
  }, [searchParams]);

  const getDifficultyClass = (value) => {
    if (value >= 0 && value < 2) {
      return "privacy"
    } else if (value < 3.5) {
      return "required"
    } return "bad"
  }

  const getQualityClass = (value) => {
    if (value >= 0 && value < 2.5) {
      return "bad"
    } else if (value < 3.5) {
      return "required"
    } return "privacy"
  }
  // privacy: green
  // bad: red
  // required: yellow


  return (
    <div className="course-list">

      {courses.map(([courseName, courseDetails], index) => (
        <div className="job-block" key={index}>
          <div className="inner-box">
            <div className="content">

              <h4>
                <Link href={`https://penncoursereview.com${courseDetails["Link"]}`}>{courseName}</Link>
              </h4>

              {/* Semester Offered */}
              {courseDetails["Semester Offered"] && (
                <ul className="job-other-info" style={{ display: 'flex', flexWrap: 'wrap' }}>
                  Semester Offered:
                  {courseDetails["Semester Offered"].map((semester, semesterIndex) => (
                    <li key={semesterIndex} className="semester">{semester}</li>
                  ))}
                </ul>
              )}

              {/* Display Career Tags only if they exist */}
              {courseDetails.careerTags && courseDetails.careerTags.length > 0 && (
                <ul className="job-other-info" style={{ display: 'flex', flexWrap: 'wrap' }}>
                  Related Career Path:
                  {courseDetails.careerTags.map((tag, tagIndex) => (
                    <li key={tagIndex} className="time">{tag}</li>
                  ))}
                </ul>
              )}

              <p>{courseDetails.description}</p>

              <ul className="job-other-info" style={{ display: 'flex', justifyContent: 'space-evenly' }}>
                <li className={getQualityClass(courseDetails["Course Quality"])}>
                  <span className="icon flaticon-star"></span>
                  Course Quality: {courseDetails["Course Quality"]}
                </li>
                {/* compnay info */}
                <li className={getQualityClass(courseDetails["Instructor Quality"])}>
                  <span className="icon flaticon-man"></span>
                  Instructor Quality: {courseDetails["Instructor Quality"]}
                </li>
                {/* location info */}
                <li className={getDifficultyClass(courseDetails.Difficulty)}>
                  <span className="icon flaticon-notebook"></span>
                  Difficulty: {courseDetails.Difficulty}
                </li>
                {/* time info */}
                <li className={getDifficultyClass(courseDetails.Workload)}>
                  <span className="icon flaticon-clock-3"></span>
                  Workload: {courseDetails.Workload}
                </li>
                {/* salary info */}
              </ul>
              {/* End .job-info */}

            </div>
          </div>
        </div>
        // End all jobs


      ))}

    </div>);
};

export default FilterJobsBox;
