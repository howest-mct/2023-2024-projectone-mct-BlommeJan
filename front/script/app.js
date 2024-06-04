const lanIP = `${window.location.hostname}:5000`;
const socketio = io(lanIP);

const listenToUI = function () {};

const listenToSocket = function () {
  socketio.on('connect', function () {
    console.log('verbonden met socket webserver');
  });
};

socketio.on("BTF_temp", function (value) {
  console.log(value.temp)
  temp = document.querySelector('.js-temp-value').innerHTML
  console.log(temp)
  temp = value.temp

  document.querySelector('.js-temp-value').innerHTML = temp
})

const init = function () {
  console.info('DOM geladen');
  listenToUI();
  listenToSocket();
};

document.addEventListener('DOMContentLoaded', init);