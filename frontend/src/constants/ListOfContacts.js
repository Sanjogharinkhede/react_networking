/**
 * @fileoverview Contact information and social media links
 * Contains contact details and social media links for the footer
 * @description This is a constant that contains the contact information and
 * social media links for the footer
 * @author Sanjog Harinkhede
 */

import { faPhone, faEnvelope } from "@fortawesome/free-solid-svg-icons";
import { faLinkedin } from "@fortawesome/free-brands-svg-icons";

/**
 * @typedef {Object} ContactInfo
 * @property {string} className - Bootstrap classes for styling
 * @property {string} href - URL or contact information
 * @property {import('@fortawesome/fontawesome-svg-core').IconDefinition} [icon] - Font Awesome icon
 * @property {string} [src] - Image source URL for non-Font Awesome icons
 */

/** @type {ContactInfo[]} */
export const CONTACT_LIST = [
  { 
    className: "fs-4", 
    href: "tel:8827444726", 
    icon: faPhone 
  },
  {
    className: "ms-3 fs-4",
    href: "mailto:sanjogjharinkhede@gmail.com",
    icon: faEnvelope,
  },
  {
    className: "ms-3 fs-4",
    href: "https://www.linkedin.com/in/sanjogharinkhede",
    icon: faLinkedin,
  },
  {
    className: "ms-3 fs-4",
    href: "https://leetcode.com/u/sanjogharinkhede/",
    src: "https://user-images.githubusercontent.com/63964149/152531278-5e01909d-0c2e-412a-8acc-4a06863c244d.png",
  },
];

export default CONTACT_LIST;
