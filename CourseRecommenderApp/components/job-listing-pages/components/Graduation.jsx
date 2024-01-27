'use client';

import React from 'react';

const Graduation = ({ value, setValue }) => {
    return (
        <>
            <select
                value={value}
                className="chosen-single form-select"
                onChange={(e) => setValue(e.target.value)}
            >
                <option value="" disabled>Graduation</option>
                <option value="24Spring">24 Spring</option>
                <option value="24Fall">24 Fall</option>
                <option value="25Spring">25 Spring</option>
                <option value="25Fall">25 Fall</option>
            </select>
            <span className="icon flaticon-open-magazine"></span>
        </>
    );
};

export default Graduation;

