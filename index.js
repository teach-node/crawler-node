
const request = require('request');
const iconv = require('iconv-lite');

const FOREIGN_OVERBOUGHT_RANKING_URL = 'https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZG_D.djhtm';

request({url: FOREIGN_OVERBOUGHT_RANKING_URL, encoding: null}, function (error, response, body) {
  console.error('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', iconv.decode(body, 'big5')); // Print the HTML for the Google homepage.
});