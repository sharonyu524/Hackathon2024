

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
        const fetchedCourses = await getCourses(searchParams);
        setCourses(Object.entries(fetchedCourses));
      } catch (error) {
        console.error('Error fetching courses:', error);
      }
    };

    if (searchParams) {
      fetchCourses();
    }
  }, [searchParams]);

  const getDifficultyClass = (value) => {
    if (value >= 0 && value < 2.5) {
      return "privacy"
    } else if (value < 3.5) {
      return "required"
    } return "time"
  }

  const getQualityClass = (value) => {
    if (value >= 0 && value < .5) {
      return "time"
    } else if (value < 3.5) {
      return "required"
    } return "privacy"
  }
  // privacy: green
  // time: red
  // required: yellow


  return (
    <div className="course-list">
      {courses.map(([courseName, courseDatails], index) => (
        <div className="job-block" key={index}>
          <div className="inner-box">
            <div className="content">

              <h4>
                <Link href={`https://penncoursereview.com${courseDatails["Link"]}`}>{courseName}</Link>

              </h4>

              {/* Career Tags */}
              <ul className="job-other-info" style={{ display: 'flex', flexWrap: 'wrap' }}>
                Related Career Path: {courseDatails.careerTags.map((tag, tagIndex) => (
                  <li key={tagIndex} className="career">{tag}</li>
                ))}
              </ul>

              <p>{courseDatails.description}</p>

              <ul className="job-other-info" style={{ display: 'flex', justifyContent: 'space-evenly' }}>
                <li className={getQualityClass(courseDatails["Course Quality"])}>
                  <span className="icon flaticon-star"></span>
                  Course Quality: {courseDatails["Course Quality"]}
                </li>
                {/* compnay info */}
                <li className={getQualityClass(courseDatails["Instructor Quality"])}>
                  <span className="icon flaticon-man"></span>
                  Instructor Quality: {courseDatails["Instructor Quality"]}
                </li>
                {/* location info */}
                <li className={getDifficultyClass(courseDatails.Difficulty)}>
                  <span className="icon flaticon-notebook"></span>
                  Difficulty: {courseDatails.Difficulty}
                </li>
                {/* time info */}
                <li className={getDifficultyClass(courseDatails.Workload)}>
                  <span className="icon flaticon-clock-3"></span>
                  Workload: {courseDatails.Workload}
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
