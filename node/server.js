const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {

var seconds = os.uptime();
var minutes = seconds/60;
var hours = minutes/60;
var days = hours/24;

seconds = Math.floor(seconds);
minutes = Math.floor(minutes);
hours = Math.floor(hours);
days = Math.floor(days);

seconds = seconds%60;
minutes = minutes%60;
hours = hours%24;

var totalbytes = os.totalmem();
var totalmega = totalbytes/1000000;
var freebytes = os.freemem();
var freemega = freebytes/1000000;

  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${days}, Hours: ${hours}, Minutes: ${minutes}, Seconds: ${seconds}</p>
        <p>Total Memory: ${totalmega} MB</p>
        <p>Free Memory: ${freemega} MB</p>
        <p>Number of CPUs: ${os.cpus().length}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");