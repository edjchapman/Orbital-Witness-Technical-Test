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
    const date = new Date(item.timestamp).toLocaleDateString();
    acc[date] = (acc[date] || 0) + item.credits_used;
    return acc;
  }, {});

  const chartLabels = Object.keys(chartData);
  const chartValues = Object.values(chartData);

  return (
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
  );
}

export default Chart;
