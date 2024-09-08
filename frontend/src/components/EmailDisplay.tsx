// src/components/EmailDisplay.jsx


const EmailDisplay = ({ email }) => {
    const formatText = (text) => {
        return text.replace(/\n/g, '<br/>');
    };

    const handleCopy = () => {
        navigator.clipboard.writeText(email)
            .then(() => alert('Email copied to clipboard!'))
            .catch((error) => alert('Failed to copy email: ' + error));
    };

    return (
        <div className="email-display">
            <h3 className="email-title">Generated Email:</h3>
            <div className="email-container">
                <pre className="email-content" dangerouslySetInnerHTML={{ __html: formatText(email) }} />
                <button className="copy-btn" onClick={handleCopy}>Copy Email</button>
            </div>
        </div>
    );
};

export default EmailDisplay;
