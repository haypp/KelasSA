const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const axios = require('axios');
const cheerio = require("cheerio");

function scrapeTitleContent(url) {
  axios.get(url)
    .then(urlResponse => {
      const $ = cheerio.load(urlResponse.data);
      const titleElement = $('h1.jeg_post_title');
      const title = titleElement.text().trim();

      const contentContainer = $('.content-inner');
      const content = contentContainer.text().trim()
        .replace(/\s+/g, ' ') 
        .replace(/^\s*|\s*$/g, ''); 

      console.log(`Title: ${title}`);
      console.log(`Content: \n${content}`);
    })
    .catch(error => console.error(error));
}

readline.question('Enter the URL of the article: ', (url) => {
  scrapeTitleContent(url.trim());
  readline.close();
});
