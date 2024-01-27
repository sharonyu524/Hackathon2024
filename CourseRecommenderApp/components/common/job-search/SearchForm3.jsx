'use client'

import { useRouter } from "next/navigation";
import Select from 'react-select';
import makeAnimated from 'react-select/animated';
import { useState } from "react";
import careerOptions from '../../../data/options';



const SearchForm3 = () => {
  const router = useRouter()
  const [selectedCareerPaths, setSelectedCareerPaths] = useState([]);
  const [currentSemester, setCurrentSemester] = useState('');
  const [graduation, setGraduation] = useState('');
  const [valueMost, setValueMost] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = {
      careerPaths: selectedCareerPaths,
      currentSemester,
      graduation,
      valueMost
    };
    console.log(formData)
  };

  const handleCareerChange = (selectedOptions) => {
    setSelectedCareerPaths(selectedOptions || []);
  };

  const animatedComponents = makeAnimated();

  return (
    <form onClick={handleSubmit}>
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

        {/* <!-- Form Group --> */}
        <div className="form-group col-lg-2 col-md-12 col-sm-12 location">
          <span className="icon flaticon-map-locator"></span>
          <select value={currentSemester} className="chosen-single form-select"
            onChange={(e) => setCurrentSemester(e.target.value)}>
            <option defaultValue="" disabled selected>Current</option>
            <option defaultValue="44">24 Spring</option>
            <option defaultValue="106">24 Fall</option>
            <option defaultValue="46">25 Spring</option>
            <option defaultValue="48">25 Fall</option>
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
          <button
            type="submit"
            className="theme-btn btn-style-one"
            onClick={() => router.push("/job-list-v2")}
          >
            Get CourseList
          </button>
        </div>
      </div>
    </form>
  );
};

export default SearchForm3;
