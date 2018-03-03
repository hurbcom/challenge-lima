const DroneController = require('../src/controller/droneController.js')
const Commands1 = require('../src/controller/commands.js')
const Grid = require('../src/model/grid.js')
grid = new Grid([10,10]);
drone = new DroneController(1,5,3,'L',[10,10]);
var commands = new Commands1;
grid.map = [1+'i',5,3];
grid.map = drone.move();
drone.turn('D');
grid.map = drone.move();

console.log('X:'+drone.x+', Y:'+drone.y+', face_camera:'+drone.orientation + ', fotos:'+drone.fotos);
console.log(grid.map);
