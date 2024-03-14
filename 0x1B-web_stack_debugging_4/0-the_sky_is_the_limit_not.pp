# Puppet manifest to fix multiple server errors in Nginx server

# Define Nginx configuration file
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Define Exec resource to run the script
exec { 'fix_failed_requests':
  command     => '/usr/local/bin/fix_failed_requests.sh',
  refreshonly => true,  # Only run when the nginx.conf file changes
  subscribe   => File['/etc/nginx/nginx.conf'],
}

# Define the script file
file { '/usr/local/bin/fix_failed_requests.sh':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
  content => template('nginx/fix_failed_requests.sh.erb'),
}
