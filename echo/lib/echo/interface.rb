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
      puts Echo::Color.green("Generated new Space with #{space.x}m by #{space.y}m.")
      loop do
        print_menu_description
        case STDIN.gets.chomp[0].to_s.strip.downcase
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
#{Echo::Color.blue("- Menu")}
 - h : help
 - n : new drone
 - p : print report
 - q : exit
}
      end

      def print_menu_drone
        title = Echo::Color.blue("- Please insert position and orientation for Drone #{drones.size + 1}")
        puts %{
#{title}
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
        title = Echo::Color.blue("Please insert movement sequence:")
      puts %{
#{title}
 - ex.: DFFFEDF
 - F -> go forward
 - D -> go right and rotate 90 degress
 - E -> go left and rotate -90 degress
}
        sequence = STDIN.gets.chomp
        drone.print
        drone.move_sequence(sequence) do
          drone.print
        end
      end

      def print_report
        puts Echo::Color.blue("\nReports\n")
        drones.each_with_index do |drone, index|
          puts Echo::Color.green("- Drone #{index+1}")
          drone.report
          puts ""
        end
        puts ""
      end
  end
end