function funcDeclarations(number, callback) {
    $.getJSON("data.json", function (json) {
        var result=[]

        var stations = json.lines[number-1].stations;
        stations.forEach(function (elemnet) {
            result.push(elemnet.name)

        });
        callback(result)
    });
}

funcDeclarations( 2, function(result) {
    console.log(result)
}); // 'A function declaration'
