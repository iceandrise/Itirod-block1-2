var server = require('ws').Server;
var s = new server({port: 4000});
const express = require('express')
const cors = require('cors')

const app = express()
app.use(cors())
app.use(express.json())
app.use(express.static('../client'))
// app.get('*', (req, res) => {
//     res.redirect('/')
// })

let idd = 0;
let count = 0;

s.on('connection', function(ws){
    count++

    if(count > 2){
        ws.send(JSON.stringify({
            name: "Warning: ",
            data: "allowed only one connection"
        }))
        ws.close()
        
    }else{
       
    }
    
  ws.on('message', function(message){
        message = JSON.parse(message)
        if(message.type == "name"){
            
            ws.personName = message.data;
            return;
        }

        console.log("Received: " + message);

        s.clients.forEach(function e(client){
            if(client != ws)
                client.send(JSON.stringify({
                    idd: idd++,
                    name: ws.personName,
                    data: message.data
                }))
        })
    })

    ws.on('close', function(){
        count--
        console.log("Lost client");
    })

})

app.listen(3000, () => {
    console.log(`Server started`)
})
