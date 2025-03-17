import PropTypes from 'prop-types';
import FootLi from "./FootLi";
import listOfContacts from "../../constants/ListOfContacts";
import { FOOTER_ACCESSIBILITY } from "../../constants/footerConstant";

function FootUl({ className }) {
  return (
    <ul
      className={className}
      role="list"
      aria-label={FOOTER_ACCESSIBILITY.socialLinks}
    >
      {listOfContacts.map((contact) => (
        <FootLi
          key={contact.id || contact.href}
          className={contact.className}
          href={contact.href}
          icon={contact.icon}
          src={contact.src}
        />
      ))}
    </ul>
  );
}

FootUl.propTypes = {
  className: PropTypes.string
};

export default FootUl;
