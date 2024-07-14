import React, { useState, useEffect, useRef } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';

function Table() {
  const location = useLocation();
  const navigate = useNavigate();
  const isInitialLoad = useRef(true);

  const getSortConfigFromURL = () => {
    const params = new URLSearchParams(location.search);
    const sortCreditsUsed = params.get('sortCreditsUsed') || '';
    const sortReportName = params.get('sortReportName') || '';
    return { credits_used: sortCreditsUsed, report_name: sortReportName };
  };

  const [data, setData] = useState([]);
  const [sortConfig, setSortConfig] = useState(getSortConfigFromURL);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/usage', {
          params: {
            sort_credits_used: sortConfig.credits_used || undefined,
            sort_report_name: sortConfig.report_name || undefined,
          },
        });
        setData(response.data.usage);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [sortConfig]);

  useEffect(() => {
    if (isInitialLoad.current) {
      isInitialLoad.current = false;
      return;
    }

    const params = new URLSearchParams(location.search);
    if (sortConfig.credits_used) {
      params.set('sortCreditsUsed', sortConfig.credits_used);
    } else {
      params.delete('sortCreditsUsed');
    }

    if (sortConfig.report_name) {
      params.set('sortReportName', sortConfig.report_name);
    } else {
      params.delete('sortReportName');
    }

    const newSearch = params.toString();
    if (location.search !== `?${newSearch}`) {
      navigate({ search: newSearch }, { replace: true });
    }
  }, [sortConfig, navigate, location.search]);

  const requestSort = key => {
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
    <table>
      <thead>
        <tr>
          <th>Message ID</th>
          <th>Timestamp</th>
          <th>
            <button type="button" onClick={() => requestSort('report_name')}>
              Report Name
            </button>
          </th>
          <th>
            <button type="button" onClick={() => requestSort('credits_used')}>
              Credits Used
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.message_id}>
            <td>{item.message_id}</td>
            <td>{item.timestamp}</td>
            <td>{item.report_name || ''}</td>
            <td>{item.credits_used.toFixed(2)}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Table;
