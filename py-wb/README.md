# crawler-python
股票用 python 

## 安裝套件資源

> https://github.com/mlouielu/twstock

twstock 台灣股市股票價格擷取

```
四大買賣點判斷 Best Four Point

```

### cheerio
> https://www.npmjs.com/package/cheerio

```
const cheerio = require('cheerio');
const $ = cheerio.load('<h2 class="title">Hello world</h2>');

$('h2.title').text('Hello there!');
$('h2').addClass('welcome');

$.html();
```

### request
> https://www.npmjs.com/package/request

```
const request = require('request');
request('http://www.google.com', function (error, response, body) {
  console.error('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the HTML for the Google homepage.
});
```

### iconv-lite
> https://www.npmjs.com/package/iconv-lite

```
var iconv = require('iconv-lite');

// Convert from an encoded buffer to a js string.
str = iconv.decode(Buffer.from([0x68, 0x65, 0x6c, 0x6c, 0x6f]), 'win1251');

// Convert from a js string to an encoded buffer.
buf = iconv.encode("Sample input string", 'win1251');

// Check if encoding is supported
iconv.encodingExists("us-ascii")
```
