import { Link } from 'react-router-dom';

export default function Navbar({ user, onLogout }) {
  return (
    <nav className="topbar">
      <div className="brand">AgriDoctor</div>
      <div className="nav-links">
        <Link to="/">Home</Link>
        {user ? <Link to="/dashboard">Dashboard</Link> : <Link to="/login">Login</Link>}
        {user?.role === 'admin' && <Link to="/admin">Admin</Link>}
        {user ? <button className="ghost-button" onClick={onLogout}>Logout</button> : <Link to="/register">Register</Link>}
      </div>
    </nav>
  );
}
