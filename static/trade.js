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




  $("#bsbutton").click(function()
  {
    if ($( "#bsamount" ).val().length!=0)
  {
    
      let cur = $("#currency option:selected").val()
      if (cur==1)
      {console.log($('#usd').text()*$( "#bsamount" ).val())}
      if (cur==2)
      {console.log($('#eur').text()*$( "#bsamount" ).val())}
      if (cur==3)
      {console.log($('#gbp').text()*$( "#bsamount" ).val())}

      

  }
  }
  );
