module Echo
  class Space
    attr_reader :x, :y

    def initialize(x, y)
      @x = x.to_i
      @y = y.to_i

      validates!
    end

    def permit_x?(new_x)
      new_x >= minx && new_x <= x
    end

    def permit_y?(new_y)
      new_y >= miny && new_y <= y
    end

    def minx
      1
    end

    def miny
      1
    end

    private

    def validates!
      validates_x!
      validates_y!
    end

    def validates_x!
      raise StandardError.new("x should grater than 0") if x <= 0
    end

    def validates_y!
      raise StandardError.new("y should grater than 0") if y <= 0
    end
  end
end