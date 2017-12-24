#!/usr/bin/env node

const drone = require('./source/drone');
const readline = require('readline');
const process = require('process');

let droneNumber = 1;

const getSequenceQuestion = () =>
`\nPlease inform the command sequence for drone ${droneNumber++} or leave empty to exit: `;

const getStartInformation = (posX, posY, facingName, sequence) =>
`- Drone initiated at position [${posX}, ${posY}] facing "${facingName}" with sequence "${sequence}"`;

let answers = [];

if (process.argv.length < 3) {
    process.exit(0);
}

const args = process.argv[2].split('x');
const gridX = Number(args[0]);
const gridY = Number(args[1]);

console.log(`Generating flying grid with dimensions of ${gridX}m by ${gridY}m.\n`);
console.log(getSequenceQuestion());

const readlineInterface = readline.createInterface({
    input: process.stdin, output: process.stdout, prompt: ''});

const getFacingName = (facing) => {
    switch (facing) {
        case 'L': return 'Leste';
        case 'O': return 'Oeste';
        case 'N': return 'Norte';
        default: return 'Sul';
    }
};

readlineInterface.prompt();
readlineInterface
    .on('line', (defaultLine) => {
        const line = defaultLine.trim();
        const posX = Number(line.substring(0, 2)) || 0;
        const posY = Number(line.substring(2, 4)) || 0;
        const facing = line[4] || 'S';
        const instructions = line.substring(5, line.length);

        if (line !== '') {
            console.log(getStartInformation(posX, posY, getFacingName(facing), instructions));
            const collectedInfo = drone.fly(gridX, gridY, posX, posY, facing, instructions);
            answers.push(collectedInfo);
            console.log(getSequenceQuestion());
        } else {
            console.log('Report:');
            answers.forEach((info, index) => {
                console.log(`- Drone ${index+1}`);
                console.log(` - Final position: [${info.posX}, ${info.posY}]`);
                console.log(` - Direction: ${getFacingName(info.facing)}`);
                console.log(` - Pictures taken: ${info.picturesTaken}\n`);
            });
            readlineInterface.close();
        }

        readlineInterface.prompt();
    })
    .on('close', () => process.exit(0));
