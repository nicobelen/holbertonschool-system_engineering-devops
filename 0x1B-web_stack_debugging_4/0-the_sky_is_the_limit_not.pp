# Puppet script to correct falied requests on nginx
exec {
    'sed -i s/15/1000/ /etc/default/nginx':
    }
exec {
    'service nginx restart':
    }
