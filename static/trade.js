console.log("uploaded js")

// function update_values() {
//     $.getJSON("http://127.0.0.1:5000" + '/rates',
            
//     function(data) {
//     $('#usd').text(data.rate[0]);
//     $('#gbp').text(data.rate[1]);
//     $('#eur').text(data.rate[2]);
//     });
    
// };

// $(document).ready(update_values())

// $(function() {
//   $('#flash').delay(5000).fadeOut();
// });


let cbsell = document.getElementById('cbsell');
let cbbuy = document.getElementById('cbbuy');
let bsbutton = document.getElementById('bsbutton');
let amount = document.getElementById('bsamount');
let currency = document.getElementById('currency');
let sell_cat = document.getElementById('sell_cat');
let buy_cat = document.getElementById('buy_cat');
let r_buysell = document.getElementById('r_buysell');
let bs_option = document.getElementById('bs-option');


cbsell.addEventListener('change', uncheck_cbbuy)
cbbuy.addEventListener('change', uncheck_cbsell)

function uncheck_cbbuy() 
{
    cbbuy.checked = false;
    console.log(cbbuy.checked,cbsell.checked)
    if (cbbuy.checked == false && cbsell.checked == false)
    {console.log("both off")
      r_buysell.style.display = "none";
      bs_option.style.top = "20%";
    }
    if (cbbuy.checked == true || cbsell.checked == true)
    {console.log("either on")
    r_buysell.style.display = "grid";
    bs_option.style.top = "15%";
    }
    bsbutton.innerHTML = '<i class="icon-collapse"></i>SELL';
    bsbutton.style.backgroundImage = "linear-gradient(to right, lightsalmon, white)";
    currency.style.backgroundImage = "linear-gradient(to right, lightsalmon, white)";
    amount.style.backgroundImage = "linear-gradient(to right, lightsalmon, white)";
    amount.value = ""
}

function uncheck_cbsell() 
{
    cbsell.checked = false;
    console.log(cbbuy.checked, cbsell.checked)
    if (cbbuy.checked == false && cbsell.checked == false)
    {console.log("both off")
    r_buysell.style.display = "none";
    bs_option.style.top = "20%";
    }
    if (cbbuy.checked == true || cbsell.checked == true)
    {console.log("either on")
    r_buysell.style.display = "grid";
    bs_option.style.top = "15%";
    }
    bsbutton.innerHTML = '<i class="icon-collapse-top"></i> BUY';
    bsbutton.style.backgroundImage = "linear-gradient(to right,#90EE90, white)";
    currency.style.backgroundImage = "linear-gradient(to right,#90EE90, white)";
    amount.style.backgroundImage = "linear-gradient(to right,#90EE90, white)";
    amount.value = ""
}
