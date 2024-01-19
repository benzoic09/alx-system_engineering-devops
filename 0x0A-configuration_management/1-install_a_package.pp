#!/usr/bin/puppet

# Installing flask
package { 'Flask':
  ensure   => '2.1.1',
  provider => 'pip',
  command  => '/usr/bin/pip3',
}
