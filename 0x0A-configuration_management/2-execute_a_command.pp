#!/usr/bin/puppet

# Define a Puppet exec resource to kill the process
exec { 'pkill -f killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
  logoutput   => true,
}
