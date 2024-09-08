// src/components/EmailForm.jsx

import React, { useState } from 'react';

const EmailForm = ({ onGenerateEmail, username, setUsername, loading, email }) => {
    const [error, setError] = useState('');
    // Define a regex pattern for valid names (e.g., only letters and spaces, no special characters, 2-50 characters long)
    const nameRegex = /^[A-Za-z\s]{2,50}$/;

    // Validation function
    const validateName = (name) => {
        // Check if the name matches the regex pattern
        return nameRegex.test(name);
    };

       // Handle form submission
       const handleSubmit = async (e) => {
        e.preventDefault();

        // Validate the username
        if (validateName(username)) {
            setError('');
            onGenerateEmail(username);
        } else {
            setError('Please enter a valid name (letters and spaces only, 2-50 characters).');
        }
    }

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
                    disabled={loading || email}
                    required
                />
            </div>
            {error && <p className="error-message">{error}</p>}
            <button type="submit" className="btn" disabled={loading || email}>
                Generate Email
            </button>
        </form>
    );
};

export default EmailForm;
