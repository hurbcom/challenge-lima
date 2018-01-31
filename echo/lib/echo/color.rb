module Echo
  class Color
    class << self
      def black(str)
        "\033[30m#{str}\033[0m"
      end

      def red(str)
        "\033[31m#{str}\033[0m"
      end

      def green(str)
        "\033[32m#{str}\033[0m"
      end

      def brown(str)
        "\033[33m#{str}\033[0m"
      end

      def blue(str)
        "\033[34m#{str}\033[0m"
      end

      def magenta(str)
        "\033[35m#{str}\033[0m"
      end

      def cyan(str)
        "\033[36m#{str}\033[0m"
      end

      def gray(str)
        "\033[37m#{str}\033[0m"
      end
    end
  end
end