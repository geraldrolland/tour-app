uri = "ws://" + window.location.host + "/ws/chatapp/"

var chatSocket = new WebSocket(uri)

    chatSocket.onmessage = (e) => {
        const message = JSON.parse(e.data)
        const ul = document.getElementById("text-box")
        const li = document.createElement("li")
        li.innerHTML = message["text"]
        ul.appendChild(li)
    }

    chatSocket.onclose = (e) => {
        console.log("disconnected")
    }

    chatSocket.onopen = (e) => {
        console.log("connected")
    }

    function sendMessage() {
        if (document.getElementById("input-text").value !== "") {
            const input_text = document.getElementById("input-text").value
            const text_json = JSON.stringify({text: input_text})
            chatSocket.send(text_json)
            document.getElementById("input-text").value=""
        }
    }