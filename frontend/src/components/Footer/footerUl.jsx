import FooterLi from "./FooterLi";
import listOfContacts from "./ListOfContacts.js";

function FooterUl({ className,...props }) {
  return (
    <ul className="justify-content-end list-unstyled d-flex">
      {listOfContacts.map((obj, index) => (
        <FooterLi
          key={index}
          className={obj.className}
          href={obj.href}
          icon={obj.icon}
          src={obj.src}
        />
      ))}
    </ul>
  );
}

export default FooterUl;
