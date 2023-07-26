const express = require('express');
const bodyParser = require('body-parser');
const xmlJs = require('xml-js');

const app = express();

app.use(bodyParser.json());

app.post('/convert', (req, res) => {
  try {
    const jsonData = req.body;
    const xmlData = xmlJs.js2xml(jsonData, { compact: true, spaces: 4 });
    res.header('Content-Type', 'application/xml');
    res.send(xmlData);
  } catch (error) {
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});