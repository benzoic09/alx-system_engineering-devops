#!/usr/bin/pup
# Installing flask to get the api info

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip'
}
