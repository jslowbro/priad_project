function initMap() {
 ILITEAPI.init({
"divId" : "iapi",
"width" : 1000,
"height" : 1000,
"activeGpMapId" : "gp0",
"activeGpMaps" : ["gp0","gp1"],
"activeGpActions" : ["pan","fullExtent"],
"scale" : 2000,
"marker" : [{
"x" : 362269,
"y" : 362264,
"scale":2000,
"opts" : {
"title" : "dymek nr 1",
"content" : "dymek"
}
},{
"x" : 361968,
"y" : 362234,
"scale":2000,
"opts" : {
"title" : "dymek nr 2",
"content" : "dymek"
}
}]
});
}