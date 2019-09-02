const http = require('http');
const express = require('express');
const app = express();
app.get("/", (request, response) => {
  console.log(new Date() + " Ping Received");
  response.sendStatus(400);
});
app.listen(3000);
setInterval(() => {
  http.get(`http://discord-js-botz.glitch.me/`);
}, 280000);
 
const setupCMD = "+setreactionrole"
let initialMessage = `**React to the messages below to receive the associated role. If you would like to remove the role, simply remove your reaction!**`;
const roles = ["Javascript", "Python"];
const reactions = ["✅", "✅"];
 
//Load up the bot...
const Discord = require('discord.js');
const bot = new Discord.Client();
 
bot.once('ready', () => {
  bot.user.setGame(`i am a boring bot ever`, 'https://twitch.tv/DarkOufa');
  console.log(`${bot.user.username} is online!`);
});
 
//If there isn't a reaction for every role, scold the user!
if (roles.length !== reactions.length) throw "Roles list and reactions list are not the same length!";
 
//Function to generate the role messages, based on your settings
function generateMessages(){
    var messages = [];
    messages.push(initialMessage);
    for (let role of roles) messages.push(`React below to get the **"${role}"** role!`); //DONT CHANGE THIS
    return messages;
}
 
 
bot.on("message", message => {
    if (message.member.hasPermission("ADMINISTRATOR") && message.content.toLowerCase() == setupCMD){
        var toSend = generateMessages();
        let mappedArray = [[toSend[0], false], ...toSend.slice(1).map( (message, idx) => [message, reactions[idx]])];
        for (let mapObj of mappedArray){
            message.channel.send(mapObj[0]).then( sent => {
                if (mapObj[1]){
                  sent.react(mapObj[1]);  
                }
            });
        }
    }
})
 
 
bot.on('raw', event => {
    if (event.t === 'MESSAGE_REACTION_ADD' || event.t == "MESSAGE_REACTION_REMOVE"){
       
        let channel = bot.channels.get(event.d.channel_id);
        let message = channel.fetchMessage(event.d.message_id).then(msg=> {
        let user = msg.guild.members.get(event.d.user_id);
       
        if (msg.author.id == bot.user.id && msg.content != initialMessage){
       
            var re = `\\*\\*"(.+)?(?="\\*\\*)`;
            var role = msg.content.match(re)[1];
       
            if (user.id != bot.user.id){
                var roleObj = msg.guild.roles.find(r => r.name === role);
                var memberObj = msg.guild.members.get(user.id);
               
                if (event.t === "MESSAGE_REACTION_ADD"){
                    memberObj.addRole(roleObj);
                } else {
                    memberObj.removeRole(roleObj);
                }
            }
        }
        })
 
    }  
});
 
bot.login(process.env.TOKEN);
