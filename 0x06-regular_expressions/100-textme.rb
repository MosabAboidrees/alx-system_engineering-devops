#!/usr/bin/env ruby
from = ARGV[0].scan(/\[from:(.+?)\]/).flatten.join
to = ARGV[0].scan(/\[to:(.+?)\]/).flatten.join
flags = ARGV[0].scan(/\[flags:(.+?)\]/).flatten.join
puts "#{from},#{to},#{flags}"
