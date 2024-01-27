import Image from "next/image";
import FooterContent3 from "../footer/FooterContent3";

const Footer = () => {
  return (
    <footer
      className="main-footer style-three"
      style={{ backgroundImage: "url(/images/background/3.png)" }}
    >
      <div className="auto-container">
        {/* <!--Widgets Section--> */}
        <div className="widgets-section" data-aos="fade-up">
          <div className="row">
            <div className="big-column col-xl-3 col-lg-3 col-md-12">
              <div className="footer-column about-widget">
                <div className="logo">
                  <a href="#">
                    <Image
                      width={154}
                      height={50}
                      src="/images/penn.png"
                      alt="brand"
                    />
                  </a>
                </div>
                <p className="phone-num">
                  <span>Contact us </span>
                </p>
                <p className="address">
                  <a href="mailto:support@superio.com" className="email">
                    gablyu@seas.upenn.edu
                    sharonyu@seas.upenn.edu
                  </a>
                </p>
              </div>
            </div>
            {/* End footer address left widget */}

            <div className="big-column col-xl-9 col-lg-9 col-md-12">
              <div className="row">
                <FooterContent3 />
              </div>
              {/* End .row */}
            </div>
            {/* End col-xl-8 */}
          </div>
        </div>
      </div>
      {/* End auto-container */}
      {/* <!--Bottom--> */}
    </footer>
  );
};

export default Footer;
