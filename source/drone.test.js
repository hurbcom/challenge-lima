const drone = require('./drone');
const expect = require('chai').expect;

describe('drone', () => {
    it('should perform 15x30 0404ODDDDD correctly', () => {
        const info = drone.fly(15, 30, 4, 4, 'O', 'DDDDD');
        expect(info.posX).to.be.equal(4);
        expect(info.posY).to.be.equal(4);
        expect(info.facing).to.be.equal('O');
        expect(info.picturesTaken).to.be.equal(1);
    });

    it('should perform 15x30 0404ODDDDDF correctly', () => {
        const info = drone.fly(15, 30, 4, 4, 'O', 'DDDDDF');
        expect(info.posX).to.be.equal(4);
        expect(info.posY).to.be.equal(5);
        expect(info.facing).to.be.equal('N');
        expect(info.picturesTaken).to.be.equal(2);
    });

    it('should perform 10x20 0315ODEDEFFDFFD correctly', () => {
        const info = drone.fly(10, 20, 3, 15, 'O', 'DEDEFFDFFD');
        expect(info.posX).to.be.equal(1);
        expect(info.posY).to.be.equal(17);
        expect(info.facing).to.be.equal('N');
        expect(info.picturesTaken).to.be.equal(5);
    });

    it('should perform 10x20 0505LFFDFEFDDF correctly', () => {
        const info = drone.fly(10, 20, 5, 5, 'L', 'FFDFEFDDF');
        expect(info.posX).to.be.equal(8);
        expect(info.posY).to.be.equal(4);
        expect(info.facing).to.be.equal('O');
        expect(info.picturesTaken).to.be.equal(5);
    });

    it('should perform 10x20 0505LFFEEEEFFDF correctly', () => {
        const info = drone.fly(50, 20, 5, 5, 'L', 'FFEEEEFFDF');
        expect(info.posX).to.be.equal(9);
        expect(info.posY).to.be.equal(4);
        expect(info.facing).to.be.equal('S');
        expect(info.picturesTaken).to.be.equal(6);
    });
});
