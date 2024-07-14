import React, { useState, useEffect } from 'react';
import { Route, Routes, useLocation, useNavigate } from 'react-router-dom';
import Table from './components/Table';
import axios from 'axios';
import Chart from './components/Chart';
import './App.css'

function App() {
  const [usageData, setUsageData] = useState([]);
  const location = useLocation();
  const navigate = useNavigate();
  const [isInitialLoad, setIsInitialLoad] = useState(true);

  const getSortConfigFromURL = () => {
    const params = new URLSearchParams(location.search);
    const sortCreditsUsed = params.get('sortCreditsUsed') || '';
    const sortReportName = params.get('sortReportName') || '';
    return { credits_used: sortCreditsUsed, report_name: sortReportName };
  };

  const [sortConfig, setSortConfig] = useState(getSortConfigFromURL);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const params = new URLSearchParams();
        if (sortConfig.credits_used) params.set('sort_credits_used', sortConfig.credits_used);
        if (sortConfig.report_name) params.set('sort_report_name', sortConfig.report_name);

        const response = await axios.get('http://127.0.0.1:8000/api/usage', { params });
        setUsageData(response.data.usage);
        setIsInitialLoad(false);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [sortConfig]);

  useEffect(() => {
    if (isInitialLoad && !location.search) {
      setIsInitialLoad(false);
    } else if (!isInitialLoad) {
      const params = new URLSearchParams();
      if (sortConfig.credits_used) params.set('sortCreditsUsed', sortConfig.credits_used);
      if (sortConfig.report_name) params.set('sortReportName', sortConfig.report_name);

      navigate({ search: params.toString() }, { replace: true });
    }
  }, [sortConfig, navigate, location.search, isInitialLoad]);

  const requestSort = (key) => {
    const newSortConfig = { ...sortConfig };
    if (newSortConfig[key] === 'ascending') {
      newSortConfig[key] = 'descending';
    } else if (newSortConfig[key] === 'descending') {
      newSortConfig[key] = '';
    } else {
      newSortConfig[key] = 'ascending';
    }
    setSortConfig(newSortConfig);
  };

  return (
      <div className="page-container">
        <Chart data={usageData}/>
        <Routes>
          <Route path="/" element={<Table data={usageData} requestSort={requestSort} sortConfig={sortConfig}/>}/>
        </Routes>
      </div>
  );
}

export default App;
