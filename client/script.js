var name = prompt("Enter your name:")
var sock = new WebSocket("ws://localhost:4000", ["protocolOne", "protocolTwo"])
var log = document.getElementById('log')

sock.onopen = function() {  

    sock.send(JSON.stringify({
        type: "name",
        data: name
    }))
    
}
sock.onmessage = function(event){
    console.log(event);
    var json = JSON.parse(event.data)
    log.innerHTML += "[" + json.idd + "]" + " " + json.name + " : " + json.data + "<br>"
}
document.querySelector('button').onclick = function() {
    var text = document.getElementById('text').value;
 
    sock.send(JSON.stringify({

        type: "message",
        data: text
    }));
    
    log.innerHTML += "You: " + text +"<br>"
}

sock.onclose = function(){ 
    alert("Socket closed");
}
















































