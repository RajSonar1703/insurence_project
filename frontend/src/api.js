import axios from 'axios';

const API_BASE = "http://localhost:8000/api";

export const uploadPolicy = (file, userEmail) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('user_email', userEmail);
  return axios.post(`${API_BASE}/upload-policy`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
};

export const checkClaim = (condition) => {
  const params = new URLSearchParams({ condition });
  return axios.post(`${API_BASE}/check-claim?${params}`);
};
