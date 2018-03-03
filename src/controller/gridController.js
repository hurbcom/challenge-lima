const Grid = require('../model/grid.js');

class GridController extends Grid {
    get map() {
        return this._map;
    }
    set map ( mapRange = [1,1,1]) {
        this._map[mapRange[1]][mapRange[2]] = mapRange[0];
    }
}

module.exports = GridController;