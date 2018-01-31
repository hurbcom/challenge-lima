module Echo
  class Helper
    def self.print(drone)
      matrix = []

      matrix << "   #{(0..(@y-1)).map { |d| d.to_s.rjust(3, ' ')  }.join(" ")}"
      matrix << "    +#{'---+'*@y}"
      @x.times.each do |nx|

        line = (0..(@y-1)).to_a.map do |ny|
          "   "
        end

        matrix << "#{nx.to_s.rjust(3, ' ')} |#{line.join("|")}|"

        matrix << "    +#{'---+'*@y}"
      end
      matrix.join("\n")
    end
  end
end