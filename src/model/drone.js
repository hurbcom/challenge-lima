class Drone {
    constructor(id = 1, x = 0, y = 0, orientation = 'N', mapRange = [10,10]) {
        this._id = id;
        this._x = x;
        this._y = y;
        this._orientation = orientation;
        // Take a photo if Drone inicialize on correct position
        this._photos = 1;
        this._mapRange = mapRange;
        // Directions based on commands 'D' and 'E' for orientation
        this._directions = {
            'N': {'D': 'L', 'E': 'O'},
            'S': {'D': 'O', 'E': 'L'},
            'L': {'D': 'S', 'E': 'N'},
            'O': {'D': 'N', 'E': 'S'}
        };
        // Paces on grid based on face orientation
        this._paces = {
            'N': {'X': 0, 'Y': 1},
            'L': {'X': 1, 'Y': 0},
            'O': {'X': -1, 'Y': 0},
            'S': {'X': 0, 'Y': -1}
        };
    };
}
module.exports = Drone;