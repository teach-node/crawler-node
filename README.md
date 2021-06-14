# crawler-node
練習 node 爬蟲
安安

## TERMINAL語法:
- git status: 看檔案更改狀況
- git add ${file name}: 把要更改的檔案加上去
- npm init: 建立專案初始化
- Node -v: 看node版本
- node ${file name}: 執行該檔案程式
- git pull: 把現在git上最新的程式抓下來

## NODE語法：
console.log(“”) : 印log
const : 引用套件
> const cheerio = require('cheerio');
let : 宣告變數






## 安裝套件資源

> npm i cheerio request -save

 - cheerio 可以抓取網頁裡面的資料
 - request 抓取網頁的原始碼
 - iconv-lite 解析字元

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
