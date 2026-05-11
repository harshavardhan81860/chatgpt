const handleSend = async () => {
  if (!input.trim()) return;

  const userMsg = { sender: "user", text: input };
  setMessages((prev) => [...prev, userMsg]);
  
  const messageToSend = input; 
  setInput("");
  setLoading(true);

  try {
    // 1. Axios automatically handles JSON and headers
    const response = await axios.post("http://127.0.0.1:5000/chat", { 
      message: messageToSend 
    });

    // 2. Axios data is found in response.data (not response.json())
    const botMsg = { 
      sender: "bot", 
      text: response.data.response // Matches the 'response' key from Python
    };
    
    setMessages((prev) => [...prev, botMsg]);
  } catch (error) {
    console.error("Error details:", error.response || error.message);
    setMessages((prev) => [
      ...prev, 
      { sender: "bot", text: "Error connecting to AI." }
    ]);
  } finally {
    setLoading(false);
  }
};
