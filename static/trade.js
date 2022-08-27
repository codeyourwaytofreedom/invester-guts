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
    let current_budget = parseFloat($(".budget").text());
    let usd_bal = parseFloat($("#usd_bal").text());
    let eur_bal = parseFloat($("#eur_bal").text());
    if ($( "#bsamount" ).val().length!=0)
  {
    
      let cur = $("#currency option:selected").val()
      if (cur==1)
      {console.log($('#usd').text()*$( "#bsamount" ).val())
        console.log(current_budget-$('#usd').text()*$( "#bsamount" ).val())
        $("#bud").html(current_budget-$('#usd').text()*$( "#bsamount" ).val())
        console.log(usd_bal+$( "#bsamount" ).val())
        $("#usd_bal").html(usd_bal+parseFloat($( "#bsamount" ).val()))
      }
      if (cur==2)
      {console.log($('#eur').text()*$( "#bsamount" ).val())
      $("#bud").html(current_budget-$('#eur').text()*$( "#bsamount" ).val())
      console.log(eur_bal+$( "#bsamount" ).val())
      $("#eur_bal").html(eur_bal+parseFloat($( "#bsamount" ).val()))
      }
      if (cur==3)
      {console.log($('#gbp').text()*$( "#bsamount" ).val())}

      

  }
  }
  );

  console.log(parseFloat($(".budget").text()));
  