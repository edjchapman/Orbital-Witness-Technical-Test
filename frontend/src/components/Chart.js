import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';
import './Chart.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function Chart({ data }) {
  const chartData = data.reduce((acc, item) => {
    acc[item.timestamp] = (acc[item.timestamp] || 0) + item.credits_used;
    return acc;
  }, {});

  // Ensure the chart data is sorted by timestamp
  const chartLabels = Object.keys(chartData).sort((a, b) => new Date(a) - new Date(b));
  const chartValues = chartLabels.map(label => chartData[label]);

  return (
    <div>
      <div className="chart-title">Usage Chart</div>
      <Bar
        data={{
          labels: chartLabels,
          datasets: [
            {
              label: 'Credits Used',
              data: chartValues,
              backgroundColor: 'rgba(75,192,192,1)',
            },
          ],
        }}
        options={{
          scales: {
            x: {
              title: {
                display: true,
                text: 'Date',
              },
            },
            y: {
              title: {
                display: true,
                text: 'Credits',
              },
            },
          },
        }}
      />
    </div>
  );
}

export default Chart;
