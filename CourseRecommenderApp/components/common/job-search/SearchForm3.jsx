'use client'

import { useRouter } from "next/navigation";
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
import { useState } from "react";
import careerOptions from '../../../data/options';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { getCourses } from '@/api/courses';



const SearchForm3 = () => {
  const router = useRouter()
  const [selectedCareerPaths, setSelectedCareerPaths] = useState([]);
  const [currentSemester, setCurrentSemester] = useState('');
  const [graduation, setGraduation] = useState('');
  const [valueMost, setValueMost] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Check if all fields are filled
    if (selectedCareerPaths.length === 0 || !currentSemester || !graduation || !valueMost) {
      toast.error("Please enter all required fields!", {
        position: "top-center",
        autoClose: 5000
      });
      return;
    }

    const formData = {
      careerPaths: selectedCareerPaths.map(option => option.value),
      currentSemester,
      graduation,
      valueMost
    };

    console.log(formData)

    try {
      const courseList = await getCourses(formData);
      // Assuming you have a way to pass this data to the course list page
      // For example, you might use a global state, context, or another method
      router.push("/job-list-v2"); // Navigate to course list page
    } catch (error) {
      toast.error("An error occurred while fetching courses.");
      console.error('Error fetching courses:', error);
    }

  };

  const handleCareerChange = (selectedOptions) => {
    setSelectedCareerPaths(selectedOptions || []);
  };

  const animatedComponents = makeAnimated();

  return (
    <form onSubmit={handleSubmit}>
      <div className="row">
        {/* <!-- Form Group --> */}
        {/* Multi-selectable dropdown for Career Path */}
        <div className="form-group col-lg-3 col-md-12 col-sm-12 location">
          <span className="icon flaticon-briefcase"></span>
          <Select
            components={animatedComponents}
            isMulti
            options={careerOptions}
            value={selectedCareerPaths}
            onChange={handleCareerChange}
            className="basic-multi-select"
            classNamePrefix="select"
          />
        </div>

        <div className="form-group col-lg-2 col-md-12 col-sm-12 location">
          <span className="icon flaticon-map-locator"></span>
          <select
            value={currentSemester}
            onChange={(e) => setCurrentSemester(e.target.value)}
            className="chosen-single form-select"
          >
            <option value="" disabled>{currentSemester ? currentSemester : "Current"}</option>
            <option value="44">24 Spring</option>
            <option value="106">24 Fall</option>
            <option value="46">25 Spring</option>
            <option value="48">25 Fall</option>
          </select>
        </div>


        {/* <!-- Form Group --> */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 location">
          <span className="icon flaticon-open-magazine"></span>
          <select className="chosen-single form-select"
            onChange={(e) => setGraduation(e.target.value)}>
            <option defaultValue="" disabled selected>Graduation</option>
            <option defaultValue="44">24 Spring</option>
            <option defaultValue="106">24 Fall</option>
            <option defaultValue="46">25 Spring</option>
            <option defaultValue="48">25 Fall</option>
          </select>
        </div>

        {/* <!-- Form Group --> */}
        <div className="form-group col-lg-3 col-md-12 col-sm-12 category">
          <span className="icon flaticon-star"></span>
          <select className="chosen-single form-select"
            onChange={(e) => setValueMost(e.target.value)}>
            <option defaultValue="" disabled selected>What I value the most</option>
            <option defaultValue="44">Workload (Low)</option>
            <option defaultValue="106">Workload (high)</option>
            <option defaultValue="46">Difficulty (Low)</option>
            <option defaultValue="48">Difficulty (High)</option>
            <option defaultValue="47">Instructor Quality</option>
            <option defaultValue="45">Course Quality</option>
          </select>
        </div>

        {/* <!-- Form Group --> */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 text-right">
          <button type="submit" className="theme-btn btn-style-one">
            Get CourseList
          </button>
        </div>
      </div>
    </form>
  );
};

export default SearchForm3;