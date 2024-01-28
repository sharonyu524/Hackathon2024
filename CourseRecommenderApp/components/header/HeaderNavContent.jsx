"use client";

import Link from "next/link";
import { isActiveLink } from "../../utils/linkActiveChecker";
import { usePathname } from "next/navigation";

const HeaderNavContent = () => {
  return (
    <>
      <nav className="nav main-menu">
        <ul className="navigation" id="navbar">
          {/* current dropdown */}
          {/* Home link */}
          <li className={isActiveLink('/', usePathname()) ? "current" : ""}>
            <Link href="/">Home</Link> {/* Direct link to the home route */}
          </li>
          {/* End homepage menu items */}

          {/* Find Jobs link */}
          <li className={isActiveLink('/job-list-v2', usePathname()) ? "current" : ""}>
            <Link href="/job-list-v2">Browse Courses</Link> {/* Update the href to your job list route */}
          </li>
          {/* End findjobs menu items */}

          <li className={usePathname() === '/about' ? "current" : ""}>
            <Link href="/about">About Us</Link> {/* Update the href to your about route */}
          </li>
          {/* End Pages menu items */}
        </ul>
      </nav>
    </>
  );
};

export default HeaderNavContent;
