import { useState, useEffect } from 'react';

const Intake = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const apiEndpoint = 'https://2f9k8s82s6.execute-api.us-east-2.amazonaws.com/prod';
    const apiKey = '20O25PMjVS7P7VRUAtmHaR6NLkkxWPt6OP1hSwS4'; // replace with your actual API key

    fetch(apiEndpoint, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
        // Or, if the API expects the key under a different header, like 'X-API-KEY':
        // 'X-API-KEY': apiKey
      }
    })
    .then(response => response.json())
    .then(data => setData(data))
    .catch(error => console.error('Error:', error));
  }, []);


  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Column 1</th>
            <th>Column 2</th>
            {/* Add more column headers as necessary */}
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item}</td>
              
              {/* Add more cells as necessary */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Intake;
