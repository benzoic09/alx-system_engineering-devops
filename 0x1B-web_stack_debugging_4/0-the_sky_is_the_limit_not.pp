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
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Define the script file
-> file { '/usr/local/bin/fix_nginx_errors.sh':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
  content => template('nginx/fix_nginx_errors.sh.erb'),
}
