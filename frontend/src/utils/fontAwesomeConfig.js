/**
 * @fileoverview Font Awesome icon configuration and exports
 * This file initializes Font Awesome library and exports commonly used icons
 * @module utils/fontAwesomeConfig
 * @author Sanjog Harinkhede
 */

import { library, config } from "@fortawesome/fontawesome-svg-core";
import { 
  faGithub, 
  faLinkedin, 
  faTwitter 
} from "@fortawesome/free-brands-svg-icons";
import { 
  faEnvelope, 
  faPhone ,
  faCode,
  faArrowRight
} from "@fortawesome/free-solid-svg-icons";

/**
 * @description Prevent Font Awesome from adding its CSS since we import it
 *  better to use this as it so font awesome is not added to the global css
 */

config.autoAddCss = false;

/**
 * @description Initialize Font Awesome library with specific icons
 *  Only import and add icons that are actually used in the application
 */

library.add(
  faGithub,
  faLinkedin,
  faTwitter,
  faEnvelope,
  faPhone,
  faCode,
  faArrowRight,
  faWandSparkles
);

/**
 * @description Common icons used throughout the application
 * @type {Object.<string, import('@fortawesome/fontawesome-svg-core').IconDefinition>} 
 * type of the object is IconDefinition
 */

export const SOCIAL_MEDIA_ICONS = {
  github: faGithub,
  linkedin: faLinkedin,
  twitter: faTwitter,
  email: faEnvelope,
  phone: faPhone
};

export const SCRIPT_ICONS = {
  code: faCode,
  arrowRight: faArrowRight,
  wandSparkles: faWandSparkles
};

