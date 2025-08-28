// src/App.js
import React, { useState } from 'react';
import { uploadPolicy, checkClaim } from './api';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [file, setFile] = useState(null);
  const [userEmail, setUserEmail] = useState('');
  const [condition, setCondition] = useState('');
  const [result, setResult] = useState(null);
  const [uploadMessage, setUploadMessage] = useState('');

  const handleUpload = async () => {
    if (!file || !userEmail) return;
    try {
      const response = await uploadPolicy(file, userEmail);
      setUploadMessage(response.data.message);
    } catch (err) {
      setUploadMessage('Upload failed');
    }
  };

  const handleCheckClaim = async () => {
    if (!condition) return;
    try {
      const response = await checkClaim(condition);
      setResult(response.data);
    } catch (err) {
      setResult({ error: 'Check failed' });
    }
  };

  return (
    <div className="container-fluid bg-light min-vh-100 d-flex flex-column">
      <header className="bg-primary text-white text-center py-4 shadow">
        <h1>Insurease Claim Portal</h1>
        <p>Upload your policy and check eligibility in seconds</p>
      </header>

      <main className="flex-grow-1">
        <div className="container mt-5">
          <div className="row mb-4">
            <div className="col-md-6">
              <h4>Upload Policy PDF</h4>
              <input type="file" className="form-control mb-2" onChange={(e) => setFile(e.target.files[0])} />
              <input type="email" className="form-control mb-2" placeholder="Your Email" value={userEmail} onChange={(e) => setUserEmail(e.target.value)} />
              <button className="btn btn-success" onClick={handleUpload}>Upload</button>
              {uploadMessage && <div className="alert alert-info mt-3">{uploadMessage}</div>}
            </div>

            <div className="col-md-6">
              <h4>Check Claim Eligibility</h4>
              <input type="text" className="form-control mb-2" placeholder="Enter condition (e.g. cataract)" value={condition} onChange={(e) => setCondition(e.target.value)} />
              <button className="btn btn-primary" onClick={handleCheckClaim}>Check</button>
              {result && (
                <div className="alert alert-secondary mt-3">
                  <strong>Condition:</strong> {result.condition || '—'}<br />
                  <strong>Eligible:</strong> {result.eligible || '—'}<br />
                  <strong>Reason:</strong> {result.reason || result.error || '—'}
                </div>
              )}
            </div>
          </div>
        </div>
      </main>

      <footer className="bg-dark text-white text-center py-3">
        <p className="mb-0">&copy; 2025 Insurease - Built for Bajaj Hackathon</p>
      </footer>
    </div>
  );
}

export default App;
