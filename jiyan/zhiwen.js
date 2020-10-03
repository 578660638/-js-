
location = {
    "href": "https://www.w3school.com.cn/jsref/prop_anchor_href.asp",
    "origin": "https://www.w3school.com.cn",
    "protocol": "https:",
}
document = {
    createElement: function () {
        var loc = {
            href: ""
        };
        var temp_href = loc.href;
        Object.defineProperty(loc, 'href', {
            // Hook loc.href，当为其赋值时，按下面的规则强制改变
            get: function () {
                return temp_href
            },
            set: function (val) {
                if (val.indexOf('http://') === 0 || val.indexOf('https://') === 0) {
                    // 1.当值为http://或https://开头时，即为该值
                    temp_href = val;
                } else if (val.indexOf('//') === 0) {
                    // 2.当值为//开头时，即为location.protocol加上该值
                    temp_href = location.protocol + val;
                } else if (val.indexOf('/') === 0) {
                    // 3.当值为/开头时，即为location.origin加上该值
                    temp_href = location.origin + val;
                } else {
                    // 4.除以上3种情况，即为location.href中最后一个/之前的值加上该值
                    var s = location.href
                    temp_href = s.substring(0, s.lastIndexOf("/")+1) + val
                }
                return temp_href
            }
        });
        return loc;
    }
}