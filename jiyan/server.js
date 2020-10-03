var express = require("express")
var bodyParser=require('body-parser')
var sdk1 = require('./jiyanparo')
var api =express();
api.use(bodyParser.urlencoded({
    parameterLimit:50000,
        limit:'50mb',
        extended:false
}));

api.get('/get_token',function (req,res) {
    var token=sdk1.jKCV()
    res.send(token)
});

var server =api.listen('8090',function () {

})


