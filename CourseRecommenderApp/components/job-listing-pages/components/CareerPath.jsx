'use client';

import React from 'react';
import makeAnimated from 'react-select/animated';
import Select from 'react-select';
import careerOptions from "@/data/options";

const CareerPath = ({ value, setValue }) => {
    const animatedComponents = makeAnimated();

    const handleCareerChange = (selectedOptions) => {
        setValue(selectedOptions || []);
        console.log(selectedOptions);
    };

    return (
        <>
            <Select
                components={animatedComponents}
                isMulti
                options={careerOptions}
                value={value}
                onChange={handleCareerChange}
                className="basic-multi-select"
                classNamePrefix="select"
            />
            <span className="icon flaticon-briefcase"></span>
        </>
    );
};

export default CareerPath;
