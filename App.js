const { useState } = React;

const App = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMsg = { sender: "user", text: input };
        setMessages((prev) => [...prev, userMsg]);

        const messageToSend = input;
        setInput("");
        setLoading(true);

        try {
            const response = await axios.post("http://127.0.0.1:5000/chat", {
                message: messageToSend,
            });

            const botMsg = { sender: "bot", text: response.data.response };
            setMessages((prev) => [...prev, botMsg]);

        } catch (error) {
            console.error("Error details:", error);
            setMessages((prev) => [
                ...prev,
                { sender: "bot", text: "Error connecting to AI server." },
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="chat-container">
            <div className="header">HARSHA AI</div>
            <div className="chat-window">
                {messages.map((msg, index) => (
                    <div key={index} className={`message-wrapper ${msg.sender}`}>
                        <div className="message-bubble">{msg.text}</div>
                    </div>
                ))}
                {loading && <div className="loading">Assistant is typing...</div>}
            </div>
            <div className="input-area">
                <input 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                    placeholder="Type a message..."
                />
                <button onClick={handleSend}>Send</button>
            </div>
        </div>
    );
};

// Mount the app
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
