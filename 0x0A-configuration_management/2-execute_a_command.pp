# Create a manifest that kills a process named killmenow
exec {'pkill -f killmenow':
    path     => ['/usr/bin'],
    provider => shell,
    command  => 'pkill -f killmenow'
}
