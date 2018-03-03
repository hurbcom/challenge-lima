const Grid = require('../src/controller/gridController.js');
grid = new Grid([3,5]);

grid.map = [1+'i',5,5];
grid.map = [1,6,5];
grid.map = [1,7,5];
grid.map = [1,7,4];
grid.map = [1,8,4];

console.log(grid.map);