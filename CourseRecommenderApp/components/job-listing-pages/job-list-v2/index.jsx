'use client';
import FooterDefault from "../../../components/footer/common-footer";
import DefaulHeader from "../../header/DefaulHeader";
import FilterJobsBox from "./FilterJobsBox";
import CourseSearchForm from "./CourseSearchForm";
import React, { useState } from 'react';

const index = () => {
  const [searchParams, setSearchParams] = useState({
  });

  const handleSearchSubmit = (newSearchParams) => {
    setSearchParams(newSearchParams);
  }

  return (
    <>
      {/* <!-- Header Span --> */}
      <span className="header-span"></span>

      <DefaulHeader />
      {/* End Header with upload cv btn */}

      {/* Page Title Section */}
      <section className="page-title style-two">
        <div className="auto-container">
          {/* Job Search Form */}
          <CourseSearchForm onSearchSubmit={handleSearchSubmit} />
        </div>
      </section>

      <section className="ls-section">
        <div className="auto-container">
          <div className="row">
            <div className="content-column col-lg-12 col-md-12 col-sm-12">
              <div className="ls-outer">
                <FilterJobsBox searchParams={searchParams} />
                {/* <!-- ls Switcher --> */}
              </div>
            </div>
            {/* <!-- End Content Column --> */}
          </div>
          {/* End row */}
        </div>
        {/* End container */}
      </section>
      {/* <!--End Listing Page Section --> */}

    </>
  );
};

export default index;
