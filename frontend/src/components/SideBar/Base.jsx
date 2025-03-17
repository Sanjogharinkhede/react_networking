
import { faCode, faArrowRight, faWandSparkles } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
function Sidebar() {
  return (
    <>
      <div className="sidebar">
        <h4>Networking Lab</h4>
        <a href="./py_show.html" className="btn-scripts my-md-4">
        <FontAwesomeIcon icon={faCode} className="me-2" />
           Python Scripts
           <FontAwesomeIcon icon={faArrowRight} className="ms-auto" />
        </a>

        <button id="generateJsonBtn" className="ai-button">
          <FontAwesomeIcon icon={faWandSparkles} className="me-2" />
          <span>See Magic of AI</span>
        </button>
        <div id="sidebarMenu"></div>
      </div>
      ;
    </>
  );
}

export default Sidebar;
