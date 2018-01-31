module Echo
  class Space
    attr_reader :x, :y

    def initialize(x, y)
      @x = x.to_i
      @y = y.to_i
    end
  end
end