import Partner from "../../common/partner/Partner";
import FooterDefault from "../../footer/common-footer";
import DefaulHeader from "../../header/DefaulHeader";
import Funfact from "../../fun-fact-counter/Funfact";
import ImgBox from "./ImgBox";
import IntroDescriptions from "./IntroDescriptions";
import Breadcrumb from "../../common/Breadcrumb";
import Image from "next/image";

const index = () => {
  return (
    <>
      {/* <!-- Header Span --> */}
      <span className="header-span"></span>

      <DefaulHeader />
      {/* <!--End Main Header --> */}

      <section className="about-section-three">
        <div className="auto-container">
          <ImgBox />

          {/* <!-- Fun Fact Section --> */}
          <div className="fun-fact-section">
            <div className="row">
              <Funfact />
            </div>
          </div>
          {/* <!-- Fun Fact Section --> */}

          <IntroDescriptions />
        </div>
      </section>
      {/* <!-- End About Section Three --> */}

      <FooterDefault />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default index;
