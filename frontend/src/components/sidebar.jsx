function Sidebar() {
  return (
    <>
      <div className="sidebar">
        <h4>Networking Lab</h4>
        <a href="./py_show.html" className="btn-scripts my-md-4">
          <i className="fas fa-code me-2"></i> Python Scripts
          <i className="fas fa-arrow-right ms-auto"></i>
        </a>

        <button id="generateJsonBtn" className="ai-button">
          <i className="fas fa-wand-magic-sparkles"></i>
          <span>See Magic of AI</span>
        </button>
        <div id="sidebarMenu"></div>
      </div>
      ;
    </>
  );
}

export default Sidebar;
