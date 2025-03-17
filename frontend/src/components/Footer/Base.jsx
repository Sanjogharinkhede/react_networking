import PropTypes from 'prop-types';
import FootUl from "./FootUl";
import { FOOTER_STYLES } from "../../constants/footerConstant";

function Footer() {
  return (
    <footer 
      className={FOOTER_STYLES.footerClass}
      role="contentinfo"
    >
      <div className="d-flex align-items-center">
        <span className="text-muted">
          {FOOTER_STYLES.leftText} <strong>Sanjog Harinkhede</strong>.
        </span>
      </div>
      <FootUl
        className="justify-content-end list-unstyled d-flex"
      />
    </footer>
  );
}

Footer.propTypes = {};

export default Footer;

