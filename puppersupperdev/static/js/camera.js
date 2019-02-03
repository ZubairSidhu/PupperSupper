// Grab elements, create settings, etc.
var video = document.getElementById('video');

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}

// Elements for taking the snapshot
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var video = document.getElementById('video');

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
  context.drawImage(video, 0, 0, 1200, 1200);
  var dataurl = canvas.toDataURL();
  var FD = new FormData();
  var xhr = new XMLHttpRequest();
  xhr.open("POST", 'http://127.0.0.1:8000/google', true);
  // xhr.setRequestHeader('Content-Type', 'multipart/form-data');
  FD.append('photo', dataurl);
  xhr.send(FD);

  // postData(dataurl);
  var output = dataurl;
  var sideEffects = document.getElementById('sideEffects');
  sideEffects.innerHTML = output;
});

