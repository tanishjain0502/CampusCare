import { createContext, useContext, useEffect, useState } from 'react';
import { loginUser, registerUser, getProfile } from '../services/authService';

/**
 * AuthContext
 * -----------
 * Provides authentication state and actions to the entire component tree.
 *
 * What it stores:
 *   - user    : the authenticated user object (id, name, email, role) or null
 *   - loading : true while the initial session check is in progress
 *
 * Token storage note:
 *   The JWT is kept in localStorage under the key "campuscare_token".
 *   This is a simple approach suitable for a learning project, but localStorage
 *   is accessible to all JavaScript on the page and is therefore vulnerable to
 *   XSS. A more secure production approach is to use HttpOnly cookies, which
 *   are not readable by JavaScript.
 */
const AuthContext = createContext(null);

const TOKEN_KEY = 'campuscare_token';
const USER_KEY = 'campuscare_user';

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // On mount, check if there is an existing session
  useEffect(() => {
    const initAuth = async () => {
      const token = localStorage.getItem(TOKEN_KEY);
      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const res = await getProfile();
        setUser(res.data.user);
      } catch {
        // Token is invalid or expired — clear storage
        localStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(USER_KEY);
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    initAuth();
  }, []);

  const login = async (email, password) => {
    const res = await loginUser({ email, password });
    const { token, user: userData } = res.data;
    localStorage.setItem(TOKEN_KEY, token);
    localStorage.setItem(USER_KEY, JSON.stringify(userData));
    setUser(userData);
    return userData;
  };

  const register = async (name, email, password) => {
    const res = await registerUser({ name, email, password });
    const { token, user: userData } = res.data;
    localStorage.setItem(TOKEN_KEY, token);
    localStorage.setItem(USER_KEY, JSON.stringify(userData));
    setUser(userData);
    return userData;
  };

  const logout = () => {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

/**
 * useAuth — convenience hook.
 * Throws if used outside an <AuthProvider> so misuse is caught early.
 */
export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error('useAuth must be used inside an <AuthProvider>');
  }
  return ctx;
};
