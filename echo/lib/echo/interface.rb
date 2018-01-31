module Echo
  class Interface
    attr_reader :space, :drones

    def initialize(dimentions)
      x, y = dimentions.to_s.split("x")
      @space = Echo::Space.new(x, y)
      @drones = []
      ARGV.clear
    end

    def start
      puts "Generated new Space with #{space.x}m by #{space.y}m."
      loop do
        print_menu_description
        case STDIN.gets.chomp[0].downcase
        when 'n' then new_drone
        when 'p' then print_report
        when 'q' then print_report; break
        when ''  then print_report; break
        end
      end
    end

    private

      def print_menu_description
        puts %{
- Menu
 - h : help
 - n : new drone
 - p : print report
 - q : exit
}
      end

      def print_menu_drone
        puts %{
- Please insert position and orientation for Drone #{drones.size + 1}.
 - ex.: 3 3 N
 - press enter to go menu
 - possible orientations:
   - N -> North
   - S -> South
   - O -> West
   - L -> East
}
      end

      def new_drone
        loop do
          print_menu_drone
          arguments = STDIN.gets.chomp.split(/[\s\;\,\-\t]+/).compact[0..2]

          break if arguments.empty?

          begin
            drone = Echo::Drone.new(space, *arguments)
            move_drone(drone)
            drones << drone
            break
          rescue => e
            puts ""
            puts "Error: #{e.message}"
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
        puts ""
        puts "Reports"
        drones.each_with_index do |drone, index|
          puts "- Drone #{index+1}"
          drone.report
          puts ""
        end
        puts ""
      end
  end
end