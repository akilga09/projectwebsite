 navigator.mediaDevices.getUserMedia({
    video: true
    })
    .then(stream=> {
    document.getElementById("vid").srcObject = stream;
    })