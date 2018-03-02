const Drone = require('../src/drone.js')
const Monitor = require('../src/monitor.js')
drone = new Drone(1,5,3,'L',[10,10]);
monitor = new Monitor([10,10]);
monitor.map = drone.move();
drone.turn('D');
monitor.map = drone.move();
console.log('X:'+drone.x+', Y:'+drone.y+', face_camera:'+drone.orientation + ', fotos:'+drone.fotos);
console.log(monitor.map);