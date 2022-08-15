# script that sets up your client SSH configuration file so that you can
# connect to a server without typing a password.
exec {'ssh_config':
    path    => '/usr/bin/',
    command => 'echo "IdentityFile ~/.ssh/school\n PasswordAuthentication no" >> /etc/ssh/ssh_config'
}