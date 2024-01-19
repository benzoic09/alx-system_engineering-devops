#!/usr/bin/puppet

# Define a Puppet exec resource to kill the process
exec { 'killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
  logoutput   => true,
}

notify { 'Process killed':
  subscribe => Exec['killmenow_process'],
}
