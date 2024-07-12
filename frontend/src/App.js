import React, { useState, useEffect } from 'react';
import Table from './components/Table';
import Chart from './components/Chart';
import axios from 'axios';

function App() {
  const [usageData, setUsageData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/usage')
      .then(response => {
        setUsageData(response.data.usage);
      });
  }, []);

  return (
    <div>
      <Chart data={usageData} />
      <Table data={usageData} />
    </div>
  );
}

export default App;
