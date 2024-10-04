var scart = document.querySelector('#scart');
var stotal = document.querySelector('#stotal');

//add sandwich

function addSandwich(sid){
    //get sandwich name
    sandwichId = '#sand' + sid;
    var name = document.querySelector(sandwichId).innerHTML;
    //get sandwich price
    var radio = 'sandwich' + sid;
    var pri = document.getElementsByName(radio);
    var size, price;
    if(pri[0].checked){
        price = pri[0].value;
        size = ' ';
    }

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

    butto = '<button class="del" onclick="removeSandwich(' + cartSize + ')">x</button>';      //'<div class="delete" onclick="removeSandwich('+ cartSize +')">x</div>';
    stotal.innerHTML = 'Total: '+ total + '₹';
    scart.innerHTML += '<li>' + name + ' ' + size + ': ' + price + '₹ ' + butto + '</li>';
}


function sshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    scart.innerHTML = '';
    for (let i=0; i< cartSize; i++){
        butto = '<button class="del" onclick="removeSandwich(' + i + ')">x</button>';         //'<div class="delete" onclick="removeSandwich('+ i +')">x</div>';
        scart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ': ' + orders[i][2] + '₹ ' + butto + '</li>';
    }
    stotal.innerHTML = 'Total: '+ total +'₹';
}

sshoppingCart();

function removeSandwich(n){
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