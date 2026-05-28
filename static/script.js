async function sendMessage() {

    const input = document.getElementById("user-input");

    const chatBox = document.getElementById("chat-box");

    const query = input.value.trim();

    if (!query) return;

    // User message
    const userMessage = document.createElement("div");

    userMessage.className = "message user";

    userMessage.innerText = query;

    chatBox.appendChild(userMessage);

    input.value = "";

    // Bot typing
    const botMessage = document.createElement("div");

    botMessage.className = "message bot";

    botMessage.innerText = "Thinking...";

    chatBox.appendChild(botMessage);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: query
            })
        });

        const data = await response.json();

        botMessage.innerHTML = marked.parse(data.answer);

    } catch (error) {

        botMessage.innerText =
            "Error connecting to server.";
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}