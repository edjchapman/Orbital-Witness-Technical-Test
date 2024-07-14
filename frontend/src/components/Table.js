import React from 'react';

function Table({ data, requestSort, sortConfig }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Message ID</th>
          <th>Timestamp</th>
          <th>
            <button type="button" onClick={() => requestSort('report_name')}>
              Report Name {sortConfig.report_name === 'ascending' ? '↑' : sortConfig.report_name === 'descending' ? '↓' : ''}
            </button>
          </th>
          <th>
            <button type="button" onClick={() => requestSort('credits_used')}>
              Credits Used {sortConfig.credits_used === 'ascending' ? '↑' : sortConfig.credits_used === 'descending' ? '↓' : ''}
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
