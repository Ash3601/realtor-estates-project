const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();
console.log("In main js");
setTimeout(function() {
  console.log("In timout method");
  $("#message").fadeOut("slow");
}, 3000);
