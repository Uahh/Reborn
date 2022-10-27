var dataURL = ROOT_PATH + '/data/asset/data/gps/gps_' + idx + '.bin';
console.log(dataURL)
var xhr = new XMLHttpRequest();
xhr.open('GET', dataURL, true);
xhr.responseType = 'arraybuffer';
xhr.onload = function (e) {
    var rawData = new Int32Array(this.response);
    var data = new Float32Array(rawData.length);
    for (var i = 0; i < rawData.length; i += 2) {
        data[i] = rawData[i + 1] / 1e7;
        data[i + 1] = rawData[i] / 1e7;
    }
    myChart.appendData({
        seriesIndex: 0,
        data: data
    });
    fetchData(idx + 1);
};