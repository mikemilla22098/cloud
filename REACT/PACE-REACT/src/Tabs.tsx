import React, { useState } from "react";
import Intake from "./Intake";

const Tabs = () => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div>
      <div>
        <button onClick={() => setActiveTab(0)}>Intake</button>
        <button onClick={() => setActiveTab(1)}>Scheduled</button>
        <button onClick={() => setActiveTab(2)}>Completed</button>
      </div>
      
      <div>
        {activeTab === 0 && <div><Intake /></div>}
        {activeTab === 1 && <div>Content for Tab 2</div>}
        {activeTab === 2 && <div>Content for Tab 3</div>}
      </div>
    </div>
  );
};

export default Tabs;
