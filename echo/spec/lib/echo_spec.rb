require_relative '../spec_helper'

describe Echo do
  it "should return a correct version" do
    expect( Echo.version ).to eq('0.0.1')
  end
end