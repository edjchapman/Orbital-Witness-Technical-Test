import React from 'react';
import './Table.css';

function Table({ data, requestSort, sortConfig }) {
  return (
    <div>
      <div className="table-title">Usage Data</div>
      <table className="table-container">
        <thead>
          <tr>
            <th>Message ID</th>
            <th>Timestamp</th>
            <th>
              <button type="button" className="sort-button" onClick={() => requestSort('report_name')}>
                Report Name
                {sortConfig.report_name === 'ascending' ? (
                  <span className="sort-arrow">↑</span>
                ) : sortConfig.report_name === 'descending' ? (
                  <span className="sort-arrow">↓</span>
                ) : (
                  ''
                )}
              </button>
            </th>
            <th>
              <button type="button" className="sort-button" onClick={() => requestSort('credits_used')}>
                Credits Used
                {sortConfig.credits_used === 'ascending' ? (
                  <span className="sort-arrow">↑</span>
                ) : sortConfig.credits_used === 'descending' ? (
                  <span className="sort-arrow">↓</span>
                ) : (
                  ''
                )}
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
    </div>
  );
}

export default Table;
