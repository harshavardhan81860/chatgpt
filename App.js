const handleSend = async () => {
    if (!input) return;

    const userMsg = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    
    // Save input to a constant because setInput("") happens immediately
    const messageToSend = input; 
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post("/chat", { message: input });
        body: JSON.stringify({ message: messageToSend }),
      });

      if (!response.ok) throw new Error("Server error");

      const data = await response.json();
      const botMsg = { sender: "bot", text: data.reply };
      setMessages((prev) => [...prev, botMsg]);
    } catch (error) {
      console.error("Error details:", error); // Check your browser console!
      setMessages((prev) => [...prev, { sender: "bot", text: "Error connecting to AI." }]);
    } finally {
      setLoading(false);
    }
  };
