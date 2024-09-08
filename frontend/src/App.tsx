// src/App.jsx
import { useState } from 'react';
import EmailForm from './components/EmailForm';
import EmailDisplay from './components/EmailDisplay';
import { generateEmail } from './api/emailApi';
import './App.css';

const App = () => {
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(false);
    const [username, setUsername] = useState('');

    const handleGenerateEmail = async (username) => {
        setLoading(true);
        try {
            const generatedEmail = await generateEmail(username);
            setEmail(generatedEmail);
            setUsername('')
        } catch (error) {
            alert('An error occurred while generating the email.');
            setLoading(false);
            setUsername('')
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="app">
            <div className="container">
                <EmailForm onGenerateEmail={handleGenerateEmail} username={username} setUsername={setUsername} loading={loading} />
                {loading && <p className="loading">Generating email...</p>}
                {email && <EmailDisplay email={email} />}
            </div>
        </div>
    );
};

export default App;
