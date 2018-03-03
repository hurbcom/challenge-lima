class Commands {
    constructor() {

    }
    validate (command) {
        var regex = /^[0-9]{4}[NSLO][DEF]{1,}$/g;
        return regex.test(command);
    }
    parttition (command) {
        if (this.validate(command)) {
            var groups = /^([0-9]{2})([0-9]{2})([NSLO])([DEF]{1,})$/.exec(command);
            return {
                'X': groups[1], 
                'Y': groups[2],
                'orientation': groups[3],
                'commands': groups[4]
            };
        }
    }
}
module.exports = Commands;