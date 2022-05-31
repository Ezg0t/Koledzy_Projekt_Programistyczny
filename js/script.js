function searchWatches() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    ul = document.getElementById("list-group");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("h4")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function checkPrices() {
    var price1, price2, ul, li, a, i, small, value;
    price1 = parseFloat(document.getElementById("price_1").value);
    price2 = parseFloat(document.getElementById("price_2").value);
    ul = document.getElementById("list-group");
    li = ul.getElementsByTagName("li");
    small = ul.getElementsByTagName("small");

    for (i = 0; i < li.length; i++) {
        value = parseFloat(small[i].textContent.slice(0, -4));
        if (price1 > value || price2 < value) {
            li[i].style.display = "none";
        } else if (price2 < value && price2 < value) {
            li[i].style.display = "none";
        } else {
            li[i].style.display = "";
        }
    }
}

function sortList() {
    var list, i, switching, b, shouldSwitch, small, n, select;
    list = document.getElementById("list-group");
    small = list.getElementsByTagName("small");
    switching = true;
    select = document.getElementById('sort');
    n = select.options[select.selectedIndex].value;
    if (n == '1') {
        while (switching) {
            switching = false;
            b = list.getElementsByTagName("li");
            for (i = 0; i < (b.length - 1); i++) {
                parseFloat(small[i].textContent.slice(0, -4));
                shouldSwitch = false;
                if (parseFloat(small[i].textContent.slice(0, -4)) > parseFloat(small[i + 1].textContent.slice(0, -4))) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                b[i].parentNode.insertBefore(b[i + 1], b[i]);
                switching = true;
            }
        }
    } else if (n == '2') {
        while (switching) {
            switching = false;
            b = list.getElementsByTagName("li");
            for (i = 0; i < (b.length - 1); i++) {
                parseFloat(small[i].textContent.slice(0, -4));
                shouldSwitch = false;
                if (parseFloat(small[i].textContent.slice(0, -4)) < parseFloat(small[i + 1].textContent.slice(0, -4))) {
                    shouldSwitch = true;
                    break;
                }
            }
            if (shouldSwitch) {
                b[i].parentNode.insertBefore(b[i + 1], b[i]);
                switching = true;
            }
        }
    }

}