# 101-setup_web_static.pp
# Configures web servers for deployment.

# Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$hostname;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt',
} ->

file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
} ->

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
} ->

file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  force   => true,
} ->

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
} ->

file { '/var/www':
  ensure  => 'directory',
} ->

file { '/var/www/html':
  ensure  => 'directory',
} ->

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Holberton School Nginx\n',
} ->

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
} ->

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf,
  notify  => Service['nginx'],
} ->

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
} ->

exec { 'nginx restart':
  path => '/etc/init.d/',
}
