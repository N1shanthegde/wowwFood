var mcart = document.querySelector('#mcart');
var mtotal = document.querySelector('#mtotal');

//add sandwich

function addMoms(mid){
    //get sandwich name
    sandwichId = '#mom' + mid;
    var name = document.querySelector(sandwichId).innerHTML;
    //get sandwich price
    var radio = 'moms' + mid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if(pri[0].checked){
        price = pri[0].value;
        size = ' ';
    }
    // else{
    //     price = pri[1].value;
    //     size = ' ';
    // }

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    //saving item & total in storage
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));
    
    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    //updating no. of items in shopping cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    butto = '<button class="del" onclick="removeMoms(' + cartSize + ')">x</button>';      //'<div class="delete" onclick="removeMoms('+ cartSize +')">x</div>';
    mtotal.innerHTML = 'Total: '+ total + '₹';
    mcart.innerHTML += '<li>' + name + ' ' + ': ' + price + '₹ ' + butto + '</li>';
}


function mshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    mcart.innerHTML = '';
    for (let i=0; i < cartSize; i++){
        butto = '<button class="del" onclick="removeMoms(' + i + ')">x</button>';         //'<div class="delete" onclick="removeMoms('+ i +')">x</div>';
        mcart.innerHTML += '<li>' + orders[i][0] + ' ' + ': ' + orders[i][2] + '₹ ' + butto + '</li>';
    }
    mtotal.innerHTML = 'Total: '+ total +'₹';
}

mshoppingCart();

function removeMoms(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    //updating no. of items in shopping cart
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    mshoppingCart();
}