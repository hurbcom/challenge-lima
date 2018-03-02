class Monitor {
    constructor(map = [10,10]) {
        this._map = [];
        for (var x = 0; x <= map[0]; x++) {
            var columns = [];
            for (var y = 0; y <= map[1]; y++) {
                columns[y] = 0;
            }
            this._map[x] = columns;
        }
    }
    get map() {
        return this._map;
    }
    set map ( map = [1,1,1]) {
        this._map[map[1]][map[2]] = map[0];
    }
}

module.exports = Monitor;