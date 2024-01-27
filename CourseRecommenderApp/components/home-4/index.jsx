import Header from "./Header";
import Footer from "./Footer";
import Hero4 from "../hero/hero-4";
import JobFilterTab from "../job-featured/JobFilterTab";
import JobCategorie1 from "../job-categories/JobCategorie1";

const index = () => {
  return (
    <>
      <Header />
      {/* <!--End Main Header --> */}

      <Hero4 />
      {/* <!-- End Banner Section--> */}

      <section className="job-categories">
        <div className="auto-container">
          <div className="sec-title text-center">
            <h2>Popular Career Paths Categories</h2>
            <div className="text">70+ Courses - 10+ Catogories</div>
          </div>

          <div
            className="row "
            data-aos="fade-up"
            data-aos-anchor-placement="top-bottom"
          >
            {/* <!-- Category Block --> */}
            <JobCategorie1 />
          </div>
        </div>
      </section>
      {/* End Job Categorie Section */}

      <Footer />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default index;
