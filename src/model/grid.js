class Monitor {
    constructor(mapRange = [10,10]) {
        this._map = [];
        for (var x = 0; x <= mapRange[0]; x++) {
            var columns = [];
            for (var y = 0; y <= mapRange[1]; y++) {
                columns[y] = 0;
            }
            this._map[x] = columns;
        }
    }
    get map() {
        return this._map;
    }
    set map ( mapRange = [1,1,1]) {
        this._map[mapRange[1]][mapRange[2]] = mapRange[0];
    }
}

module.exports = Monitor;