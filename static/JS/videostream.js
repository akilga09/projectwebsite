function openNav() {
  document.getElementById("myNav").style.width = "50%";
}

function closeNav() {
  document.getElementById("myNav").style.width = "0%";
}

 navigator.mediaDevices.getUserMedia({
    video: true
    })
    .then(stream=> {
    document.getElementById("vid").srcObject = stream;
    })