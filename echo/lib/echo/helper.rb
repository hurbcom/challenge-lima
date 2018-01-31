module Echo
  class Helper
    def self.print(space, x, y, char)
      matrix = []

      matrix << "   #{'N'.rjust(space.y*4/2, ' ')}"
      matrix << "   #{(0..(space.y-1)).map { |d| d.to_s.rjust(3, ' ')  }.join(" ")}"
      matrix << "    +#{'---+'*space.y}"

      (0..(space.x-1)).to_a.each do |nx|

        line = (0..(space.y-1)).to_a.map do |ny|
          if nx == x && ny == y
            " #{char} "
          else
            "   "
          end
        end

        matrix << "#{nx.to_s.rjust(3, ' ')} |#{line.join("|")}|"

        matrix << "    +#{'---+'*space.y}"
      end

      matrix << "   #{'S'.rjust(space.y*4/2, ' ')}"
      matrix << "\n"
      matrix.join("\n")
    end
  end
end