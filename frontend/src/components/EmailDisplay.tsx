import React, { useState, useEffect } from 'react';

const EmailDisplay = ({ email }) => {
    const [copied, setCopied] = useState(false);

    useEffect(() => {
        let timer;

        if (copied) {
            timer = setTimeout(() => setCopied(false), 2000); // Revert to original text after 2 seconds
        }

        // Cleanup the timeout when the component unmounts or copied state changes
        return () => {
            if (timer) {
                clearTimeout(timer);
            }
        };
    }, [copied]);

    const formatText = (text) => {
        return text.replace(/\n/g, '<br/>');
    };

    const handleCopy = () => {
        navigator.clipboard.writeText(email)
            .then(() => {
                setCopied(true);
            })
            .catch((error) => alert('Failed to copy email: ' + error));
    };

    const handleRefresh = () => {
        window.location.reload(); // Refreshes the page
    };

    return (
        <div className="email-display">
            <h3 className="email-title">Generated Email:</h3>
            <div className="email-container">
                <pre className="email-content" dangerouslySetInnerHTML={{ __html: formatText(email) }} />
                <div className="copy-container">
                    <button className="copy-btn" onClick={handleCopy} title='Copy the email to the clipboard'>
                        {copied ? '✔ Copied!' : 'Copy Email'}
                    </button>
                    <button className="reresh-btn" onClick={handleRefresh} title="Refresh to Generate New Email">
                        🔄
                    </button>
                </div>
            </div>
        </div>
    );
};

export default EmailDisplay;
