console.log("uploaded js")

function update_values() {
    $.getJSON("http://127.0.0.1:5000" + '/rates',
            
    function(data) {
    $('#usd').text(data.rate[0]);
    $('#gbp').text(data.rate[1]);
    $('#eur').text(data.rate[2]);
    });
    
};
$(document).ready(update_values())


