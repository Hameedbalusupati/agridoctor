import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import { useEffect, useState } from 'react';
import api from './services/api';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ProtectedRoute from './components/ProtectedRoute';
import CameraScanner from './components/CameraScanner';
import { AuthProvider, useAuth } from './context/AuthContext';

function LandingPage() {
  return (
    <div className="page-shell">
      <section className="hero card">
        <div>
          <p className="eyebrow">Smart farming for Indian farmers</p>
          <h1>AgriDoctor</h1>
          <p>
            Diagnose crop disease, analyze soil, track weather, and receive practical recommendations
            for healthier harvests.
          </p>
          <div className="hero-actions">
            <a href="/login" className="primary-button">Login</a>
            <a href="/register" className="secondary-button">Register</a>
          </div>
        </div>
      </section>

      <section className="grid-3">
        <div className="card feature">
          <h3>Disease detection</h3>
          <p>Upload crop images and use the advisory workflow to assess plant health.</p>
        </div>
        <div className="card feature">
          <h3>Soil analysis</h3>
          <p>Capture soil details and get crop suitability and health recommendations.</p>
        </div>
        <div className="card feature">
          <h3>Smart insights</h3>
          <p>Blend weather, disease, and field context into practical action steps.</p>
        </div>
      </section>
    </div>
  );
}

