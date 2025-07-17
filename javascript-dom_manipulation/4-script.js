document.querySelector("#add_item").addEventListener('click', function () {
    const new_item = document.createElement("li");
    new_item.innerText = "Item";

const my_list = document.querySelector('.my_list');
my_list.appendChild(new_item);
})
