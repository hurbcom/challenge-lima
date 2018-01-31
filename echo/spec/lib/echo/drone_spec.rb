require_relative '../../spec_helper'

describe Echo::Drone do
  context "#initialize" do
    let(:space) { Echo::Space.new(10, 10) }

    it "should with default config" do
      drone = Echo::Drone.new(space)
      expect( drone.x ).to eq(0)
      expect( drone.y ).to eq(0)
      expect( drone.orientation ).to eq('S')
    end

    it "should raise exception when inicialize with x invalid" do
      expect { Echo::Drone.new(space, 10) }.to raise_error('Initialize position is not permited of x')
    end

    it "should raise exception when inicialize with y invalid" do
      expect { Echo::Drone.new(space, 0, 10) }.to raise_error('Initialize position is not permited of y')
    end

    it "should raise exception when inicialize with orientation invalid" do
      expect { Echo::Drone.new(space, 0, 0, 'D') }.to raise_error('Initialize orientation is not permited')
    end
  end

  context "#rotate" do
    let(:space) { Echo::Space.new(10, 10) }
    let(:drone) { Echo::Drone.new(space, 5, 5, 'S') }

    it "should rotate correct drone" do
      expect( drone.orientation ).to eq('S')
      drone.rotate
      expect( drone.orientation ).to eq('O')
      drone.rotate
      expect( drone.orientation ).to eq('N')
      drone.rotate
      expect( drone.orientation ).to eq('L')
    end
  end

  context "#move" do
    let(:space) { Echo::Space.new(10, 10) }

    context "orientation S" do
      let(:drone) { Echo::Drone.new(space, 5, 5, 'S') }

      it "front" do
        drone.front(2)
        expect(drone.y).to eq(7)

        drone.front(10)
        expect(drone.y).to eq(9)
      end

      it "back" do
        drone.back(2)
        expect(drone.y).to eq(3)

        drone.back(10)
        expect(drone.y).to eq(0)
      end

      it "right" do
        drone.right(2)
        expect(drone.x).to eq(3)

        drone.right(10)
        expect(drone.x).to eq(0)
      end

      it "left" do
        drone.left(2)
        expect(drone.x).to eq(7)

        drone.left(10)
        expect(drone.x).to eq(9)
      end
    end

    context "orientation N" do
      let(:drone) { Echo::Drone.new(space, 5, 5, 'N') }

      it "front" do
        drone.front(2)
        expect(drone.y).to eq(3)
      end

      it "back" do
        drone.back(2)
        expect(drone.y).to eq(7)
      end

      it "right" do
        drone.right(2)
        expect(drone.x).to eq(7)
      end

      it "left" do
        drone.left(2)
        expect(drone.x).to eq(3)
      end
    end

    context "orientation L" do
      let(:drone) { Echo::Drone.new(space, 5, 5, 'L') }

      it "front" do
        drone.front(2)
        expect(drone.x).to eq(7)
      end

      it "back" do
        drone.back(2)
        expect(drone.x).to eq(3)
      end

      it "right" do
        drone.right(2)
        expect(drone.y).to eq(7)
      end

      it "left" do
        drone.left(2)
        expect(drone.y).to eq(3)
      end
    end

    context "orientation O" do
      let(:drone) { Echo::Drone.new(space, 5, 5, 'O') }

      it "front" do
        drone.front(2)
        expect(drone.x).to eq(3)
      end

      it "back" do
        drone.back(2)
        expect(drone.x).to eq(7)
      end

      it "right" do
        drone.right(2)
        expect(drone.y).to eq(3)
      end

      it "left" do
        drone.left(2)
        expect(drone.y).to eq(7)
      end
    end
  end

  context "#move_sequence" do
    let(:space) { Echo::Space.new(10, 10) }
    let(:drone) { Echo::Drone.new(space, 5, 5, 'S') }

    it "should move correct sequence" do
      drone.move_sequence('DFFEEFDFE')

      expect( drone.orientation ).to eq('O')
      expect( drone.y ).to eq(5)
      expect( drone.x ).to eq(2)
    end
  end
end