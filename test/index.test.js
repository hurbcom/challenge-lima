const test = require('tape');
const Drone = require('../src/controller/droneController');
const Commands = require('../src/lib/commands');

test('Init Drone', (t) => {
    drone = new Drone(1,5,4,'L',[6,8]);
    t.assert(drone.x === 5, "X")
    t.assert(drone.y === 4, "Y")
    t.assert(drone.face === 'Leste', "Orientation L")
    t.end()
});

test('Move Drone', (t) => {
    drone = new Drone(1,5,4,'L',[6,8]);
    drone.move('D');
    drone.move('F');
    t.assert(drone.x === 5, "X")
    t.assert(drone.y === 3, "Y")
    t.assert(drone.face === 'Sul', "Orientation S")
    t.assert(drone.photos.length === 2, "Taken photos")
    t.end()
});

test('Commands check', (t) => {
    commands = new Commands;
    t.ok(commands.validate('1515SDFDEFDE'), 'Test with rigth command');
    t.notOk(commands.validate('1515DFDEFDE'), 'Test with wrong command');
    t.ok(commands.validateGrid('20x20'), 'Test with rigth grid range');
    t.notOk(commands.validateGrid('2000x20'), 'Test with wrong grid range');
    droneUtils = commands.partition('1515SDFDEFDE');
    t.equal(droneUtils.X,15)
    t.equal(droneUtils.Y,15)
    t.equal(droneUtils.orientation,'S')
    t.equal(droneUtils.commands,'DFDEFDE')
    t.end()
});