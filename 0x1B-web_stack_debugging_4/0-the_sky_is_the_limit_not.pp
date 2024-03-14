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

# Define Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

