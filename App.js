const { useState } = React;

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:5000/chat", { message: input });
      const botMsg = { sender: "bot", text: response.data.reply };
      setMessages((prev) => [...prev, botMsg]);
    } catch (error) {
      setMessages((prev) => [...prev, { sender: "bot", text: "Error connecting to AI." }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="header">HARSHA AI</div>
      <div className="chat-window">
        {messages.map((msg, i) => (
          <div key={i} className={`message-wrapper ${msg.sender}`}>
            <div className="message-bubble">{msg.text}</div>
          </div>
        ))}
        {loading && <div className="loading">Assistant is typing...</div>}
      </div>
      <div className="input-area">
        <input 
          value={input} 
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          onChange={(e) => setInput(e.target.value)} 
          placeholder="Type a message..." 
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
