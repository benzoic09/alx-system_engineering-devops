#!/usr/bin/pop
# installing flask
package { 'Flask':
  ensure   => '2.1.1',
  provider => 'gem'
  }
