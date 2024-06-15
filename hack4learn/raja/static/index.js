document.addEventListener('DOMContentLoaded', function() {
  console.log('Document is loaded');
  var p = document.querySelector("#text");
  document.querySelector('#click').addEventListener('click',()=>{
    fetch('/greet')
    .then(response => response.json())
    .then(data => {p.innerHTML = data.message, console.log(data)});
  })
});