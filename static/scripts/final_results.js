/*Parts of js code are based on free educational w3scools materials*/


var modal1 = document.getElementById('myModal1');

var img1 = document.getElementById('myImg1');
var modalImg1 = document.getElementById("img01");
var captionText1 = document.getElementById("caption1");
img1.onclick = function(){
  modal1.style.display = "block";
  modalImg1.src = this.src;
  captionText1.innerHTML = this.alt;
}

var span1 = document.getElementById("s_close1");

span1.onclick = function() {
  modal1.style.display = "none";
}

var modal2 = document.getElementById('myModal2');

var img2 = document.getElementById('myImg2');
var modalImg2 = document.getElementById("img02");
var captionText2 = document.getElementById("caption2");

img2.onclick = function(){
  modal2.style.display = "block";
  modalImg2.src = this.src;
  captionText2.innerHTML = this.alt;
}
var span2 = document.getElementById("s_close2");

span2.onclick = function() {
  modal2.style.display = "none";
}