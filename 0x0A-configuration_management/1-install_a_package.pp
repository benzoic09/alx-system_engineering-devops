# installing flask

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
  require  => Package['python3-pip']
}
exec { 'install_flask':
}
