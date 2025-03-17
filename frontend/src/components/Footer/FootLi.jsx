import PropTypes from "prop-types";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  FOOTER_STYLES,
  FOOTER_ACCESSIBILITY,
} from "../../constants/footerConstant";

function FootLi({
  className,
  href,
  icon,
  src,
  innerStyle = FOOTER_STYLES.iconStyle,
  ...props
}) {
  return (
    <li className={className} role="listitem">
      <a
        href={href}
        aria-label={
          icon
            ? FOOTER_ACCESSIBILITY.externalLink
            : FOOTER_ACCESSIBILITY.socialIcon
        }
        target="_blank"
        rel="noopener noreferrer"
      >
        {icon ? (
          <FontAwesomeIcon icon={icon}  aria-hidden="true" />
        ) : (
          <img
            src={src}
            style={innerStyle}
            alt={FOOTER_ACCESSIBILITY.socialIcon}
            role="img"
          />
        )}
      </a>
    </li>
  );
}

FootLi.propTypes = {
  className: PropTypes.string,
  href: PropTypes.string.isRequired,
  icon: PropTypes.object,
  src: PropTypes.string,
  innerStyle: PropTypes.object,
};

FootLi.defaultProps = {
  innerStyle: FOOTER_STYLES.iconStyle,
};

export default FootLi;
