import { useState, useEffect } from 'react';
import EmailForm from './components/EmailForm';
import EmailDisplay from './components/EmailDisplay';
import { generateEmail } from './api/emailApi';
import './App.css';

const App = () => {
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(false);
    const [username, setUsername] = useState('');
    const [delayMessage, setDelayMessage] = useState(false);

    const handleGenerateEmail = async (username) => {
        setLoading(true);
        setDelayMessage(false);

        // Show the delay message after 15 seconds
        const timer = setTimeout(() => {
            setDelayMessage(true);
        }, 15000);

        try {
            const generatedEmail = await generateEmail(username);
            setEmail(generatedEmail);
            setUsername('');
        } catch (error) {
            alert('An error occurred while generating the email.');
        } finally {
            clearTimeout(timer);
            setLoading(false);
        }
    };

    return (
        <div className="app">
            <div className="container">
                <EmailForm onGenerateEmail={handleGenerateEmail} username={username} setUsername={setUsername} loading={loading} />
                {loading && (
                    <div className="loader-container">
                        <div className="spinner"></div>
                        {!delayMessage && <p>Generating email...</p>}
                        {delayMessage && <p className="delay-message">Looks like it is taking a while, wait on please!</p>}
                    </div>
                )}
                {email && <EmailDisplay email={email} />}
            </div>
        </div>
    );
};

export default App;
