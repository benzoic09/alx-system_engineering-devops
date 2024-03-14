# Puppet manifest to fix server errors in Nginx server

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
exec { 'fix_nginx_errors':
  command     => '/usr/local/bin/fix_nginx_errors.sh',
  path        => ['/usr/local/bin', '/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
}

# Define the script file
file { '/usr/local/bin/fix_nginx_errors.sh':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
  content => template('nginx/fix_nginx_errors.sh.erb'),
}
