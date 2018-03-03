const Drone = require('../model/drone.js')

class DroneController extends Drone {
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

    get photos() {
        return this._photos;
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

    set photos(foto) {
        this._photos = this.photos + foto;
    }
    can_move() {
        var x = this._x + this._paces[this.orientation]['X'];
        var y = this._y + this._paces[this.orientation]['Y'];
        return (x >= 0 && x <= this._mapRange[0] && y >= 0 && y <= this._mapRange[1]);
    }

    move() {
        if (this.can_move()) {
            this.x = this._x + this._paces[this.orientation]['X'];
            this.y = this._y + this._paces[this.orientation]['Y'];
            this.photos = 1;
        }
        return [this.id, this.x, this.y];
    };
    
    turn(direction) {
        this.orientation = this._directions[this.orientation][direction];
    };
}

module.exports = DroneController;