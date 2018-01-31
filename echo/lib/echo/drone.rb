# N -> Cima
# S -> baixo
# O -> esquerda
# L -> Direita
module Echo
  class Drone
    attr_accessor :space, :x, :y, :orientation, :pictures

    def initialize(space, new_x = 1, new_y = 1, orientation = 'S')
      @space = space
      @x = new_x.to_i
      @y = new_y.to_i
      @orientation = orientation.to_s.upcase.strip
      @pictures = []

      validates!
    end

    def print
      system "clear"
      puts Echo::Helper.print(space, y, x, arrow)
      sleep 1
    end

    def report
      puts " - photos taken: #{pictures.size}"
      puts " - position: x: #{x} y: #{y}"
      puts " - orientation: x: #{x} y: #{y}"
    end

    def arrow
      case @orientation
        when 'N' then "↑"
        when 'L' then "→"
        when 'S' then "↓"
        when 'O' then "←"
      end
    end

    def move_sequence(sequence)
      commands = sequence.to_s.split('')
      commands.each do |command|
        case command.to_s.upcase.strip
          when 'D' then
            right(1)
            rotate
            take_photo
          when 'E' then
            left(1)
            rotate_inverse
            take_photo
          when 'F' then front(1)
        end
        yield if block_given?
      end
    end

    def take_photo
      @pictures << { x: x, y: x, orientation: orientation }
    end

    def rotate
      case @orientation
        when 'N' then @orientation = 'L'
        when 'L' then @orientation = 'S'
        when 'S' then @orientation = 'O'
        when 'O' then @orientation = 'N'
      end
    end

    def rotate_inverse
      case @orientation
        when 'N' then @orientation = 'O'
        when 'L' then @orientation = 'N'
        when 'S' then @orientation = 'L'
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
        @y = [ @y + n, space.y ].min
      else
        @y = [ @y - n, space.miny ].max
      end
    end

    def move_x(n, positive = true)
      if positive
        @x = [ @x + n, space.x ].min
      else
        @x = [ @x - n, space.minx ].max
      end
    end

    def validates!
      validates_x!
      validates_y!
      validates_orientation!
    end

    def validates_x!
      raise StandardError.new("Initialize position is not permited of x") unless space.permit_x?(x)
    end

    def validates_y!
      raise StandardError.new("Initialize position is not permited of y") unless space.permit_y?(y)
    end

    def validates_orientation!
      raise StandardError.new("Initialize orientation is not permited") unless ['S', 'N', 'L', 'O'].include?(orientation)
    end
  end
end