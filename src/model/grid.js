class Grid {
    constructor(mapRange = [1,1]) {
        this._map = [];
        for (var y = 0; y <= mapRange[1]-1; y++) {
            var columns = [];
            for (var x = 0; x <= mapRange[0]-1; x++) {
                columns[x] = '  ';
            }
            this._map[y] = columns;
        }
    }
}

module.exports = Grid;