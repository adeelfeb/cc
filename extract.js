
const Unrar = require('unrar');
const fs = require('fs');
const path = require('hometask/c.ra');

// Define paths
const rarFilePath = path.join(__dirname, 'c.rar'); // Replace with your actual .rar file name
const extractDir = path.join(__dirname, 'extracted-files');

// Ensure extraction directory exists
if (!fs.existsSync(extractDir)) {
  fs.mkdirSync(extractDir);
}

// Initialize unrar and extract the files
const rar = new Unrar(rarFilePath);

rar.extract(extractDir, null, (err) => {
  if (err) {
    console.error('Extraction failed:', err);
  } else {
    console.log('Extraction successful!');
  }
});
