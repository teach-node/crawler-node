
const request = require('request');
const iconv = require('iconv-lite');
const cheerio = require('cheerio');

const FOREIGN_OVERBOUGHT_RANKING_URL = 'https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZG_D.djhtm';

request({url: FOREIGN_OVERBOUGHT_RANKING_URL, encoding: null}, function (error, response, body) {
    if (error)
        console.error('error:', error);

    if (response && response.statusCode !== 200)
        console.log('statusCode:', response && response.statusCode); 
    
    let bodyHtml = iconv.decode(body, 'big5');
    // console.log('body:', bodyHtml);
    const $ = cheerio.load(bodyHtml);

    let dataTable = $('table#oMainTable').html();
    console.log('L20', dataTable)

    let stock = [];

    $('table#oMainTable td.t3t1').each(function(index, element){
        stock[index] = {};
        stock[index].name = $(this).text();
    })

    $('table#oMainTable td.t3t1+td.t3n1').each(function(index, element){
        stock[index] = stock[index] || {} ;
        stock[index].endprice = $(this).text();
    })

    $('table#oMainTable td.t3t1+td.t3n1+td').each(function(index, element){
        stock[index] = stock[index] || {} ;
        // console.log('L36', index, $(this).text())
        stock[index].upAndDown = $(this).text();
    })

    $('table#oMainTable td.t3t1+td.t3n1+td+td').each(function(index, element){
        stock[index] = stock[index] || {} ;
        stock[index].upAndDownRate = $(this).text();
    })

    $('table#oMainTable td.t3t1+td.t3n1+td+td+td').each(function(index, element){
        stock[index] = stock[index] || {} ;
        stock[index].count = $(this).text();
    })


    console.log('L30',  stock)

});