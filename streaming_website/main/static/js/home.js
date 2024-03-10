//const data = document.currentScript.dataset;
//const token = data.token;
//
//function getName() {
//    return +new Date()
//}
//
//const STREAM_NAME = getName()
//const video = document.querySelector('#video');
//const mediaSource = new MediaSource();
//
//
//
//async function sendFile(file, chunkNumber) {
//    const formData = new FormData();
//
//    formData.append('file', file);
//    formData.append('name', JSON.stringify(STREAM_NAME));
//    formData.append('chunk', JSON.stringify(chunkNumber));
//
//    await fetch('/main/post/', {
//        method: 'POST',
//        body: formData,
//    });
//}
//
// function registerRecord(stream) {
//    const mediaRecorder = new MediaRecorder(stream)
//    let countUploadChunk = 0
//
//    mediaRecorder.start()
//
//    setInterval(() => {
//        mediaRecorder.requestData()
//    }, 2000)
//
//    mediaRecorder.ondataavailable = (data) => {
//        sendFile(data.data, countUploadChunk)
//        countUploadChunk++
//    }
//}
//
//function registerPlayer(mediaSource) {
//    const videoBuffer = mediaSource.addSourceBuffer('video/webm;codecs=vp8');
//    let countDownloadChunk = 0
//
//    setInterval(() => {
//        fetch(`/main/get/${STREAM_NAME}/${countDownloadChunk}`)
//            .then((response) => {
//                if (response.status !== 200) {
//                    throw Error('no such file')
//                }
//                return response
//            }).then((buffer) => {
//                countDownloadChunk++
//                mediaSource.addSourceBuffer(buffer)
//            }).catch(() => {})
//    }, 1000)
//}
//
//async function processStream(stream, mediaSource) {
//    await registerRecord(stream)
//    registerPlayer(mediaSource)
//}

//navigator.mediaDevices.getUserMedia({
//    video: true,
//}).then((stream) => {await processStream(stream, mediaSource)});
//video.src = URL.createObjectURL(mediaSource);


function getName() {
    return +new Date()
}

const STREAM_NAME = getName();
video = document.querySelector('#video');

navigator.mediaDevices.getUserMedia({
        video: {width: 1280},
    })
    .then(stream=>{
        video.srcObject = stream
        video.addEventListener('loadeddata', predict)
        })


function predict  (stream) {
try{
   const formData = new FormData();
   let chunkNumber = 0;
   formData.append('file', stream);
   formData.append('name', JSON.stringify(STREAM_NAME));
   formData.append('chunk', JSON.stringify(chunkNumber));
   fetch('/main/post/', {
        method: 'POST',
        body: formData,
   });
   chunkNumber++
requestAnimationFrame(predict)}
catch(e){console.log(e)}
}
