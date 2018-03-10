#!/usr/bin/env node

const util = require("util");
const readlineSync = require("readline-sync");
const Commands = require('./src/lib/commands.js');
const Grid = require('./src/lib/grid.js');
const Drone = require('./src/lib/drone.js');

command = new Commands;


//Chech if grid parameter is rigth
if (!command.validateGrid(process.argv[2])){
    console.log('Grid initialization failed. Wrong format.');
    console.log('Run again and try like this 08x11');
    process.exit(1);
}

gridRange = command.partitionGrid(process.argv[2]);
console.log(util.format('Generating flying grid with dimentions of %dm by %dm \n', gridRange.X, gridRange.Y));

grid = new Grid([gridRange.X, gridRange.Y]);

function report(droneId, finalPosition=[1,1], direction, photos) {
    console.log(util.format('- Drone %d:', droneId));                                                                                                                                                            
    console.log(util.format('  - Final position: [%d, %d]', finalPosition.X, finalPosition.Y));                                                                                                                                        
    console.log(util.format('  - Direction: %s', direction));
    console.log(util.format('  - Pictures taken: %d \n', photos));
};

var commandStr,
    droneCount = 1,
    dronesArr = [];
do {
    repeat = true;
    try {
        // Get command from User
        commandStr = readlineSync.question(util.format('Please inform the command sequence for drone %d or leave empty to exit : ', droneCount));
    } catch (e) {
        console.error(e);
        process.exit(1);
    }
    if (commandStr.length > 0) {
        if (command.validate(commandStr)){
            droneUtils = command.partition(commandStr);
            // Verify if coordinates is free or init by another drone 
            if (grid.can_init([droneUtils.X, droneUtils.Y])) {
                drone = new Drone(droneCount, droneUtils.X, droneUtils.Y, droneUtils.orientation, [gridRange.X,gridRange.Y]);
                grid.map = [droneCount+'i', droneUtils.X, droneUtils.Y];
                console.log(util.format('- Drone initiated at position [%d, %d] facing "%s" with sequence "%s"', droneUtils.X, droneUtils.Y, drone.face, droneUtils.commands));
                // Pass to drone one per one command
                for (var i = 0, len = droneUtils.commands.length; i < len; i++) {
                    position = drone.move(droneUtils.commands[i]);
                    (position)?grid.map = position:null;
                }
                droneCount++;
                // Save information for reporting
                dronesArr.push({
                    'droneId': drone.id, 
                    'finalPosition': {'X':drone.x, 'Y': drone.y},
                    'direction': drone.face,
                    'photos': drone.photos.length

                });
                drone = null;
            } else if (droneUtils.X > gridRange.X || droneUtils.Y > gridRange.Y ) {
                console.log(util.format('You cant start drone at [%d,%d], Grid out of range [%d,%d]', droneUtils.X, droneUtils.Y, gridRange.X, gridRange.Y))
            } else {
                console.log(util.format('This drone can`t init in [%d, %d] because another drone init here.', droneUtils.X, droneUtils.Y));
                console.log(util.format('For drone %d, try again!', droneCount));
            }
        } else {
            console.log('WORNG command format. Try this format [0-9][0-9][0-9][0-9][NSLO][DEF]{1,}');
            console.log('Ex: 0315ODEDEFFDFFD')
        }
    } else {
        console.log('...exiting \n\n');
        repeat = false;
        // Print report saved on previus array
        for (var i = 0, len = dronesArr.length; i < len; i++) {
            report(dronesArr[i].droneId, dronesArr[i].finalPosition, dronesArr[i].direction, dronesArr[i].photos);
        }
    };
}
while (repeat);

// offer to user the option to print the grid
if (readlineSync.keyInYN('Do you want to print GRID?')) {
    grid.map.forEach(
        function(line){
            console.log(JSON.stringify(line, undefined, ''))

    })
}