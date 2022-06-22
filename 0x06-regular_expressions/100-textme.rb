#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)\w*\S*(?=\])|(?<=to:).\S\d*|(?<=flags:)\S*(?=\])/).join(",")
