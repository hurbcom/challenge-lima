const saveInMemo = (memo, posX, posY) =>
    (memo[`${posX}x${posY}`] = true);

const isInMemo = (memo, posX, posY) =>
    (memo[`${posX}x${posY}`] === true);

const rotateRight = (facing) => {
    switch (facing) {
        case 'L': return 'S';
        case 'S': return 'O';
        case 'O': return 'N';
        default: return 'L';
    }
};

const rotateLeft = (facing) => {
    switch (facing) {
        case 'L': return 'N';
        case 'N': return 'O';
        case 'O': return 'S';
        default: return 'L';
    }
};

const getNextPos = (posX, posY, facing) => {
    switch (facing) {
        case 'N': return { posX: posX, posY: posY + 1 };
        case 'S': return { posX: posX, posY: posY - 1 };
        case 'L': return { posX: posX + 1, posY: posY };
        case 'O': return { posX: posX - 1, posY: posY };
    }
};

const getValidInstructions = (instructions) => {
    const lastF = instructions.lastIndexOf('F');
    if (lastF === -1) {
        return '';
    }
    return instructions.substring(0, lastF + 1);
};

const fly = (gridX, gridY, posX, posY, facing, instructions) => {
    let picturesTaken = 1;
    const memo = {};
    saveInMemo(memo, posX, posY);
    const validInstructions = getValidInstructions(instructions);
    validInstructions.split('').forEach(instruction => {
        if (instruction === 'E') {
            facing = rotateLeft(facing);
        }
        if (instruction === 'D') {
            facing = rotateRight(facing);
        }
        if (instruction === 'F') {
            const pos = getNextPos(posX, posY, facing);
            if (pos.posX > 0 && pos.posX <= gridX &&
                pos.posY > 0 && pos.posY <= gridY &&
                !isInMemo(memo, pos.posX, pos.posY)) {
                    picturesTaken++;
                    posX = pos.posX;
                    posY = pos.posY;
                    saveInMemo(memo, posX, posY);
            }
        }
    });
    return { posX, posY, facing, picturesTaken };
};

module.exports = { fly };
