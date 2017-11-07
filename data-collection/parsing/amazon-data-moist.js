const util = require('util')
var amazon = require('amazon-product-api');
var fs = require('fs');

var client = amazon.createClient({
  awsId: "AKIAJYQEGPADE3EZJX2A",
  awsSecret: "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",
  awsTag: "alexisherrera-20"
});

var data = [];

//moisterizers: 50
for (var i = 1; i <= 5; i++) {
  client.itemSearch({
    keywords: 'moisturizer',
    searchIndex: 'Beauty',
    responseGroup: 'ItemAttributes,Images',
    itemPage: "" + i + ""
  }, function(err, results, response) {
    if (err) {
      console.log(util.inspect(err, false, null));
    } else {
      console.log(results.length)
      //iterate through each result
      for (var j = 0; j < results.length; j++) {
        var item = {};
        item.url = results[j].DetailPageURL
        item.brand = results[j].ItemAttributes[0].Brand
        item.manufacturer = results[j].ItemAttributes[0].Manufacturer
        item.model = results[j].ItemAttributes[0].Model
        item.title = results[j].ItemAttributes[0].Title
        item.features = results[j].ItemAttributes[0].Feature
        item.imageLink = results[j].MediumImage[0].URL
        data.push(item)
      }

    }
  });
}

//write to JSON file
setTimeout(function() {
  fs.writeFile("moisturizer-data.json",  JSON.stringify(data) , function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
  });
}, 8000)
