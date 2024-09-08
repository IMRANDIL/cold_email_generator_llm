// src/components/EmailDisplay.jsx


const EmailDisplay = ({ email }) => {
    const formatText = (text) => {
        return text.replace(/\n/g, '<br/>');
    };

    return (
        <div className="email-display">
            <h3 className="email-title">Generated Email:</h3>
            <p className="email-content" dangerouslySetInnerHTML={{ __html: formatText(email) }} />
        </div>
    );
};

export default EmailDisplay;
