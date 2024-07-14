import React, { useState, useEffect } from 'react';
import { Route, Routes, useLocation } from 'react-router-dom';
import Table from './components/Table';
import axios from 'axios';
import Chart from "./components/Chart";

function App() {
  const [usageData, setUsageData] = useState([]);
  const location = useLocation();
  const [isInitialLoad, setIsInitialLoad] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const params = new URLSearchParams(location.search);
        const sortCreditsUsed = params.get('sortCreditsUsed') || '';
        const sortReportName = params.get('sortReportName') || '';

        const response = await axios.get('http://127.0.0.1:8000/api/usage', {
          params: {
            sort_credits_used: sortCreditsUsed || undefined,
            sort_report_name: sortReportName || undefined,
          },
        });
        setUsageData(response.data.usage);
        setIsInitialLoad(false); // Set to false after the initial data fetch
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [location.search]);

  useEffect(() => {
    if (isInitialLoad && !location.search) {
      setIsInitialLoad(false); // Set to false immediately to prevent infinite loop
    }
  }, [location.search, isInitialLoad]);

  return (
    <div>
      <Chart data={usageData} />
      <Routes>
        <Route path="/" element={<Table data={usageData} />} />
      </Routes>
    </div>
  );
}

export default App;
