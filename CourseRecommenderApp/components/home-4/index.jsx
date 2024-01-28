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

      <Footer />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default index;
