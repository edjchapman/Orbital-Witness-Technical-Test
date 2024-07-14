import React, { useState } from 'react';

function Table({ data }) {
  const [sortConfig, setSortConfig] = useState({ key: 'credits_used', direction: 'ascending' });

  const sortedData = React.useMemo(() => {
    let sortableData = [...data];
    if (sortConfig !== null) {
      sortableData.sort((a, b) => {
        if (a[sortConfig.key] < b[sortConfig.key]) {
          return sortConfig.direction === 'ascending' ? -1 : 1;
        }
        if (a[sortConfig.key] > b[sortConfig.key]) {
          return sortConfig.direction === 'ascending' ? 1 : -1;
        }
        return 0;
      });
    }
    return sortableData;
  }, [data, sortConfig]);

  const requestSort = key => {
    let direction = 'ascending';
    if (sortConfig.key === key && sortConfig.direction === 'ascending') {
      direction = 'descending';
    }
    setSortConfig({ key, direction });
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
        {sortedData.map((item) => (
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
