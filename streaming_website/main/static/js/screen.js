let share_start = document.querySelector("#start-screen");
let share_stop = document.querySelector("#stop-screen");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let image = document.querySelector("#image");


let stream = null;
let recorder = null;
let blobs_recorded = [];

share_start.addEventListener("click", async () => {
  // Prompt the user to share their screen.
  stream = await navigator.mediaDevices.getDisplayMedia();
  video.srcObject = stream;
});

share_stop.addEventListener("click", () => {
  // Stop the stream.
  stream.getTracks().forEach(track => track.stop());
  video.srcObject = null;
});

start_button.addEventListener("click", async () => {
  recorder = new MediaRecorder(stream, { mimeType: 'video/webm' });

    // event : new recorded video blob available
    recorder.addEventListener('dataavailable', function(e) {
		blobs_recorded.push(e.data);
		const blobToImage = (e.data) => {
          return new Promise(resolve => {
            const url = URL.createObjectURL(e.data);
            image.onload = () => {
              URL.revokeObjectURL(url);
              resolve(image);
            }
          image.src = url;
          })
        }
    });

    // event : recording stopped & all blobs sent
    recorder.addEventListener('stop', function() {
    	// create local object URL from the recorded video blobs
    	let video_local = new Blob(blobs_recorded, { type: 'video/webm' });

        const fileInput = document.querySelector('input[type="file"]');

        // Create a new File object
        const myFile = new File([video_local], 'video.webm', {
            type: 'video/webm',
            lastModified: new Date(),
        });

        // Now let's create a DataTransfer to get a FileList
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(myFile);
        fileInput.files = dataTransfer.files;
        });

    // start recording with each recorded blob having 1 second video
    recorder.start(1000);
});

stop_button.addEventListener('click', function() {
	recorder.stop();
});
