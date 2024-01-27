'use client';

import React, { useState } from 'react';
import Categories from "../components/Categories";
import CurrentSemester from "../components/CurrentSemester";
import CareerPath from "../components/CareerPath";
import Graduation from "../components/Graduation";

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const CourseSearchForm = ({ onSearchSubmit }) => {
  const [careerPath, setCareerPath] = useState([]);
  const [currentSemester, setCurrentSemester] = useState('');
  const [graduation, setGraduation] = useState('');
  const [categories, setCategories] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const searchParams = {
      careerPath,
      currentSemester,
      graduation,
      categories
    };

    // Check if all fields are filled
    if (careerPath.length === 0 || !currentSemester || !graduation || !categories) {
      toast.error("Please enter all required fields!", {
        position: "top-center", // Using a string value instead
        autoClose: 5000
      });
      return; // Prevent form submission
    }

    // Call the parent component's submit handler with the new search parameters
    onSearchSubmit(searchParams);
  };

  return (
    <form className="job-search-form" onSubmit={handleSubmit}>
      <div className="row">
        {/* Career Path Selection */}
        <div className="form-group col-lg-3 col-md-12 col-sm-12">
          <CareerPath value={careerPath} setValue={setCareerPath} />
        </div>

        {/* Current Semester Selection */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 location">
          <CurrentSemester value={currentSemester} setValue={setCurrentSemester} />
        </div>

        {/* Graduation Selection */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 location">
          <Graduation value={graduation} setValue={setGraduation} />
        </div>

        {/* Categories Selection */}
        <div className="form-group col-lg-3 col-md-12 col-sm-12 location">
          <Categories value={categories} setValue={setCategories} />
        </div>

        {/* Submit Button */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 text-right">
          <button type="submit" className="theme-btn btn-style-one">
            Get CourseList
          </button>
        </div>
      </div>
    </form>
  );
};

export default CourseSearchForm;