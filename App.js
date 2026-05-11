const handleSend = async () => {
    if (!input) return;

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
        // DO NOT RENDER THE ROOT HERE
    }
};

// ... Rest of your component (return JSX) ...

// THIS GOES AT THE VERY END OF THE FILE, OUTSIDE THE APP COMPONENT
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
