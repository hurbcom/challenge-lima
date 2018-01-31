# N -> Cima
# S -> baixo
# O -> esquerda
# L -> Direita
module Echo
  class Drone
    attr_accessor :x, :y, :orientation

    def initialize(space, x = 0, y = 0, orientation = 'S')
      @space = space
      @x = x
      @y = y
      @orientation = orientation.to_s.upcase.strip

      validates!
    end

    def move_sequence(sequence)
      commands = sequence.to_s.split('')
      commands.each do |command|
        case command.to_s.upcase.strip
          when 'D' then
            rotate
            right(1)
          when 'E' then
            rotate
            left(1)
          when 'F' then front(1)
        end
        yield if block_given?
      end
    end

    def rotate
      case @orientation
        when 'S' then @orientation = 'L'
        when 'L' then @orientation = 'N'
        when 'N' then @orientation = 'O'
        when 'O' then @orientation = 'S'
      end
    end

    def front(n)
      case @orientation
        when 'S' then move_y(n, true)
        when 'N' then move_y(n, false)
        when 'L' then move_x(n, true)
        when 'O' then move_x(n, false)
      end
    end

    def back(n)
      case @orientation
        when 'S' then move_y(n, false)
        when 'N' then move_y(n, true)
        when 'L' then move_x(n, false)
        when 'O' then move_x(n, true)
      end
    end

    def right(n)
      case @orientation
        when 'S' then move_x(n, false)
        when 'N' then move_x(n, true)
        when 'L' then move_y(n, true)
        when 'O' then move_y(n, false)
      end
    end

    def left(n)
      case @orientation
        when 'S' then move_x(n, true)
        when 'N' then move_x(n, false)
        when 'L' then move_y(n, false)
        when 'O' then move_y(n, true)
      end
    end

    private

    def move_y(n, positive = true)
      if positive
        @y = [ @y + n, @space.y - 1 ].min
      else
        @y = [ @y - n, 0 ].max
      end
    end

    def move_x(n, positive = true)
      if positive
        @x = [ @x + n, @space.x - 1 ].min
      else
        @x = [ @x - n, 0 ].max
      end
    end

    def validates!
      validates_x!
      validates_y!
      validates_orientation!
    end

    def validates_x!
      raise StandardError.new("Initialize position is not permited of x") unless x >= 0 && x < @space.x
    end

    def validates_y!
      raise StandardError.new("Initialize position is not permited of y") unless y >= 0 && y < @space.y
    end

    def validates_orientation!
      raise StandardError.new("Initialize orientation is not permited") unless ['S', 'N', 'L', 'O'].include?(orientation)
    end
  end
end