class Drone {
    constructor(id = 1, x = 0, y = 0, orientation = 'N', map = [10,10]) {
        this._id = id;
        this._x = x;
        this._y = y;
        this._orientation = orientation;
        this._fotos = 1;
        this.directions = {
            'N': {'D': 'L', 'E': 'O'},
            'S': {'D': 'O', 'E': 'L'},
            'L': {'D': 'S', 'E': 'N'},
            'O': {'D': 'N', 'E': 'S'}
        };
        this.paces = {
            'N': {'X': 0, 'Y': 1},
            'L': {'X': 1, 'Y': 0},
            'O': {'X': -1, 'Y': 0},
            'S': {'X': 0, 'Y': -1}
        };
        this.map = map;
    };

    get id() {
        return this._id;
    }

    get x() {
        return this._x;
    }

    get y() {
        return this._y;
    }

    get orientation(){
        return this._orientation;
    }

    get fotos() {
        return this._fotos;
    }

    set x(x) {
        this._x = x;
    }

    set y(y) {
        this._y = y;
    }

    set orientation(orientation){
        this._orientation = orientation;
    }

    set fotos(foto) {
        this._fotos = this.fotos + foto;
    }
    can_move() {
        var x = this._x + this.paces[this.orientation]['X'];
        var y = this._y + this.paces[this.orientation]['Y'];
        return (x >= 0 && x <= this.map[0] && y >= 0 && y <= this.map[1]);
    }

    move() {
        if (this.can_move()) {
            this.x = this._x + this.paces[this.orientation]['X'];
            this.y = this._y + this.paces[this.orientation]['Y'];
            this.fotos = 1;
        }
        return [this.id, this.x, this.y];
    };
    
    turn(direction) {
        this.orientation = this.directions[this.orientation][direction];
    };
}
module.exports = Drone;