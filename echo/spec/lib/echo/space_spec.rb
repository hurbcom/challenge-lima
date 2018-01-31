require_relative '../../spec_helper'

describe Echo::Space do
  context "#initialize" do
    it "should not initialize with negative dimentions" do
      expect { Echo::Space.new(-1, 10) }.to raise_error('x should grater than 0')
    end
  end
end