class Grid {
    constructor(mapRange = [1,1]) {
        this._mapRange = [mapRange[0]-1, mapRange[1]-1]
        this._map = [];
        for (var y = 0; y <= mapRange[1]-1; y++) {
            var columns = [];
            for (var x = 0; x <= mapRange[0]-1; x++) {
                columns[x] = '  ';
            }
            this._map[y] = columns;
        }
    }

    get map() {
        return this._map.reverse();
    }

    set map ( coord = [1,1,1]) {
        this._map[coord[2]-1][coord[1]-1] = coord[0].toString().padStart(2,"_");
    }

    can_init (coord = [1,1]) {
        if (this._mapRange[0] < coord[0]-1 || this._mapRange[1] < coord[1]-1) {
            return false;
        }
        if (this._map[coord[1]-1][coord[0]-1].toString().indexOf('i') > -1) {
            return false;
        }
        return true;
    }
}

module.exports = Grid;