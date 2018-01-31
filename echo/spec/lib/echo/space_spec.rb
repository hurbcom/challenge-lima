require_relative '../../spec_helper'

describe Echo::Space do
  context "#move" do
    let(:space) { Echo::Space.new(10, 10) }
    let(:drone) { Echo::Drone.new(space, 0, 0, 'S') }

  end
end