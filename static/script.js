$(document).ready(function(){
    var serverIp = "http://127.0.0.1:5000/"
    var data = $.get(serverIp);
    alert(data);
});