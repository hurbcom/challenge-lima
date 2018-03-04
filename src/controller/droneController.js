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

    set photos(coord = []) {
        this._photos.push(coord);
    }
    get face() {
        return this._directions[this.orientation]['name'];
    }

    //Verify next step in de grid range
    can_move() {
        var x = this._x + this._paces[this.orientation]['X'];
        var y = this._y + this._paces[this.orientation]['Y'];
        return (x > 0 && x <= this._mapRange[0] && y > 0 && y <= this._mapRange[1]);
    }

    //Move only forward with orientation based
    move(command) {
        if (this.can_move() && command === 'F') {
            this.x = this._x + this._paces[this.orientation]['X'];
            this.y = this._y + this._paces[this.orientation]['Y'];
            this.take_photo();
            return [this.id, this.x, this.y];
        } 
        if (command === 'D' || command === 'E'){
            this.turn(command);
            return null;
        }
    };

    take_photo(){
        if(JSON.stringify(this.photos).indexOf(JSON.stringify([this.x, this.y])) == -1){
            this.photos = [this.x, this.y];
        }
    }
    
    // Turn 90° to Left (E) or Rigth (D) with orientation based 
    turn(direction) {
        this.orientation = this._directions[this.orientation][direction];
    };
}

module.exports = DroneController;