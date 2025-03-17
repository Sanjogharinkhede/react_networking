import { useState } from "react";
import "./App.css";
import Footer from './components/Footer/Base';
import  Sidebar  from "./components/SideBar/Base.jsx";
import  BaseContent  from "./components/Content/Base.jsx";
function App() {
  return (
    <>
      <div className="mb-5">
        <div className="d-flex">
          <Sidebar />
          <BaseContent />
        </div>
      </div>
      <Footer />
    </>
  );
}

export default App;
