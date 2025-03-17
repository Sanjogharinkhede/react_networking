import { useState } from 'react'
import './App.css'
import Sidebar from './components/sidebar'
import Content from './components/content'
import Footer from './components/footer'
function App() {

  return (
    <>
      <div className="mb-5">
        <div className="d-flex">
          <Sidebar />
          <Content />
        </div>
      </div>
      <Footer />
    </>
  )
}

export default App
