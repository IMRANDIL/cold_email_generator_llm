// src/api/emailApi.js
export const generateEmail = async (username) => {
    try {
        const response = await fetch('http://localhost:5000/generate-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username }),
        });
        
        if (!response.ok) {
            throw new Error('Failed to generate email');
        }
        
        const data = await response.json();
        console.log(data)
        return data.emails[0];
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
};
