module Echo
  class Interface
    attr_reader :space, :drones

    def initialize(dimentions)
      x, y = dimentions.split("x")
      @space = Echo::Space.new(x, y)
      @drones = []
      ARGV.clear
    end

    def start
      puts "Generated new Space with #{space.x}m by #{space.y}m."
      puts ""
      menu
    end

    private

      def menu
        loop do
          puts "Menu"
          puts "  \"h\" for help"
          puts "  \"n\" for new drone"
          puts "  \"p\" for print report"
          puts "  \"q\" for exit"
          case STDIN.gets.chomp[0].downcase
          when 'n' then new_drone
          when 'p' then print_report
          when 'q' then
            print_report
            break
          end
        end
      end

      def new_drone
        loop do
          puts "Drone #{drones.size + 1}"
          puts "Please insert position and orientation."
          puts "  ex.: 3 3 N"
          puts "  possible orientations:\n\tN -> North, S -> South, O -> West and L -> East"
          params = STDIN.gets.chomp
          arguments = params.split("").compact[0..2]

          break if arguments.empty?

          begin
            drone = Echo::Drone.new(space, *arguments)
            move_drone(drone)
            drones << drone
            break
          rescue => e
            puts ""
            puts e.message
            puts ""
          end
        end
      end

      def move_drone(drone)
        puts "Please insert movement sequence:"
        sequence = STDIN.gets.chomp
        drone.print
        drone.move_sequence(sequence) do
          drone.print
        end
      end

      def print_report
        puts "print_report"
      end

      # def readline
      #   line = nil
      #   while line = gets("\n")
      #     puts line
      #   end
      # end
  end
end