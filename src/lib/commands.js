class Commands {
    constructor() {

    }
    validate (command) {
        if (command != null){
            command = command.toUpperCase();
            var regex = /^[0-9]{4}[NSLO][DEF]{1,}$/g;
            return regex.test(command);
        }
        return false;
    }

    partition (command) {
        command = command.toUpperCase();
        if (this.validate(command)) {
            var groups = /^([0-9]{2})([0-9]{2})([NSLO])([DEF]{1,})$/.exec(command);
            return {
                'X': parseInt(groups[1]), 
                'Y': parseInt(groups[2]),
                'orientation': groups[3],
                'commands': groups[4]
            };
        }
    }

    validateGrid (command) {
        if (command != null){
            command = command.toUpperCase();
            var regex = /^[0-9]{2}[X][0-9]{2}$/g
            return regex.test(command);
        }
        return false;
    }

    partitionGrid (command) {
        command = command.toUpperCase();
        if (this.validateGrid(command)) {
            var groups = /^([0-9]{2})[X]([0-9]{2})$/.exec(command);
            return {
                'X': parseInt(groups[1]), 
                'Y': parseInt(groups[2]),
            };
        }
        else {
            return 0;
        }
    }
}

module.exports = Commands;