// src/components/EmailForm.jsx



const EmailForm = ({ onGenerateEmail, username, setUsername, loading }) => {
    

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
                    disabled={loading}
                    required
                />
            </div>
            <button type="submit" className="btn" disabled={loading}>
                Generate Email
            </button>
        </form>
    );
};

export default EmailForm;
