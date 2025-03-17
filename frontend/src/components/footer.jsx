import FooterUl from "./Footer/footerUl";
// import { faPhone, faEnvelope,faLinkedin } from '@fortawesome';
const leftText = "© 2025 Created with dedication and passion by";
const footerClass =
  "d-flex flex-wrap justify-content-center align-items-center fixed-bottom border-top";


function Footer(props) {
  return (
    <>
      <footer className={footerClass}>
        <div className="d-flex align-items-center">
          <span className="text-muted">
            {leftText} <strong>Sanjog Harinkhede</strong>.
          </span>
        </div>
        <FooterUl
          className="justify-content-end list-unstyled d-flex"
        />
      </footer>
    </>
  );
}

export default Footer;
