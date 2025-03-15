const params = new URLSearchParams(window.location.search);
const productId = params.get('id');

const product = products.find(p => p.id == productId);

if (product) {
    document.getElementById('product-accord').src = product.accord;
    document.getElementById('product-name').textContent = product.name;
    document.getElementById('product-page').textContent = product.name;
    document.getElementById('product-image').src = product.image;
    document.getElementById('product-image').alt = product.name;
    document.getElementById('product-folder').textContent = product.name;
    document.getElementById('product-fedezd_fel').textContent = product.fedezd_fel;
    document.getElementById('product-leiras').textContent = product.leiras;
    document.getElementById('product-szoveg').textContent = product.szoveg;
    document.getElementById('product-velemeny').textContent = product.velemeny;
    document.getElementById('product-price').textContent = product.price;
} else {
    document.body.innerHTML = '<h1>Error 404!</h1>';
}