function LoginPage() {
  const { login } = useAuth();
  const [form, setForm] = useState({ email: '', password: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await api.post('/auth/login', form);
      const { token, user } = response.data;
      login(user, token);
      window.location.href = '/dashboard';
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-shell form-page">
      <form className="card form-card" onSubmit={handleSubmit}>
        <h2>Login</h2>
        {error && <div className="error-box">{error}</div>}
        <label>
          Email
          <input name="email" type="email" value={form.email} onChange={handleChange} required />
        </label>
        <label>
          Password
          <input name="password" type="password" value={form.password} onChange={handleChange} required />
        </label>
        <button className="primary-button" type="submit" disabled={loading}>
          {loading ? 'Signing in...' : 'Login'}
        </button>
      </form>
    </div>
  );
}

function RegisterPage() {
  const { login } = useAuth();
  const [form, setForm] = useState({
    name: '',
    mobile_number: '',
    email: '',
    password: '',
    state: '',
    district: '',
    village: '',
    farm_area: 1,
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await api.post('/auth/register', {
        ...form,
        farm_area: Number(form.farm_area),
      });
      const { token, user } = response.data;
      login(user, token);
      window.location.href = '/';
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-shell form-page">
      <form className="card form-card" onSubmit={handleSubmit}>
        <h2>Register</h2>
        {error && <div className="error-box">{error}</div>}
        <label>
          Full name
          <input name="name" value={form.name} onChange={handleChange} required />
        </label>
        <label>
          Mobile number
          <input name="mobile_number" value={form.mobile_number} onChange={handleChange} required />
        </label>
        <label>
          Email
          <input name="email" type="email" value={form.email} onChange={handleChange} required />
        </label>
        <label>
          Password
          <input name="password" type="password" value={form.password} onChange={handleChange} required />
        </label>
        <div className="two-col">
          <label>
            State
            <input name="state" value={form.state} onChange={handleChange} required />
          </label>
          <label>
            District
            <input name="district" value={form.district} onChange={handleChange} required />
          </label>
        </div>
        <div className="two-col">
          <label>
            Village
            <input name="village" value={form.village} onChange={handleChange} required />
          </label>
          <label>
            Farm area (acres)
            <input name="farm_area" type="number" min="0" step="0.1" value={form.farm_area} onChange={handleChange} required />
          </label>
        </div>
        <button className="primary-button" type="submit" disabled={loading}>
          {loading ? 'Creating account...' : 'Register'}
        </button>
      </form>
    </div>
  );
}

function DashboardPage() {
  const { user, logout } = useAuth();
  const [dashboard, setDashboard] = useState(null);
  const [soilForm, setSoilForm] = useState({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    ph: '',
    moisture: '',
    temperature: '',
    rainfall: '',
  });
  const [cropForm, setCropForm] = useState({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    temperature: '',
    humidity: '',
    ph: '',
    rainfall: '',
  });
  const [soilResult, setSoilResult] = useState(null);
  const [cropResult, setCropResult] = useState(null);
  const [diseaseResult, setDiseaseResult] = useState(null);
  const [diseaseFile, setDiseaseFile] = useState(null);
  const [error, setError] = useState('');
  const [loadingAction, setLoadingAction] = useState('');

  useEffect(() => {
    const loadDashboard = async () => {
      try {
        const response = await api.get('/farmer/dashboard');
        setDashboard(response.data);
      } catch (err) {
        setError('Unable to load dashboard data right now.');
      }
    };

    if (user) {
      loadDashboard();
    }
  }, [user]);

  const handleSoilChange = (event) => {
    const { name, value } = event.target;
    setSoilForm((current) => ({ ...current, [name]: Number(value) }));
  };

  const handleCropChange = (event) => {
    const { name, value } = event.target;
    setCropForm((current) => ({ ...current, [name]: Number(value) }));
  };

  const handleSoilSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoadingAction('soil');

    try {
      const response = await api.post('/soil/analyze', soilForm);
      setSoilResult(response.data.result);
    } catch (err) {
      setError(err.response?.data?.error || 'Soil analysis failed.');
    } finally {
      setLoadingAction('');
    }
  };

  const handleCropSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoadingAction('crop');

    try {
      const response = await api.post('/crop/recommend', cropForm);
      setCropResult(response.data.result);
    } catch (err) {
      setError(err.response?.data?.error || 'Crop recommendation failed.');
    } finally {
      setLoadingAction('');
    }
  };

  const handleDiseaseSubmit = async (event) => {
    event.preventDefault();
    if (!diseaseFile) {
      setError('Please choose an image before scanning.');
      return;
    }

    setError('');
  setLoadingAction('disease');

    try {
      const formData = new FormData();
      formData.append('image', diseaseFile);
      const response = await api.post('/disease/predict', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setDiseaseResult(response.data.result);
    } catch (err) {
      setError(err.response?.data?.error || 'Disease scan failed.');
    } finally {
      setLoadingAction('');
    }
  };

  return (
    <div className="page-shell dashboard-shell">
      <div className="card welcome-card">
        <div>
          <p className="eyebrow">Farmer dashboard</p>
          <h2>Welcome, {user?.name || 'Farmer'}</h2>
          <p>
            {user?.district ? `${user.district}, ${user.state}` : 'Your field dashboard is ready.'}
          </p>
        </div>
        <button className="secondary-button" onClick={logout}>Logout</button>
      </div>

      {error && <div className="error-box">{error}</div>}

      <div className="stats-grid">
        <div className="card stat-card">
          <span>Temperature</span>
          <strong>{dashboard?.weather?.temperature != null ? `${dashboard.weather.temperature}°C` : '—'}</strong>
        </div>
        <div className="card stat-card">
          <span>Humidity</span>
          <strong>{dashboard?.weather?.humidity != null ? `${dashboard.weather.humidity}%` : '—'}</strong>
        </div>
        <div className="card stat-card">
          <span>Disease risk</span>
          <strong>{dashboard?.disease_risk ?? '—'}</strong>
        </div>
        <div className="card stat-card">
          <span>Notifications</span>
          <strong>{dashboard?.notifications ?? '—'}</strong>
        </div>
      </div>

      <div className="dashboard-grid">
        <form className="card form-card" onSubmit={handleSoilSubmit}>
          <h3>Soil analysis</h3>
          <div className="two-col">
            <label>Nitrogen<input name="nitrogen" type="number" value={soilForm.nitrogen} onChange={handleSoilChange} /></label>
            <label>Phosphorus<input name="phosphorus" type="number" value={soilForm.phosphorus} onChange={handleSoilChange} /></label>
          </div>
          <div className="two-col">
            <label>Potassium<input name="potassium" type="number" value={soilForm.potassium} onChange={handleSoilChange} /></label>
            <label>pH<input name="ph" type="number" step="0.1" value={soilForm.ph} onChange={handleSoilChange} /></label>
          </div>
          <div className="two-col">
            <label>Moisture<input name="moisture" type="number" value={soilForm.moisture} onChange={handleSoilChange} /></label>
            <label>Temperature<input name="temperature" type="number" value={soilForm.temperature} onChange={handleSoilChange} /></label>
          </div>
          <label>Rainfall<input name="rainfall" type="number" value={soilForm.rainfall} onChange={handleSoilChange} /></label>
          <button className="primary-button" type="submit" disabled={loadingAction === 'soil'}>{loadingAction === 'soil' ? 'Analyzing...' : 'Analyze soil'}</button>
          {soilResult && (
            <div className="result-box">
              <h4>Result</h4>
              <p><strong>Condition:</strong> {soilResult.soil_condition}</p>
              <p><strong>Status:</strong> {soilResult.nutrient_status}</p>
              <p><strong>Suitable crops:</strong> {Array.isArray(soilResult.suitable_crops) ? soilResult.suitable_crops.join(', ') : soilResult.suitable_crops}</p>
            </div>
          )}
        </form>

        <form className="card form-card" onSubmit={handleCropSubmit}>
          <h3>Crop recommendation</h3>
          <div className="two-col">
            <label>Nitrogen<input name="nitrogen" type="number" value={cropForm.nitrogen} onChange={handleCropChange} /></label>
            <label>Phosphorus<input name="phosphorus" type="number" value={cropForm.phosphorus} onChange={handleCropChange} /></label>
          </div>
          <div className="two-col">
            <label>Potassium<input name="potassium" type="number" value={cropForm.potassium} onChange={handleCropChange} /></label>
            <label>pH<input name="ph" type="number" step="0.1" value={cropForm.ph} onChange={handleCropChange} /></label>
          </div>
          <div className="two-col">
            <label>Temperature<input name="temperature" type="number" value={cropForm.temperature} onChange={handleCropChange} /></label>
            <label>Humidity<input name="humidity" type="number" value={cropForm.humidity} onChange={handleCropChange} /></label>
          </div>
          <label>Rainfall<input name="rainfall" type="number" value={cropForm.rainfall} onChange={handleCropChange} /></label>
          <button className="primary-button" type="submit" disabled={loadingAction === 'crop'}>{loadingAction === 'crop' ? 'Recommending...' : 'Recommend crop'}</button>
          {cropResult && (
            <div className="result-box">
              <h4>Result</h4>
              <p><strong>Top crops:</strong> {cropResult.top_crops?.map((item) => `${item.crop} (${item.score})`).join(', ') || 'Not available'}</p>
              <p><strong>Confidence:</strong> {cropResult.confidence || 'N/A'}</p>
            </div>
          )}
        </form>

        <form className="card form-card" onSubmit={handleDiseaseSubmit}>
          <h3>Disease scanner</h3>
          <CameraScanner
            onCapture={(blob) => setDiseaseFile(new File([blob], 'leaf-capture.jpg', { type: 'image/jpeg' }))}
          />
          <label>
            Capture or upload a crop image
            <input
              type="file"
              accept="image/*"
              capture="environment"
              onChange={(event) => setDiseaseFile(event.target.files?.[0] || null)}
            />
          </label>
          <button className="primary-button" type="submit" disabled={loadingAction === 'disease'}>{loadingAction === 'disease' ? 'Scanning...' : 'Scan disease'}</button>
          {diseaseResult && (
            <div className="result-box">
              <h4>Scan result</h4>
              <p><strong>Crop:</strong> {diseaseResult.crop}</p>
              <p><strong>Disease:</strong> {diseaseResult.disease}</p>
              <p><strong>Confidence:</strong> {diseaseResult.confidence}</p>
              <p><strong>Severity:</strong> {diseaseResult.severity}</p>
            </div>
          )}
        </form>
      </div>
    </div>
  );
}

function AdminPage() {
  const { user, logout } = useAuth();
  const [stats, setStats] = useState(null);
  const [farmers, setFarmers] = useState([]);
  const [diseases, setDiseases] = useState([]);
  const [treatments, setTreatments] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadAdminData = async () => {
      try {
        const [dashboardRes, farmersRes, diseasesRes, treatmentsRes] = await Promise.all([
          api.get('/admin/dashboard'),
          api.get('/admin/farmers'),
          api.get('/admin/diseases'),
          api.get('/admin/treatments'),
        ]);

        setStats(dashboardRes.data.stats);
        setFarmers(farmersRes.data.farmers || []);
        setDiseases(diseasesRes.data.diseases || []);
        setTreatments(treatmentsRes.data.treatments || []);
      } catch (err) {
        setError(err.response?.data?.message || 'Unable to load admin data.');
      }
    };

    if (user) {
      loadAdminData();
    }
  }, [user]);

  return (
    <div className="page-shell admin-shell">
      <div className="card welcome-card">
        <div>
          <p className="eyebrow">Administrator view</p>
          <h2>AgriDoctor Admin</h2>
        </div>
        <button className="secondary-button" onClick={logout}>Logout</button>
      </div>

      {error && <div className="error-box">{error}</div>}

      {stats && (
        <div className="stats-grid">
          <div className="card stat-card">
            <span>Total farmers</span>
            <strong>{stats.total_farmers}</strong>
          </div>
          <div className="card stat-card">
            <span>Total scans</span>
            <strong>{stats.total_scans}</strong>
          </div>
          <div className="card stat-card">
            <span>Total diseases</span>
            <strong>{stats.total_diseases}</strong>
          </div>
          <div className="card stat-card">
            <span>Total treatments</span>
            <strong>{stats.total_treatments}</strong>
          </div>
        </div>
      )}

      <div className="admin-grid">
        <div className="card admin-panel">
          <h3>Registered farmers</h3>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Role</th>
              </tr>
            </thead>
            <tbody>
              {farmers.map((farmer) => (
                <tr key={farmer.id}>
                  <td>{farmer.name}</td>
                  <td>{farmer.email}</td>
                  <td>{farmer.role}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="card admin-panel">
          <h3>Disease catalog</h3>
          <table>
            <thead>
              <tr>
                <th>Crop</th>
                <th>Disease</th>
                <th>Severity</th>
              </tr>
            </thead>
            <tbody>
              {diseases.map((disease) => (
                <tr key={disease.id}>
                  <td>{disease.crop}</td>
                  <td>{disease.disease_name}</td>
                  <td>{disease.severity}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="card admin-panel wide-panel">
          <h3>Treatment catalog</h3>
          <table>
            <thead>
              <tr>
                <th>Crop</th>
                <th>Disease</th>
                <th>Product</th>
              </tr>
            </thead>
            <tbody>
              {treatments.map((treatment) => (
                <tr key={treatment.id}>
                  <td>{treatment.crop}</td>
                  <td>{treatment.disease}</td>
                  <td>{treatment.product_name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

function AppShell() {
  const { user, logout } = useAuth();

  return (
    <BrowserRouter>
      <Navbar user={user} onLogout={logout} />
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={user ? <Navigate to="/dashboard" replace /> : <LoginPage />} />
        <Route path="/register" element={user ? <Navigate to="/dashboard" replace /> : <RegisterPage />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute user={user}>
              <DashboardPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/admin"
          element={
            <ProtectedRoute user={user} role="admin">
              <AdminPage />
            </ProtectedRoute>
          }
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <AppShell />
    </AuthProvider>
  );
}
