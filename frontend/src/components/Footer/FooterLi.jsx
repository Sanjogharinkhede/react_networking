import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";


library.add(fas, far, fab);
const iconStyle = { width: "30px", height: "30px" };
function FooterLi({
  className,
  href,
  icon,
  src,
  innerStyle = iconStyle,
  ...props
}) {
  return (
    <li className={className}>
      <a href={href}>
        {icon ? (
          <FontAwesomeIcon icon={icon} style={innerStyle}></FontAwesomeIcon>
        ) : (
          <img src={src} style={innerStyle} alt="icon" />
        )}
      </a>
    </li>
  );
}

export default FooterLi;
