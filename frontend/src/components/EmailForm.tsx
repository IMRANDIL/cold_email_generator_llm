// src/components/EmailForm.jsx
import { useState } from 'react';


const EmailForm = ({ onGenerateEmail }) => {
    const [username, setUsername] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (username) {
            onGenerateEmail(username);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="email-form">
            <h2 className="title">Generate Your Cold Email</h2>
            <div className="input-group">
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Enter your name"
                    className="input"
                    required
                />
            </div>
            <button type="submit" className="btn">
                Generate Email
            </button>
        </form>
    );
};

export default EmailForm;
